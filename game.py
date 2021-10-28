import os
import sys
import math
import functools
from zoo import Zoo
from enum import Enum, auto
from typing import Callable, Optional, List



class GameState(Enum):
    START = auto()
    CHOOSE_ROOM =auto()
    ACTION = auto()
    VALIDATE = auto()
    ABORT = auto()


class ZooGame:
    def __init__(self):
        self.state:GameState = GameState.START
        self.zoo:Optional[Zoo] = None
        self.total_room:Optional[int] = None
        self.valid_room:List = []
        self.choosen_room:int = -1
    
    
    def start(self):
        if self.state == GameState.START:
            self.initiate_zoo()
            print("\n"+ "#" *40)

        if self.state == GameState.CHOOSE_ROOM:
            self.choose_room()
            print("\n"+ "#" *40)
        ret = False
        if self.state == GameState.ACTION:
            ret = self.choose_action()
            print("\n"+ "#" *40)

        if self.state == GameState.VALIDATE:
            if ret == False:
                print(f"The animal in Room{self.choosen_room} is dead. Game Over!!")
                self.abort()
            self.choosen_room = -1
            self.state = GameState.CHOOSE_ROOM
        return self.start()        
        

    def initiate_zoo(self) -> None:
        msg = ("Please enter the number of room to keep the animals (press q to abort)\n"
        + "(Interger > 0): ")
        while True:
            i = self.__convert_input_to_int(input(msg))
            if i == "q":
                self.abort()
            if (i is None) or not (i > 0):
                print("Number of room must be larger than 0")
                continue
            
            self.total_room = i
            self.zoo = Zoo(i)
            self.valid_room = self.zoo.room_numbers
            self.state = GameState.CHOOSE_ROOM
            break
        
    def abort(self):
        self.state = GameState.ABORT
        print("Quit the application")
        sys.exit(0)
        

    def choose_room(self)-> int:
        msg = ("Please enter the room number to check the animals (press q to abort the game)\n" + f"(1 - {self.total_room}): ")
        while True:
            i = self.__convert_input_to_int(input(msg))
            if i == "q":
                self.abort()            
            if i is None or i not in self.valid_room:                
                print(f"Invalid room_number {i}")
                continue
            self.choosen_room = i
            self.state = GameState.ACTION
            break
            
           
    def choose_action(self)-> bool:
        ACTION_DICT = {"q": self.abort,1: self.choose_food, 2: functools.partial(self.zoo.check_room, self.choosen_room)}

        msg = ("Please enter the action (press q to abort the game)\n"
        + "(1. Feed animal, 2. Knock door): ")
        while True:
            action_key = self.__convert_input_to_int(input(msg))
            if action_key not in ACTION_DICT:
                print(f"Invalid action number {action_key}")
                continue
            action:Callable = ACTION_DICT.get(action_key)
            ret = action()
            self.state = GameState.VALIDATE
            return ret


                
    def choose_food(self) -> bool:
        FOOD_DICT = {1:"meat", 2:"grass"}
        msg = ("Please choose the food to feed the animal (press q to abort the game)\n"
                + "(1. meat, 2. grass): ")
        while True:
            food = self.__convert_input_to_int(input(msg))
            if food == "q":
                self.abort()
            if food not in FOOD_DICT:
                print(f"Invalid food number {food}")
                continue
            return self.zoo.feed(self.choosen_room, FOOD_DICT[food])
             

    def __convert_input_to_int(self, input:str):
        input = input.strip().lower()
        if input == "q":
            return "q"
        try:
            return math.floor(float(input))    
        except ValueError as e:
            return None

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Japaripa Park")
    print("\n"+ "#" *40)
    game = ZooGame()
    game.start()
    
if __name__ == "__main__":
    main()
