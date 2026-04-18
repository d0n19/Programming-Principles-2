import os
import shutil

with open("file_to_move.txt", "w") as f:
    f.write("Text to move")

source = "file_to_move.txt"
destination = "test_folder/file_to_move.txt"


if os.path.exists(source):
    shutil.move(source, destination)
    print(f"File moved to {destination}")