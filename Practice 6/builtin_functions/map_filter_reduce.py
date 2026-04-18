from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Initial list: {numbers}")


mapped_nums = list(map(lambda x: x * 2, numbers))
print(f"After map (multiplied to 2): {mapped_nums}")

filtered_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(f"After filter (only evens'): {filtered_nums}")


sum_reduced = reduce(lambda x, y: x + y, numbers)
print(f"After reduce (sum of all numbers): {sum_reduced}")