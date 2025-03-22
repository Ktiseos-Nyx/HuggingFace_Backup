# 🚀 Hugging Face Uploader: Streamline Your Model Sharing! 🚀

[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-xl-dark.svg)](https://huggingface.co/Duskfallcrew/Huggingface_Backup) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/duskfallcrew/HuggingFace_Backup)

This tool provides a user-friendly way to upload files directly to your Hugging Face repositories using a Jupyter Notebook. Designed to streamline your workflow, it makes sharing your models, datasets, and spaces easier than ever!

We are actively working on further development and security enhancements for the Jupyter Notebook edition.

We are also actively struggling to update and keep track of the Google Colab version.

> 2025 'EXTRA' is the version with the extra cell to zip up images or files before uploading to huggingface.  March 2025 has minor adjustments to environment code.
> Dataset Zipper is a standalone zip & download function notebook, which it's  cell is in the 'extra' notebook as well.

---

## 📝 Table of Contents

*   [Key Features](#key-features)
*   [Jupyter Notebook Edition: Interactive and User-Friendly](#-jupyter-notebook-edition-interactive-and-user-friendly)
    *   [One-Time Setup for Jupyter Users](#one-time-setup-for-jupyter-users)
    *   [Using the Uploader Widget in the Jupyter Notebook](#️-using-the-uploader-widget-in-the-jupyter-notebook)
    *   [Important Notes for Jupyter Users](#💡-important-notes-for-jupyter-users)
*   [Updates & Community](#-updates--community)
*   [About Us](#-about-us)
*   [Let's Connect!](#-lets-connect)
*   [Support Our Adventures](#-support-our-adventures)
*   [Proudly Supported By](#-proudly-supported-by)
*   [Need Help?](#️-need-help)
*   [Credits & Origins](#-credits--origins)
*   [Changelog: Our Journey So Far](#-changelog-our-journey-so-far)

---

## Key Features

| Feature                       | Badge/Link                                                                                                                                                                                                                                                            | Description                                                                                               |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Coded With Help From**      | [![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)](https://gemini.google.com/)                                                                                                | Acknowledgment of AI assistance in development.                                                          |
| **Language**                  | [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)                                                                                                                                | Developed primarily in Python.                                                                         |
| **Hugging Face Repository**   | [![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-xl-dark.svg)](https://huggingface.co/Duskfallcrew/Huggingface_Backup)                                                                                                | Link to the Hugging Face repository for the tool.                                                          |
| **GitHub Repository**         | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/duskfallcrew/HuggingFace_Backup)                                                                                                | Link to the GitHub repository for the tool. Always check here for the latest updates.                      |
| **Open in Google Colab**      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ktiseos-Nyx/HuggingFace_Backup/blob/main/HuggingFace_Backup_2024_Colab.ipynb)                                                              | Directly open and run the Jupyter Notebook in Google Colab.                                                |

---

## 💻 Jupyter Notebook Edition: Interactive and User-Friendly

For an interactive and visually intuitive experience, use our Jupyter Notebook edition. 


<br/>

### One-Time Setup for Jupyter Users

1.  **How To Get Your Huggingface API Token:**

    *   Navigate to your [Hugging Face settings page](https://huggingface.co/settings/tokens).
    *   Click "New token."
    *   Provide a descriptive name for your token (e.g., "Uploader Token").
    *   Select the appropriate role and permissions. For uploading files, ensure it has "write" permissions.
    *   Click "Generate token."
    *   **Securely copy the generated API token.** This token is essential for authentication and will only be displayed once. If lost, you will need to generate a new one.

2.  **Authentication:**  After generating your API token, execute the `notebook_login()` cell *once* at the beginning of the notebook. This securely stores your Hugging Face API token for the session.

    *   **Important Security Note:** To maintain the security of your API token, avoid sharing the notebook file or system state after running `notebook_login()`. **Do not commit the notebook to public repositories**, especially if using platforms like Google Colab. If you suspect your token has been compromised, generate a new one immediately.

### 🗂️ Using the Uploader Widget in the Jupyter Notebook

1.  **Repository Details:**
    *   **Owner:** Enter your Hugging Face Organization or Username. This is the name found in your repository URL.
    *   **Repo:** Enter the name of the repository you wish to upload to.
        *   Ensure both "Owner" and "Repo" names are accurate to prevent upload failures.
    *   **Repo Type:** Select the repository type from the dropdown menu: "model," "dataset," or "space."
    *   **Subfolder:** (Optional) To upload files to a specific subfolder within your repository, enter the subfolder name. If left blank, files will be uploaded to the repository root.

2.  **Directory Selection:**
    *   **Path:** Enter the full path to the local directory containing the files you want to upload.
    *   **Update Dir:** Click '🔄 Update Dir' to set the path and refresh the file list based on the selected file type.
        *   If no files appear, verify that the path and selected file type are correct.

3.  **File Selection:**
    *   **File Type:** Choose the appropriate file type from the dropdown (e.g., `safetensors`, `png`, `txt`). This will display all files of that type within the specified directory.
    *   **File List:** Select the files for upload from the displayed list. Use the "Sort By" dropdown to organize files by name or modification date.

4.  **Commit Message:**
    *   **(Optional):** Add a specific message for the commit in the "Message" field. If left empty, a default message "Uploaded with Earth & Dusk Huggingface 🤗 Backup" will be used.

5.  **Upload Options:**
    *   **Create Pull Request:** Check this box to upload changes as a pull request. Unchecked, changes are directly committed to the main branch.
    *   **Clear output after upload:** Select this option to clear the output area after a successful upload.

6.  **Start Upload:**
    *   Click '⬆️ Upload' to begin the upload process.
    *   The current file being uploaded and the upload progress percentage will be displayed.

### 💡 Important Notes for Jupyter Users

*   **Direct Uploads:** This tool utilizes the Hugging Face API for direct file uploads, bypassing Git operations for core functionality. Command-line Git usage is not required for basic uploads.
*   **Git LFS:** Git LFS is not necessary for using this tool.  Separate Git credentials are required for repository operations outside of this notebook (like cloning or pushing via Git) and should not be stored within the notebook.
*   **Subfolders:** The tool will create subfolders in your repository based on your local file structure or the specified "Subfolder."
*   **Troubleshooting:** If you encounter issues, re-verify all steps, ensure you have write access to the repository, and that your API token has the correct permissions. Double-check file paths and file types.

<br/>

## 📣 Updates & Community

*   This tool is continuously updated and improved.
*   For the latest updates, fixes, and community contributions, please visit the [GitHub repository](https://github.com/duskfallcrew/HuggingFace_Backup).

We hope this tool simplifies your Hugging Face uploads! For questions or suggestions, please reach out.

<br/>

## 🌈 About Us

We are a diverse system of 300+ alters, navigating life with DID, ADHD, Autism, and CPTSD. We believe in the positive potential of AI for mental health and creativity and are excited to explore this intersection.

This project is managed by **Ktiseos Nyx**, the programming division of Earth & Dusk.

<br/>

### 🤝 Let's Connect!

| Platform          | Link                                        |
| :---------------- | :------------------------------------------ |
| **Website**       | [End Media](https://www.end-media.org/)      |
| **Discord**       | [Discord Community](https://discord.gg/5t2kYxt7An) |
| **Hugging Face**  | [HuggingFace Space](https://huggingface.co/EarthnDusk) |
| **YouTube**       | [YouTube Channel](https://www.youtube.com/channel/UCk7MGP7nrJz5awBSP75xmVw) |
| **DeviantArt**    | [DeviantArt Group](https://www.deviantart.com/diffusionai) |
| **Subreddit**     | [Subreddit](https://www.reddit.com/r/earthndusk/)    |

<br/>

### ☕ Support Our Adventures

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z8L4EO)

You can support our work and future development through Ko-fi.

<br/>

## 🏴‍☠️ Proudly Supported By

*   [Pirate Diffusion](https://www.piratediffusion.com/)
*   [Yodayo](https://yodayo.com/)

<br/>

## 🛠️ Need Help?

If you encounter a bug or need assistance, please reach out through:

*   GitHub Pull Requests & Bug Tracker
*   CivitAi Direct Messages/Comments
*   Earth & Dusk Discord

<br/>

## 💝 Credits & Origins

We extend our sincere gratitude to the original creators and contributors who laid the foundation for this project:

*   EVERYDREAM2 TRAINER: [https://github.com/victorchall/EveryDream2trainer](https://github.com/victorchall/EveryDream2trainer)
*   LINAQRUF
*   NOCRYPT: [![](https://dcbadge.vercel.app/api/shield/442099748669751297?style=flat)](https://lookup.guru/442099748669751297)

Explore the original Stable Diffusion Colab notebook:

[Open Original SD Colab](https://colab.research.google.com/drive/1wEa-tS10h4LlDykd87TF5zzpXIIQoCmq)
<br/>

## 📝 Changelog: Our Journey So Far

1.  **🔧 Enhanced with EveryDream2Trainer's Python widget integration.**
2.  **🌟 Maintained and highlighted Nocrypt's valuable contributions.**
3.  **📦 Integrated essential functionalities into a single Jupyter Notebook.**
4.  **🤓 Improved file handling with proper file extensions (*.safetensors).**
5.  **📝 Created user-friendly and accessible instructions.**
6.  **🤖 Utilized GPT assistance to enhance clarity and readability.**
7.  **🎨 Improved the visual presentation of the Jupyter Notebook edition.**
8.  **🔄 Synchronized Colab and Jupyter Notebook versions for consistency.**
9.  **🧹 Optimized dependencies by removing unnecessary transformers.**
10. **✨ Added advanced folder upload capabilities.**
11. **🔄 Refined and updated the Colab notebook for improved performance.**
12. **🚀 Implemented more concise widget features and restored Colab functionality.**
13. **💎 Underwent a Gemini-assisted overhaul for improved quality.**
14. **➕ Expanded supported file types in Colab, streamlined instructions, and introduced command-line functionality (Note: Command-line section removed as per request).**

We acknowledge that we are not professional programmers, and appreciate community contributions. Pull requests are always welcome for improvements! 🎉
