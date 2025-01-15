import os
import glob
import time
import argparse
import requests
import logging
from pathlib import Path
from huggingface_hub import HfApi, hf_hub_url
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def format_size(size):
    """Formats a file size into a human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def find_files(file_location, file_type, sort_by='date'):
    """Finds files matching the selected file type in the given directory."""
    try:
        file_location = os.path.abspath(os.path.normpath(file_location))  # Absolute and normalized path
        all_files = glob.glob(os.path.join(file_location, f"*.{file_type}"))
        filtered_files = []
        for file_path in all_files:
            if os.path.islink(file_path):
                logging.warning(f"⚠️ Skipping symlink {file_path}")
                continue
            if not os.path.isfile(file_path):
                logging.warning(f"⚠️ Skipping non-file {file_path}")
                continue

            filtered_files.append(file_path)

        files = sorted(
            filtered_files,
            key=os.path.getmtime if sort_by == 'date' else str
        )
        return files
    except OSError as e:
        logging.error(f"❌ Error finding files: {e}")
        return []

def upload_files(hfuser, hfrepo, file_location, file_type, commit_message, create_pr, repo_type, repo_folder, dry_run=False):
    """Uploads selected files to the Hugging Face repository."""
    if not hfuser or not hfrepo:
        logging.error("❗ Please enter both your Organization/Username and Repository name.")
        return
    if not file_location:
        logging.error("❌ No directory was selected!")
        return

    file_location = os.path.abspath(os.path.normpath(file_location)) # Absolute and normalized path
    files = find_files(file_location, file_type)
    if not files:
      logging.info("📝 No files found matching your criteria. Check your file type and ensure files are in the location specified.")
      return

    api = HfApi()
    repo_id = f"{hfuser}/{hfrepo}"
    logging.info(f"🎯 Preparing to upload to: huggingface.co/{repo_id}")

    total_files = len(files)
    logging.info(f"\n🚀 Starting upload of {total_files} file(s)...")

    with tqdm(total=total_files, desc="Total Progress", unit="file") as pbar_total:
        for idx, file in enumerate(files, 1):
            size = os.path.getsize(file)
            logging.info(f"\n📦 Uploading file {idx}/{total_files}: {file} ({format_size(size)})")

            try:
                start_time = time.time()

                path_in_repo = os.path.basename(file)
                path_parts = Path(file).parts
                if len(path_parts) > 1:
                    folder_path_parts = path_parts[len(Path(file_location).parts):-1]
                    if folder_path_parts:
                        path_in_repo = os.path.join(*folder_path_parts, os.path.basename(file))

                if repo_folder:
                    path_in_repo = os.path.join(repo_folder, path_in_repo)

                # Check if file exists (optional)
                # url = hf_hub_url(repo_id, filename=path_in_repo, repo_type=repo_type)
                # if api.file_exists(repo_id, path_in_repo, repo_type=repo_type):
                #     logging.warning(f"File {path_in_repo} already exists in the repository. Skipping.")
                #     continue
                if dry_run:
                    logging.info(f"[Dry Run] Would upload: {file} to {path_in_repo}")
                else:
                    # Upload with a progress bar for each file
                    with tqdm(total=size, desc=f"Uploading {os.path.basename(file)}", unit="B", unit_scale=True, unit_divisor=1024) as pbar_file:
                        def progress_callback(uploaded_bytes, total_bytes):
                            pbar_file.update(uploaded_bytes - pbar_file.n)

                        response = None  # Initialize response to None
                        retries = 0
                        max_retries = 3
                        retry_delay = 5  # seconds

                        while retries < max_retries:
                          try:
                            response = api.upload_file(
                                path_or_fileobj=file,
                                path_in_repo=path_in_repo,
                                repo_id=repo_id,
                                repo_type=repo_type,
                                create_pr=create_pr,
                                commit_message=commit_message,
                                progress_callback=progress_callback,
                            )
                            break  # If successful, break out of the retry loop
                          except requests.exceptions.RequestException as e:
                            logging.warning(f"⚠️ Upload failed: {e}")
                            retries += 1
                            if retries < max_retries:
                                logging.info(f"Retrying in {retry_delay} seconds... ({retries}/{max_retries})")
                                time.sleep(retry_delay)
                                retry_delay *= 2 # Exponential backoff
                            else:
                                logging.error(f"❌ Upload failed after multiple retries.")

                if response is not None:
                    duration = time.time() - start_time
                    logging.info(f"✅ Upload completed in {duration:.1f} seconds")

            except OSError as e:
                logging.error(f"❌ Error uploading {file}: {e}")

            pbar_total.update(1)

    logging.info("\n✨ All uploads complete!")
    if create_pr:
        logging.info("🎉 Check your repository for the new Pull Request!")
    else:
        logging.info("🎉 Files uploaded directly to your repository!")

if __name__ == "__main__":
    print("🌟 Hugging Face File Uploader - Standalone 🌟")

    parser = argparse.ArgumentParser(description="Upload files to the Hugging Face Hub.")
    parser.add_argument("hfuser", type=str, help="Hugging Face Username/Organization")
    parser.add_argument("hfrepo", type=str, help="Hugging Face Repository Name")
    parser.add_argument("file_type", type=str, help="File type to upload (e.g., safetensors, txt, mp3).")
    parser.add_argument("file_location", type=str, help="Path to the directory to search for files.")
    parser.add_argument("--commit_message", type=str, default="Uploaded with Earth & Dusk Huggingface 🤗 Backup", help="Commit message (optional).")
    parser.add_argument("--create_pr", action="store_true", help="Create a pull request (optional).")
    parser.add_argument("--repo_type", type=str, default="model", choices=["model", "dataset", "space"], help="Repository type (model, dataset, space).")
    parser.add_argument("--repo_folder", type=str, default="", help="Optional folder inside the repo to upload to.")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Simulate the upload process without actually uploading files.")
    args = parser.parse_args()

    upload_files(
        args.hfuser,
        args.hfrepo,
        args.file_location,
        args.file_type,
        args.commit_message,
        args.create_pr,
        args.repo_type,
        args.repo_folder,
        args.dry_run
    )
