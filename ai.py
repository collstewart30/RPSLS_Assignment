import random
from player import Player

class AI(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        user_choice = input('Please enter an AI name: ')
        self.name = user_choice


    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'AI {self.name} choice: {self.chosen_gesture}')
