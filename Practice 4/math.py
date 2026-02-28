import math
import random






print("--- Built-in Math ---")
print("min(5, 10, 25):", min(5, 10, 25))
print("max(5, 10, 25):", max(5, 10, 25))
print("abs(-7.25):", abs(-7.25))
print("round(5.76543, 2):", round(5.76543, 2))
print("pow(4, 3):", pow(4, 3))






print("\n--- math Module ---")
print("math.sqrt(64):", math.sqrt(64))
print("math.ceil(1.4):", math.ceil(1.4))
print("math.floor(1.4):", math.floor(1.4))
print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.sin(math.pi/2):", math.sin(math.pi / 2))
print("math.cos(0):", math.cos(0))






print("\n--- random Module ---")
print("random.random():", random.random())
print("random.randint(1, 10):", random.randint(1, 10))

fruits = ["apple", "banana", "cherry", "date"]
print("random.choice(fruits):", random.choice(fruits))

random.shuffle(fruits)
print("random.shuffle(fruits):", fruits)