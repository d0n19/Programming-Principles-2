import json
import os



json_string = '{"name": "Alice", "age": 28, "city": "London"}'
parsed_dict = json.loads(json_string)
print("Parsed JSON:", parsed_dict["name"], "is", parsed_dict["age"])







python_dict = {
    "title": "Python Developer",
    "skills": ["Python", "Git", "JSON"],
    "active": True
}
new_json_string = json.dumps(python_dict, indent=4)
print("\nPython to JSON string:\n", new_json_string)






with open("output.json", "w") as write_file:
    json.dump(python_dict, write_file, indent=4)
print("\nSuccessfully wrote to 'output.json'")








file_name = "sample-data.json"
if os.path.exists(file_name):
    with open(file_name, "r") as read_file:
        sample_data = json.load(read_file)
        print(f"\nSuccessfully read '{file_name}'!")
        print("Data loaded:", str(sample_data)[:100], "...")
else:
    print(f"\nFile '{file_name}' not found. Please ensure it is in the same folder.")