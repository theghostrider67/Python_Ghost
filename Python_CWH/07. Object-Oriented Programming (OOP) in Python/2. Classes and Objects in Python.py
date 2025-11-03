# Classes and Objects in Python
# Class: Class is a blueprint or a template. Form for an exam that contains name, age, electives, father's name, mother's name etc

# Object: Specific instance created from the template(class). Form which  contains the data for John Doe

class Employee:
    company = "ACER"

    def get_salary(self): #Self is important here because self is a way to reference the object of the class which is being created
        # print(self)
        return 34000
    

e1 = Employee() #An object of class Employee is created here
print(e1.get_salary())  #Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)