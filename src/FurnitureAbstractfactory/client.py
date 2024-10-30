from FurnitureAbstractfactory.FurnitureFactoryClass import FurnitureFactory

def getHannaFurniture():
    print("!!!!")
    hannaFurniture=[]
    hannaWishes=['SmallChair','BigTable','MediumTable']
    
    for dream in hannaWishes:
        if FurnitureFactory.get_furniture(dream)!=None:
            hannaFurniture.append(FurnitureFactory.get_furniture(dream))
            
    for furniture in hannaFurniture:
        print(f"Hanna's furniture incluse the {furniture.__class__} with {furniture.get_dimensions()}")
