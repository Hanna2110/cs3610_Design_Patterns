from  BuilderAndPrototypePunicWars.IWarriorClass import IWarrior
from copy import deepcopy

class WarriorArcher(IWarrior):
    initID=0
    
    def __init__(self):
        self.__field = WarriorArcher.initID
        WarriorArcher.initID+=1
          

    def clone(self, memo=None): #This clone method uses a deep copy technique
        '''
        Memo is the dictionary that is used by the `deepcopy` library to prevent infinite recursive copies in
        instances of circular references. Pass it to all the `deepcopy` calls  you make in the `__deepcopy__` implementation to prevent infinite
        recursions
        '''
        if memo is None:
            memo = {}
            
        #copiedField=deepcopy(self.__field)
        #newSelf=self.__class__(copiedField)
        newSelf=self.__class__()
        newSelf.__dict__=deepcopy(self.__dict__, memo)
        return newSelf
     
    #@staticmethod
    def info(self)-> None: 
        print(f"I am an Archer-{self.__field}")
        