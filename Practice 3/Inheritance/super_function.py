class Parent:
    def __init__(self, last_name):
        self.last_name = last_name

class Child(Parent):
    def __init__(self, first_name, last_name):
        super().__init__(last_name)
        self.first_name = first_name

kid = Child("Ivan", "Ivanov")
print(kid.first_name, kid.last_name)