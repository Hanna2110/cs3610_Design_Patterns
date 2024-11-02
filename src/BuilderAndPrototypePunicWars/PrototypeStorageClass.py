from BuilderAndPrototypePunicWars.WarriorArcherClass import WarriorArcher
from BuilderAndPrototypePunicWars.WarriorHorsemanClass import WarriorHorseman

class PrototypeRegistry:
    # Cache to store objects/prototypes
    prototypes = {}
    
    @staticmethod
    def add_prototype(name, prototype):
        PrototypeRegistry.prototypes[name] = prototype
    
    @staticmethod
    def get_prototype(name):
        if name in PrototypeRegistry.prototypes:
            return PrototypeRegistry.prototypes[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found.")
        
    @staticmethod
    def initialize():
        #load Archer
        warrior1=WarriorArcher()
        PrototypeRegistry.prototypes.setdefault(WarriorArcher.__name__, warrior1)    
        
        #load Horseman
        warrior2=WarriorHorseman()
        PrototypeRegistry.prototypes.setdefault(WarriorHorseman.__name__, warrior2)     
       
        
        
        
        