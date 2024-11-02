from typing import Type
from BuilderAndPrototypePunicWars.IBuilderClass import IBuilber
from BuilderAndPrototypePunicWars.CarthaginianArmyBuilderClass import CarthaginianArmyBuilder
from BuilderAndPrototypePunicWars.RomanArmyBuilderClass import RomanArmyBuilder

class ArmyDirector:
    def __init__(self) -> None:
        self.__builder = None

    @property
    def builder(self) -> IBuilber:
        return self.__builder

    @builder.setter
    def builder(self, builder: Type[IBuilber]) -> None:
        self.__builder=builder
        
    def makeArmy(self)-> None:
        if isinstance(self.builder, CarthaginianArmyBuilder):
            for i in range(5):
                self.builder.buildArcher()
            for i in range (3):
                self.builder.buildHorseman()
                
        if isinstance(self.builder, RomanArmyBuilder):
            for i in range(10):
                self.builder.buildArcher()
            for i in range (15):
                self.builder.buildHorseman()
        '''self.builder.buildInfantryman()
        self.builder.buildElephant()
        self.builder.buildCatapult()'''
        
        self.builder.product.showComponents()