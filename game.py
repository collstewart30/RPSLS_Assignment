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
        self.gesture_options()
        self.choose_game_gesture()
        self.game_logic()

    def display_welcome(self):
        print("")
        print('Welcome to RPSLS! Only one will win! ')
        time.sleep(1)
        print("")
        print('GAME RULES:\nChoose # of players\nChoose gesture option\nWinner is best 2/3')
        print("")
    
    def gesture_options(self):
        print('Gesture options are:')
        print("")
        time.sleep(1)
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        print("")


# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly


    def choose_game_mode(self):
        self.game_mode = ''
        game_mode_confirmed = False
        while game_mode_confirmed == False:
            self.game_mode = input('Choose 1 for player. Choose 2 for mulitplayer. Make your choice now: ')
            if self.game_mode == "1":
                self.player_one.set_name()
                self.player_two.set_name()
                game_mode_confirmed = True
            elif self.game_mode == '2':
                self.player_one.set_name()
                self.player_two.set_name()
                game_mode_confirmed = True
            else:
                print("I didn't get that.")
                game_mode_confirmed = False


    def choose_game_gesture(self):

        self.player_one.choose_gesture()
        self.player_two.choose_gesture()


    def game_logic(self):
        if self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Scissors':
            print('Rock crushes Scissors')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Paper':
            print('Scissors cuts Paper')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Rock':
            print('Paper covers Rock')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Lizard':
            print('Rock crushes Lizard')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Spock':
            print('Lizard poisons Spock')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Scissors':
            print('Spock smashes Scissors')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Lizard':
            print('Scissors decapitates Lizard')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Paper':
            print('Lizard eats Paper')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Spock':
            print('Paper disproves Spock')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Rock':
            print('Spock vaporizes Rock')
            self.player_one.score += 1
            print('{self.player_one.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')
        else:
            self.player_two.score += 1
            print('{self.player_two.name} wins!')
            print('Current sccore: {self.player_one.name}: {self.player_one.score}, {self.player_two.name}: {self.player_two.score}')




