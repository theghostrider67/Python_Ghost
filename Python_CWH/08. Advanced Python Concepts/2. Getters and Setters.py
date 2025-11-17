class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def first_name(self):
        l = self.name.split(" ")
        # print(l)
        return l[0]
    
    # def last_name(self):
    #     l = self.name.split(" ")
    #     print(l)
    #     return l[1]

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new__name = f"{first} {l[1]}"
        self.name = new__name
    
e = Employee("GHOST RIDER", 898989898)
# e.projects = 6
# print(e.projects)
# print(e.first_name())
#  print(e.last_name())
# e.set_first_name("TASIN")
# print(e.name)
print(e.first_name)
e.first_name = "ORKO"
print(e.name)