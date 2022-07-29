# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of 
# gestures within my code (display gesture options, assign player a gesture, etc).
# #NOte Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!
# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!
# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.
# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

import time
from human import Human
from ai import AI

# <!-- Rock crushes Scissors 
# Scissors cuts Paper 
# Paper covers Rock 
# Rock crushes Lizard 
# Lizard poisons Spock 
# Spock smashes Scissors 
# Scissors decapitates Lizard 
# Lizard eats Paper
# Paper disproves Spock 
# Spock vaporizes Rock -->


class Game:

    def __init__(self):
        self.player_one = Human()
        self.player_two = AI()
        

    def run_game(self):
        #self.display_welcome()
        self.choose_game_mode()
        self.choose_gesture()

    def display_welcome(self):
        print("")
        print('Welcome to RPSLS! Only one will win! ')
        time.sleep(1)
        print("")
        print('GAME RULES:\nChoose # of players\nChoose gesture option\nWinner is best 2/3')
        print("")
        print('Gesture options are:')
        print("")
        time.sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        print("")


# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly


    def choose_game_mode(self):
        self.user_choice = input('How many players? 1, 2, or 3? ')

        if self.user_choice == "1":
            self.player_one = Human.set_name(self)
            self.player_two = AI.set_name(self)
        elif self.user_choice == '2':
            self.player_one = Human.set_name(self)
            self.player_two = Human.set_name(self)
        elif self.user_choice == '3':
            self.player_one = AI.set_name(self)
            self.player_two = AI.set_name(self)

    def choose_gesture(self):
        if self.user_choice == '1':
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
        elif self.user_choice == '2':
            self.player_one.choose_gesture(self)
            self.player_two_gesture = Human.choose_gesture(self)
        elif self.user_choice == '3':
            self.player_one_gesture = AI.choose_gesture(self)
            self.player_two_gesture = AI.choose_gesture(self)
        





# Rock crushes Scissors 
# Scissors cuts Paper 
# Paper covers Rock 
# Rock crushes Lizard 
# Lizard poisons Spock 
# Spock smashes Scissors 
# Scissors decapitates Lizard 
# Lizard eats Paper
# Paper disproves Spock 
# Spock vaporizes Rock -->


