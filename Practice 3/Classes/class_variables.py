class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

emp1 = Employee("John")
emp2 = Employee("Sara")

print(emp1.name, emp1.company)
print(emp2.name, emp2.company)

Employee.company = "NewGlobal"
print(emp1.company)
print(emp2.company)