# list of gestures here


class Player:

    def __init__(self):
        self.name = ""
        self.score = 0

    def set_name(self, player_number, player_type):
        self.name = input(f'Please enter a(n) {player_type} name for {player_number}: ')

# abstract method that must be overwritten in the child class
    def choose_gesture(self):
        pass
