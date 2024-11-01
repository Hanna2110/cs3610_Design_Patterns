#from abc import ABC, abstractmethod
'''
class IWarrior(ABC):
    @staticmethod
    @abstractmethod
    def info()-> None: 
        pass
'''

from BuilderAndPrototypePunicWars.IProtoTypeClass import IProtoType
from abc import abstractmethod

class IWarrior(IProtoType):
    @staticmethod
    @abstractmethod
    def info()-> None: 
        pass