# Instance and class attributes
class Employee: 
    company = "ACER"
    def __init__(self, salary,name, bond, company):
        self.salary = salary
        self.name =  name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.Salary is {self.salary}. THe bond is for {self.bond} years")
    
e1 = Employee(100000, "Ghost Rider", 4,"Lenevo")
print(e1.company)
print(Employee.company)


#Object Introspection
# print(dir(e1))