from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def feed(self, food:str)->None:
        "Feed animal with food"
        
    @abstractmethod
    def bark(self)->None:
        "Barking"
     
    @property
    @abstractmethod
    def is_alive(self)->bool:
        "Check animal is alive or not"
        
        
class Sheep(Animal):
    
    def __init__(self):
        self.weight:int = 100
        self.sound:str = "mie~"
     
    def feed(self, food:str)->None:
        if food.lower() == "grass":
            self.weight += 10
        else:
            self.weight -= 10
        
    def bark(self):
        self.weight -= 5
        print(self.sound)
        
    @property
    def is_alive(self) -> bool:
        return self.weight > 0
    

class Tiger(Animal):
    
    def __init__(self):
        self.weight:int = 200
        self.sound:str = "Wow !!"
     
    def feed(self, food:str)->None:
        if food.lower() == "meat":
            self.weight += 10
        else:
            self.weight -= 10
        
    def bark(self):
        self.weight -= 5
        print(self.sound)
        
    @property
    def is_alive(self) -> bool:
        return self.weight > 0
          
         