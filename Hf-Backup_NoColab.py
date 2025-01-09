import os
import glob
import time
from pathlib import Path
from huggingface_hub import HfApi
from tqdm import tqdm
import argparse

def format_size(size):
    """Formats a file size into a human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def find_files(file_location, file_type, sort_by='date'):
    """Finds files matching the selected file type in the given directory.

        Args:
            file_location (str): The path to the directory to search.
            file_type (str): The file extension (e.g., "safetensors", "txt").
            sort_by (str): How to sort the files: 'date' or 'name'. Defaults to 'date'.

        Returns:
            list: A list of file paths sorted by modified date or name.
    """
    try:
        all_files = glob.glob(os.path.join(file_location, f"*.{file_type}"))
        filtered_files = []
        for file_path in all_files:
           if os.path.islink(file_path):
              print(f"⚠️ Skipping symlink {file_path}")
              continue
           if not os.path.isfile(file_path):
              print(f"⚠️ Skipping non file {file_path}")
              continue

           filtered_files.append(file_path)

        files = sorted(
            filtered_files,
            key=os.path.getmtime if sort_by == 'date' else str
        )
        return files
    except Exception as e:
        print(f"❌ Error finding files: {e}")
        return []

def upload_files(hfuser, hfrepo, file_location, file_type, commit_message, create_pr, repo_type, repo_folder):
    """Uploads selected files to the Hugging Face repository."""
    if not hfuser or not hfrepo:
        print("❗ Please enter both your Organization/Username and Repository name.")
        return
    if not file_location:
        print("❌ No directory was selected!")
        return

    files = find_files(file_location, file_type)
    if not files:
      print("📝 No files found matching your criteria. Check your file type and ensure files are in the location specified.")
      return

    api = HfApi()
    repo_id = f"{hfuser}/{hfrepo}"
    print(f"🎯 Preparing to upload to: huggingface.co/{repo_id}")

    total_files = len(files)
    print(f"\n🚀 Starting upload of {total_files} file(s)...")
    # Create a progress bar for the overall upload
    with tqdm(total=total_files, desc="Total Progress", unit="file") as pbar:
        for idx, file in enumerate(files, 1):
            size = os.path.getsize(file)
            print(f"\n📦 Uploading file {idx}/{total_files}: {file} ({format_size(size)})")
            try:
                start_time = time.time()

                # Handle folders
                path_in_repo = os.path.basename(file)
                 # Split the path
                path_parts = Path(file).parts
                if len(path_parts) > 1:
                  # Get only the folder names
                    folder_path_parts = path_parts[len(Path(file_location).parts):-1]
                  # Generate the folder path in the repo
                    if folder_path_parts:
                       path_in_repo = os.path.join(*folder_path_parts, os.path.basename(file))
                
                #Add the subfolder to the path
                if repo_folder:
                   path_in_repo = os.path.join(repo_folder, path_in_repo)


                response = api.upload_file(
                  path_or_fileobj=file,
                  path_in_repo=path_in_repo,
                  repo_id=repo_id,
                  repo_type=repo_type,
                  create_pr=create_pr,
                  commit_message=commit_message
                )
                duration = time.time() - start_time
                print(f"✅ Upload completed in {duration:.1f} seconds")
            except Exception as e:
              print(f"❌ Error uploading {file}: {e}")

            pbar.update(1)

    print("\n✨ All uploads complete!")
    if create_pr:
        print("🎉 Check your repository for the new Pull Request!")
    else:
        print("🎉 Files uploaded directly to your repository!")


if __name__ == "__main__":
    print("🌟 Hugging Face File Uploader - Standalone 🌟")

    parser = argparse.ArgumentParser(description="Upload files to the Hugging Face Hub.")
    parser.add_argument("hfuser", type=str, help="Hugging Face Username/Organization")
    parser.add_argument("hfrepo", type=str, help="Hugging Face Repository Name")
    parser.add_argument("file_type", type=str, help="File type to upload (e.g., safetensors, txt, mp3).")
    parser.add_argument("file_location", type=str, help="Path to the directory to search for files.")
    parser.add_argument("--commit_message", type=str, default="Uploaded with Earth & Dusk Huggingface 🤗 Backup", help="Commit message (optional).")
    parser.add_argument("--create_pr", action="store_true", help="Create a pull request (optional).")
    parser.add_argument("--repo_type", type=str, default="model", help="Repository type (model, dataset, space).")
    parser.add_argument("--repo_folder", type=str, default="", help="Optional folder inside the repo to upload to.")
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
    )
