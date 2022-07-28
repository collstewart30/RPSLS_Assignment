from game import Game
from player import Player

class Human(Player):

    def __init__(self):
        super().__init()

    def choose_gesture(self):
        user_choice = input('What is your gesture of choice?')



