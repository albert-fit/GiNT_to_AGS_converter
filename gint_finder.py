import os
import shutil

# Define the source and destination folders
source_folder = 'data'
destination_folder = 'data_exports'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Traverse through all the folders and subfolders in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.gpj'):
            # Construct the source and destination paths
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file[:-4] + '.mdb')

            # Copy the file to the destination folder and change the extension
            shutil.copy2(source_path, destination_path)

print('Files copied successfully!')

