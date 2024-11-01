from BuilderPunicWars.IBuilderClass import IBuilber
from BuilderPunicWars.ArmyClass import Army
from BuilderPunicWars.WarriorArcherClass import WarriorArcher
from BuilderPunicWars.WarriorHorsemanClass import WarriorHorseman
from BuilderPunicWars.CombatUnit_ElephantClass import CombatUnit_Elephant

class CarthaginianArmyBuilder(IBuilber):
    
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self.__product = Army("Carthaginian Army")
        
    @property
    def product(self) -> None:#getResult method --> Army
        currentProduct=self.__product
        self.reset()#ready to start producing another product
        return currentProduct

    def buildArcher(self) -> None:
        self.product.add(WarriorArcher())

    def buildHorseman(self) -> None:
        self.product.add(WarriorHorseman())

    def buildElephant(self) -> None:
        self.product.add(CombatUnit_Elephant())

