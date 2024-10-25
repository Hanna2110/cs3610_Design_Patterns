from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, id, name, address=None):
        self.id = id
        self.name = name
        self.address=address
    
    def __str__(self):
        return f"ID: {self.id }, Name: {self.name}"
    
        
    @abstractmethod
    def greeting(self):
        pass