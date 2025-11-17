#Static  &  Class  Method
class Employee:
    company  = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

e1 = Employee("Jack", 90000)
e2 = Employee("Jonathan", 99999)
# print(Employee.company)
# print(Employee.name)
e1.print_info()
e2.print_info()