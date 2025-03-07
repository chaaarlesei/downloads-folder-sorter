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
   Save the `sort_downloads.py` script to your computer.

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
You can edit the script to add or modify file extensions and folder categories.

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

