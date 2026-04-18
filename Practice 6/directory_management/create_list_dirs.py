import os

new_dir_path = "test_folder/sub_folder"
os.makedirs(new_dir_path, exist_ok=True) 
print(f"Folders are created: {new_dir_path}")


current_dir = os.getcwd()
print(f"Located in: {current_dir}")


print("Folder's content:")
items = os.listdir(".")
for item in items:
    print(" -", item)