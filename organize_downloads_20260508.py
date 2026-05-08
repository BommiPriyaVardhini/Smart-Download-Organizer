import os
import shutil
from datetime import datetime

# Path to Downloads folder
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

# File type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"]
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def clean_filename(filename):
    name, ext = os.path.splitext(filename)

    # Remove extra spaces and special characters
    cleaned = "".join(c if c.isalnum() or c in (" ", "_", "-") else "_" for c in name)
    cleaned = "_".join(cleaned.split())

    # Add current date
    date_str = datetime.now().strftime("%Y%m%d")

    return f"{cleaned}_{date_str}{ext}"

def organize_downloads():
    files = os.listdir(DOWNLOADS_PATH)

    for file in files:
        file_path = os.path.join(DOWNLOADS_PATH, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        name, extension = os.path.splitext(file)

        category = get_category(extension)

        category_folder = os.path.join(DOWNLOADS_PATH, category)

        # Create category folder if not exists
        os.makedirs(category_folder, exist_ok=True)

        new_filename = clean_filename(file)

        destination_path = os.path.join(category_folder, new_filename)

        # Handle duplicate filenames
        counter = 1
        base_name, ext = os.path.splitext(new_filename)

        while os.path.exists(destination_path):
            destination_path = os.path.join(
                category_folder,
                f"{base_name}_{counter}{ext}"
            )
            counter += 1

        shutil.move(file_path, destination_path)

        print(f"Moved: {file} -> {destination_path}")

if __name__ == "__main__":
    organize_downloads()
    print("\nDownloads folder organized successfully!")