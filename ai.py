import random
from player import Player

class AI(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        ai_name_choice = input('Please enter an AI name: ')
        self.name = ai_name_choice


    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        print(f'AI {self.name} choice: {self.chosen_gesture}')
