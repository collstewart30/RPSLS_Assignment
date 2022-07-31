import random
from player import Player
import time

class AI(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        ai_name_choice = input('Please enter an AI player name: ')
        self.name = ai_name_choice


    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        time.sleep(1)
        print(f"AI {self.name}'s choice: {self.chosen_gesture}")
