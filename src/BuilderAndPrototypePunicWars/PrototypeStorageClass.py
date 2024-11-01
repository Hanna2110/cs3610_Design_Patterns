from BuilderAndPrototypePunicWars.WarriorArcherClass import WarriorArcher

class PrototypeRegistry:
    # Cache to store objects/prototypes
    prototypes = {}
    
    @staticmethod
    def add_prototype(name, prototype):
        PrototypeRegistry.prototypes[name] = prototype
    
    @staticmethod
    def get_prototype( name):
        if name in PrototypeRegistry.prototypes:
            return PrototypeRegistry.prototypes[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found.")
        
    @staticmethod
    def initialize():
        #load MyClass1
        warrior1=WarriorArcher()
        PrototypeRegistry.prototypes.setdefault(WarriorArcher.__name__, warrior1)        
       
        
        
        
        