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
