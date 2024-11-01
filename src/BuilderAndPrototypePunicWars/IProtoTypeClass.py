from abc import ABC, abstractmethod

class IProtoType(ABC):
    
    @staticmethod
    @abstractmethod
    def clone():
        pass