import random
from animals import Sheep, Tiger, Animal
from typing import Dict, List

ANIMAL_TYPES = [Sheep, Tiger]

class RoomNotFoundError(Exception):
    def __init__(self, number:int):
        self.number = number
        msg = f"The Room{self.number} is invalid."
        super().__init__(msg)

class Zoo:
    def __init__(self, total_room:int):
        self.total_room = total_room
        self.room:Dict[int,Animal] = {(i+1):random.choice(ANIMAL_TYPES)() for i in range(total_room)}
        
    def feed(self, room_number:int, food:str)->bool:
        animal = self.room.get(room_number, None)
        if animal is None:
            raise RoomNotFoundError(room_number) 
        animal.feed(food)
        return animal.is_alive

    @property
    def room_numbers(self)->List[int]:
        return list(iter(self.room.keys()))

    def check_room(self, room_number:int)->bool:
        animal = self.room.get(room_number, None)
        if animal is None:
            raise RoomNotFoundError(room_number) 
        animal.bark()
        return animal.is_alive
    