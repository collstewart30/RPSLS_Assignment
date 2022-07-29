# list of gestures here



class Player:

    def __init__(self):
        self.name = ""
        self.score = 0
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.chosen_gesture = ''



# abstract method that must be overwritten in the child class
    def choose_gesture(self):
        pass