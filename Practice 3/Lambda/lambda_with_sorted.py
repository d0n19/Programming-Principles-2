students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_by_age = sorted(students, key=lambda student: student[1])

points = [{"x": 2, "y": 10}, {"x": 5, "y": 2}, {"x": 1, "y": 5}]
sorted_by_y = sorted(points, key=lambda p: p["y"])

print(sorted_by_age)
print(sorted_by_y)