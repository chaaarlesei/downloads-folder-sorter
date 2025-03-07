# Sort Downloads Script

This Python script automatically organizes files in your **Downloads** folder by moving them into categorized subfolders based on file types.

## How It Works
1. **Scans the Downloads folder** for files.
2. **Creates categorized folders** (if they don’t already exist), such as:
   - `Apps` (for `.exe`, `.msi`, etc.)
   - `Documents` (for `.pdf`, `.docx`, etc.)
   - `Images` (for `.jpg`, `.png`, etc.)
   - `Videos`, `Music`, `Compressed`, `Code`, `Torrents`, etc.
3. **Moves files** into the appropriate folders based on their extensions.
4. **Unrecognized files** go into an `Others` folder.

## Installation
1. **Install Python** (if not already installed):  
   Download and install Python from [python.org](https://www.python.org/). Ensure Python is added to your system **PATH**.

2. **Download the Script**  
   Save the following `sort_downloads.py` script to your computer.

## Python Script
```python
import os
import shutil

# Change this to your actual Downloads folder path
DOWNLOADS_PATH = os.path.expanduser("~\\Downloads")

# Define categories and their corresponding file extensions
FILE_CATEGORIES = {
    "Apps": [".exe", ".msi", ".apk", ".dmg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh", ".php"],
    "Torrents": [".torrent"],
    "Others": []  # Unrecognized files go here
}

def create_folders():
    """Create category folders in Downloads if they don't exist."""
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(DOWNLOADS_PATH, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    """Move files into their respective category folders."""
    for filename in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Determine the target folder
        target_folder = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                target_folder = category
                break

        # Move file to the appropriate folder
        destination_path = os.path.join(DOWNLOADS_PATH, target_folder, filename)
        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} → {target_folder}")

if __name__ == "__main__":
    create_folders()
    move_files()
    print("Downloads folder sorted successfully!")
```

## Usage
### Run the Script (Windows)
#### **Using Command Prompt**
1. Open Command Prompt (`Win + R`, type `cmd`, hit Enter).
2. Navigate to where the script is saved, e.g., if it's on Desktop:
   ```cmd
   cd Desktop
   ```
3. Run the script:
   ```cmd
   python sort_downloads.py
   ```

#### **Using PowerShell**
1. Open PowerShell.
2. Navigate to the script’s location:
   ```powershell
   cd ~/Desktop
   ```
3. Run the script:
   ```powershell
   python .\sort_downloads.py
   ```

## Customization
You can edit the `FILE_CATEGORIES` dictionary in the script to add or modify file extensions.

## Automating the Script
To run the script automatically, you can **schedule it with Task Scheduler**:
1. Open Windows Task Scheduler.
2. Create a new task.
3. Set the **Trigger** to run the script daily or on login.
4. Set the **Action** to run `python.exe` with the path to the script.

## License
This script is **free to use and modify**.

## Contributions
Feel free to contribute by adding new features or improvements!

---
**Happy Organizing!**

