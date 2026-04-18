import shutil
import os

source_file = "sample_data.txt"
backup_file = "sample_data_backup.txt"

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print(f"File was copied: {backup_file}")

if os.path.exists(backup_file):
    os.remove(backup_file)
    print(f"Backup file {backup_file} was deleted.")
else:
    print("File doesn't found for deleting.")