from BuilderAndPrototypePunicWars.ArmyDirectorClass import ArmyDirector
from BuilderAndPrototypePunicWars.CarthaginianArmyBuilderClass import CarthaginianArmyBuilder
from BuilderAndPrototypePunicWars.RomanArmyBuilderClass import RomanArmyBuilder
from BuilderAndPrototypePunicWars.PrototypeStorageClass import PrototypeRegistry

def PunicsWarsGame():
    PrototypeRegistry.initialize()
    gameDirector=ArmyDirector()
    
    romanBuilder = RomanArmyBuilder()
    gameDirector.builder=romanBuilder
    print("The Roman Army.")
    gameDirector.makeArmy()

    carthaginianBuilder=CarthaginianArmyBuilder()
    gameDirector.builder=carthaginianBuilder
    print("The Carthaginian Army.")
    gameDirector.makeArmy()
    