
# 🚀 Hugging Face Uploader: Streamline Your Model Sharing! 🚀

This tool provides a user-friendly way to upload files directly to your Hugging Face repositories. Whether you prefer the interactive environment of a Jupyter Notebook or the command-line efficiency of a Python script, we've got you covered. We've designed it to streamline your workflow and make sharing your models, datasets, and spaces easier than ever before!

CodeQL only works with direct Python, and we've recently linted and are working on re-securing and redeveloping the notebooks. They ARE 100% secure overall, we're just -- not able to get the code passings for Jupyter done quite yet.

------

**🔑 Quick Access Badges**

Coded With Help From:

[![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)](https://gemini.google.com/)

Languages:

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

Hugging Face Option:

[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-xl-dark.svg)](https://huggingface.co/Duskfallcrew/Huggingface_Backup)

Always check Github updates:

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/duskfallcrew/HuggingFace_Backup)

------

## 💻 Jupyter Notebook Edition: Interactive and User-Friendly

For an interactive, visual, and user-friendly experience, use our Jupyter Notebook edition! You can open it directly in Google Colab with this button:

<a target="_blank" href="https://colab.research.google.com/github/Ktiseos-Nyx/HuggingFace_Backup/blob/main/HuggingFace_Backup_2024_Colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<br/>

**🔑 One-Time Setup for Jupyter Users**

1.  **How To Get Your Huggingface API Token:**

    *   Go to the [Hugging Face settings page](https://huggingface.co/settings/tokens).
    *   Click on "New token."
    *   Give your token a descriptive name (e.g., "My Uploader Token").
    *   Select the appropriate role/permissions for your token. If you plan to upload files, it must have "write" permissions.
    *   Click "Generate token."
    *   **Copy the generated API token to a safe place.** You will need it to authenticate, and it will only be shown to you once. If you lose it, you must generate a new token.

2.  **Authentication:** After you have generated an API token, run the `notebook_login()` cell *once* at the start of the notebook to securely store your Hugging Face API token.
    *   **Important Security Note:** For security, avoid sharing your notebook file or system state after you have run `notebook_login()`. Do not commit your notebook file to a shared repository, as this could expose your API token. This is particularly important if you are sharing a notebook file, or using an online system such as Google Colab, or similar. It is recommended that you generate a new token if you suspect your token has been exposed.

**🗂️ Using the Uploader Widget in the Jupyter Notebook**

1.  **Repository Details:**
    *   **Owner:** Enter your Hugging Face Organization or Username in the "Owner" field. This is the name that appears in the URL of your repository.
    *   **Repo:** Enter your repository name in the "Repo" field. This is the name of the repository you want to upload to.
        *  Make sure these names are correct, or the tool will fail to upload.
    * **Repo Type:** Select the type of repository from the "Repo Type" dropdown. Your options are "model", "dataset", and "space".
    * **Subfolder:** *(Optional)* If you want to upload your files to a specific pre-existing subfolder within your repository, enter the folder name in the "Subfolder" field. Otherwise, files will be uploaded directly to the root.

2.  **Directory Selection:**
    *   **Path:** Enter the full path to the directory on your local machine where your files are located into the "Path" field.
    *   **Update Dir:** Click the '🔄 Update Dir' button to set that path and refresh the list of files in the file selector. This will update the list of files based on the selected file type.
    *  If no files appear after selecting "Update Dir", make sure the path is correct, and the file type is correct.

3.  **File Selection:**
    *   **File Type:** Select the appropriate file type from the dropdown menu (e.g., `safetensors`, `png`, `txt`). This will show all the files of that type within the directory you selected above.
    *   **File List:** Choose the files you want to upload from the list of files. You can sort the list by name or date modified using the "Sort By" dropdown.

4.  **Commit Message:**
    *   **(Optional)**: If you would like to add a specific message to the commit, enter that in the "Message" field. If you leave this field blank the default message will be used instead: "Uploaded with Earth & Dusk Huggingface 🤗 Backup".

5.  **Upload Options:**
    *   **Create Pull Request:** Select the "Create Pull Request" checkbox to upload the changes as a pull request. If this box is left unchecked the changes will be uploaded directly to your repo (main branch).
    *  **Clear output after upload:** Select this box if you would like the output area to be cleared after a successful upload.

6.  **Start Upload:**
    *   Click the '⬆️ Upload' button to begin the upload process.
    * The current uploading file will be shown below the progress bar.
    * A progress percentage will be displayed below this.

**💡 Important Notes for Jupyter Users**

*   **Direct Uploads:** This uploader uses the Hugging Face API for direct file uploads, bypassing traditional Git operations for core functionality. Therefore, you won't need to use command line Git.
*   **Git LFS:** You do not need to use Git LFS for this tool to function. If you need to clone or push changes to a repository *outside this notebook*, it requires a separate Git credential setup, this credential is separate from your API token and should not be stored in the notebook.
*   **Subfolders**: The tool will create subfolders in your repo based on the folder structure of your files when you upload them, or the folder you specified in the "Subfolder" field.
*   **Troubleshooting:** If you encounter any issues, please review the steps, double-check that you have write access to the repository, and that your API token has the correct scope of access. Make sure that the file path and file types are correct.

<br/>

## 🐍 Python Script Edition: Command-Line Power

For those who prefer a command-line interface, we've provided a versatile Python script.

**🔑 Initial Setup for Python Script Users**

1.  **How To Get Your Huggingface API Token:**
        * Go to the [Hugging Face settings page](https://huggingface.co/settings/tokens).
        * Click on "New token."
        * Give your token a descriptive name (e.g., "My Uploader Token").
        * Select the appropriate role/permissions for your token. If you plan to upload files, it must have "write" permissions.
        * Click "Generate token."
        * **Copy the generated API token to a safe place.** You will need it to authenticate, and it will only be shown to you once. If you lose it, you must generate a new token.

2.  **Set the `HF_TOKEN` Environment Variable:** After you have generated an API token, you will need to set it to an environment variable. This is how the script authenticates.
   * This environment variable will only last for the session you have it set. For a more permenant solution see the notes below.
    *   **Linux/macOS:** Open your terminal and run this command, replacing `<YOUR_API_TOKEN>` with your actual API token:
        ```bash
        export HF_TOKEN=<YOUR_API_TOKEN>
        ```
    *   **Windows (Command Prompt):** Run this command:
        ```cmd
        set HF_TOKEN=<YOUR_API_TOKEN>
        ```
    *   **Windows (PowerShell):** Run this command:
        ```powershell
        $env:HF_TOKEN = "<YOUR_API_TOKEN>"
        ```
    *   **Note:** Setting environment variables this way only works for the current session. For longer-term use, you may want to use a `.env` file or add it to your shell configuration file (such as `.bashrc`, `.zshrc`, or similar) so you don't need to set it each time you use the script.
    *   Setting it to a `.env` file might be useful. See the python dotenv library for more information on this.

3.  **Run the Python script:** After setting the `HF_TOKEN` environment variable, you can now run the Python script. It assumes that the environment variable is set up, and will fail if it is not.
     ```bash
    python huggingface_uploader.py <hfuser> <hfrepo> <file_type> <file_location> --commit_message "<your message>" --create_pr --repo_type <repo_type> --repo_folder <repo_folder>
    ```
     * Please note: This tool is for direct uploading of files via the Hugging Face Hub API. It doesn't perform operations that require traditional Git interactions. You do not need Git to use the uploader, you only need the API token.
     * **Replace Placeholders**: Replace the placeholders in angle brackets (`<>`) with the correct values:
        * `<hfuser>`: your Hugging Face Username or Organization name
        * `<hfrepo>`: the name of your Hugging Face Repository
        * `<file_type>`: the file type to upload (e.g., `safetensors`, `txt`, `mp3`).
        * `<file_location>`: the full path to the directory to search for files on your machine.
        * `--commit_message`: (Optional) Your commit message. If not specified, will use "Uploaded with Earth & Dusk Huggingface 🤗 Backup".
        *  `--create_pr`: (Optional) When present, a pull request will be generated. If not included the files will be directly uploaded to your repo.
        * `--repo_type`: (Optional) The repo type (model, dataset, space). If not specified defaults to "model".
        * `--repo_folder`: (Optional) The subfolder to upload to. If not specified, will upload to the root of the repo.

<br/>

## 📣 Updates & Community

*   This tool will continue to be updated.
*   For the latest patches, fixes, and community contributions, visit [https://github.com/duskfallcrew/HuggingFace_Backup](https://github.com/duskfallcrew/HuggingFace_Backup)

We hope this tool makes your Hugging Face uploads easier! If you have any questions or suggestions, please reach out.

<br/>

## 🌈 About Us

Heya! We're a vibrant system of 300+ alters, proudly rocking life with DID, ADHD, Autism, and CPTSD. We believe AI can be a game-changer for mental health and creativity, and we're here to explore that potential together!
This project is handled by **Ktiseos Nyx**, the programming arm of Earth & Dusk.

<br/>

### 🤝 Let's Connect!

*   🏠 [End Media](https://www.end-media.org/)
*   🎮 [Discord Community](https://discord.gg/5t2kYxt7An)
*   🤗 [HuggingFace Space](https://huggingface.co/EarthnDusk)
*   🎵 [YouTube](https://www.youtube.com/channel/UCk7MGP7nrJz5awBSP75xmVw)
*   🎨 [DeviantArt Group](https://www.deviantart.com/diffusionai)
*   🎪 [Subreddit](https://www.reddit.com/r/earthndusk/)

<br/>

### ☕ Support Our Adventures

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z8L4EO)

<br/>

## 🏴‍☠️ Proudly Supported By

*   [Pirate Diffusion](https://www.piratediffusion.com/)
*   [Yodayo](https://yodayo.com/)

<br/>

## 🛠️ Need Help?

Found a bug? We've got multiple ways to help:

*   GitHub PR & Bug tracker
*   CivitAi DM/comments
*   Earth & Dusk Discord

<br/>

## 💝 Credits & Origins

Big thanks to our code ancestors:

*   EVERYDREAM2 TRAINER [https://github.com/victorchall/EveryDream2trainer](https://github.com/victorchall/EveryDream2trainer)
*   LINAQRUF
*   NOCRYPT [![](https://dcbadge.vercel.app/api/shield/442099748669751297?style=flat)](https://lookup.guru/442099748669751297)

Try the original SD Colab:

<a target="_blank" href="https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq">
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<br/>

## 📝 Changelog: Our Journey So Far

1.  🔧 Added EveryDream2Trainer's Python widget magic
2.  🌟 Kept Nocrypt's awesome contributions front and center
3.  📦 Packed all the essentials into one Jupyter notebook
4.  🤓 Made friends with proper file extensions (*.safetensors)
5.  📝 Wrote instructions in human-friendly language
6.  🤖 Got GPT to help make things clearer
7.  🎨 Prettied up the Jupyter edition
8.  🔄 Synced up Colab and Jupyter versions
9.  🧹 Cleaned up dependencies (bye-bye, unnecessary transformers!)
10. ✨ Added some extra folder upload superpowers
11. Cleaned up Colab & Updated Colab
12. Added more concise features to the widgets - Colab is working again.
13. Gemini overhaul
14. Added more file types to Colab, streamlined the instructions, and added command-line functionality.

Remember: We're not pro programmers, and that's totally okay! If you see something that could be better, pull requests are always welcome! 🎉
