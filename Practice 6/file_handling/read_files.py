print("--- Full file reading (read) ---")
with open("sample_data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

print("--- Line by line reading (readlines) ---")
with open("sample_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        print(f"Line {index + 1}: {line.strip()}")