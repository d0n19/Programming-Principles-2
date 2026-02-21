numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda s: s.upper(), words))

print(squared_numbers)
print(upper_words)