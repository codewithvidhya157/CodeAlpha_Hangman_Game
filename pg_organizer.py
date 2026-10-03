import os
import shutil

# Folder containing the files
source_folder = "photos"

# New folder for JPG files
destination_folder = os.path.join(source_folder, "JPG_Files")

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Check all files in the source folder
for file in os.listdir(source_folder):

    # Check if the file is a JPG file
    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print("Moved:", file)

print("\nAll JPG files have been moved successfully!")