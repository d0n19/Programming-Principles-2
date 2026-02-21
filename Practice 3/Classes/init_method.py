class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)