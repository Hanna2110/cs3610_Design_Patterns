from PersonModule import Person

class Instructor(Person):
    def __init__(self, id, name, address, department="None", salary=0):
        super().__init__(id, name,address)
        self.department=department
        self.salary=salary
        
    
    def __lt__(self, other):
        print(f"{other.name} > {self.name}")
        return self.salary < other.salary

    def __gt__(self, other):
        print(f"{other.name} < {self.name}")
        return self.salary > other.salary
        
    def greeting(self):
        print("Hi from ",self.name)
     