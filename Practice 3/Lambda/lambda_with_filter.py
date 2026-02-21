nums = [1, 5, 8, 10, 13, 16, 20]
even_nums = list(filter(lambda x: x % 2 == 0, nums))

names = ["Alice", "Bob", "Anna", "Alex", "John"]
a_names = list(filter(lambda name: name.startswith("A"), names))

print(even_nums)
print(a_names)