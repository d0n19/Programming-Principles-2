class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

    def greet(self, owner):
        return f"Hello {owner}, I am {self.name}"

my_dog = Dog("Rex")
print(my_dog.bark())
print(my_dog.greet("Admin"))