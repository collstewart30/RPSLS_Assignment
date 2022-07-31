from html.entities import name2codepoint
from site import USER_BASE
from player import Player
import time

class Human(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        human_name_choice = input('Please enter your player name: ')
        self.name = human_name_choice


    def choose_gesture(self):
        time.sleep(2)
        print(f'{self.name} choose your gesture from the list below:')
        for gesture in self.gesture_list:
            print(f'For {gesture} press {self.gesture_list.index(gesture) + 1}')

        user_choice_confirmed = False
        while user_choice_confirmed == False:
            user_choice = int(input(f'Enter your choice: '))
            print("")
            if user_choice > (len(self.gesture_list)):
                print("I'm sorry, I don't know that gesture. Please try again.")
                user_choice_confirmed = False
            else:
                self.chosen_gesture = self.gesture_list[user_choice -1]
                print(f"{self.name}'s choice: {self.chosen_gesture}")
                print("")
                user_choice_confirmed = True




# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly

