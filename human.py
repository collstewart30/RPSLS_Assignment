from html.entities import name2codepoint
from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        user_choice = input('Please enter a Human name: ')
        self.name = user_choice


    def choose_gesture(self):

        print(f'What is your gesture of choice?')
        for gestures in gestures:
            print(f'For {gestures} press {self.gestures.index(gestures) + 1}')

        user_choice = int(input('Enter your choice: '))

        while user_choice > (len(self.gestures) - 1):
            print("I'm sorry, I don't know that one. Please try again.")
            user_choice = int(input('Enter your choice: '))
        self.chosen_gesture = self.gestures[user_choice -1]




# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly

