from html.entities import name2codepoint
from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()
        

    def set_name(self):
        human_name_choice = input('Please enter a name for this player: ')
        self.name = human_name_choice


    def choose_gesture(self):

        for gesture in self.gesture_list:
            print(f'For {gesture} press {self.gesture_list.index(gesture) + 1}')

        user_choice = int(input(f'Please enter your choice: '))
        self.chosen_gesture = self.gesture_list[user_choice -1]
        print(f"{self.name}'s choice: {self.chosen_gesture}")


        # while user_choice > (len(self.gestures) - 1):
        #     print("I'm sorry, I don't know that one. Please try again.")
        #     user_choice = int(input('Enter your choice: '))




# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly

