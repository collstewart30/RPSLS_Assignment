from player import Player

class AI(Player):

    def __init__(self):
        super().__init__()

#this method will be overwritten in the child class
    def choose_gesture(self):
        # randomly select from list of options and return
        pass

