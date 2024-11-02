from BuilderAndPrototypePunicWars.PrototypeStorageClass import PrototypeRegistry

from BuilderAndPrototypePunicWars.IBuilderClass import IBuilber
from BuilderAndPrototypePunicWars.ArmyClass import Army
from BuilderAndPrototypePunicWars.WarriorArcherClass import WarriorArcher
from BuilderAndPrototypePunicWars.WarriorHorsemanClass import WarriorHorseman


'''from BuilderAndPrototypePunicWars.WarriorInfantrymanClass import WarriorInfantryman
from BuilderAndPrototypePunicWars.WarriorHorsemanClass import WarriorHorseman
from BuilderAndPrototypePunicWars.CombatUnit_CatapultClass import CombatUnit_Catapult'''

class RomanArmyBuilder(IBuilber):
    
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self.__product = Army("Roman Army")
        
    @property
    def product(self) -> None:#getResult method --> Army
        currentProduct=self.__product
        self.reset()#ready to start producing another product
        return currentProduct

    def buildArcher(self) -> None:
        self.__product.add(PrototypeRegistry.get_prototype(WarriorArcher.__name__))

    def buildHorseman(self) -> None:
        self.__product.add(PrototypeRegistry.get_prototype(WarriorHorseman.__name__))

    def buildElephant(self) -> None:
        pass
        
    def buildInfantryman(self) -> None:
        pass
    
    def buildCatapult(self) -> None:
        pass

