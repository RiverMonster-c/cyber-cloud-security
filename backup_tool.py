import os
import shutil
from datetime import datetime

# 1. Define what to backup and where to put it
source_folder = "./data_to_backup"
backup_destination = "./backups"

# Create the folders automatically if they don't exist yet
os.makedirs(source_folder, exist_ok=True)
os.makedirs(backup_destination, exist_ok=True)

# Create a test file inside the source folder so we have something to backup
with open(f"{source_folder}/import_file.txt", "w") as f:
    f.write("This is critical company data that must be backed up!")

# 2. Generate a timestamp filename (e.g., Burgers_20260601)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"{backup_destination}/Burgers_{timestamp}"

# 3. Zip the folder
print("⏳ Starting system backup...")
shutil.make_archive(backup_filename, 'zip', source_folder)
print(f"✅ Success! Created backup archive: {backup_filename}.zip")