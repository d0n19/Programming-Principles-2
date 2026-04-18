with open("sample_data.txt", "w", encoding="utf-8") as file:
    file.write("first data line.\n")
    file.write("second data line.\n")
print("File sample_data.txt has been created and fullfilled.")




with open("sample_data.txt", "a", encoding="utf-8") as file:
    file.write("Third line, added by 'a' (append).\n")
print("New lines had been created successfully.")