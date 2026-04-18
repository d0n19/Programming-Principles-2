names = ["Don", "Sam", "Leo"]
ages = [21, 30, 22]

for index, name in enumerate(names):
    print(f"Position {index}: Name {name}")

for name, age in zip(names, ages):
    print(f"{name} age {age} years old.")


string_num = "100"
converted_to_int = int(string_num)
print(f"Line '{string_num}' become number: {converted_to_int * 2}") 


print(f"\nThe oldest age: {max(ages)}")
print(f"The youngest age: {min(ages)}")
print(f"Sum of people: {len(names)}")
print(f"Names by alphabet: {sorted(names)}")