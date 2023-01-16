# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of 
# gestures within my code (display gesture options, assign player a gesture, etc).
# #NOte Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!
# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!
# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.
# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

import time
from human import Human
from ai import AI


class Game:

    def __init__(self):
        self.player_one = Human()
        self.player_two = AI()
        

    def run_game(self):
        self.display_welcome()
        time.sleep(1)
        self.gesture_options()
        self.choose_game_mode()
        print("")
        self.game_logic()
        self.display_winner()
        self.play_again()

    def display_welcome(self):
        print("")
        print('Welcome to RPSLS! Only one will win! ')
        time.sleep(1)
        print("")
        print('HOW TO PLAY: \nChoose # of players\nChoose gesture option\nWinner is first to 3 points!')
        print("")
    
    def gesture_options(self):
        print('GAME RULES:')
        time.sleep(1)
        print('Rock crushes Scissors')
        time.sleep(1)
        print('Scissors cuts Paper')
        time.sleep(1)
        print('Paper covers Rock')
        time.sleep(1)
        print('Rock crushes Lizard')
        time.sleep(1)
        print('Lizard poisons Spock')
        time.sleep(1)
        print('Spock smashes Scissors')
        time.sleep(1)
        print('Scissors decapitates Lizard')
        time.sleep(1)
        print('Lizard eats Paper')
        time.sleep(1)
        print('Paper disproves Spock')
        time.sleep(1)
        print('Spock vaporizes Rock')
        print("")


# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary. 
# prompts them if they enter something incorrectly


    def choose_game_mode(self):
        self.game_mode = ''
        game_mode_confirmed = False
        while game_mode_confirmed == False:
            self.game_mode = input('Choose 1 for single player. Choose 2 for mulitplayer. Make your choice now: ')
            if self.game_mode == "1":
                self.player_one.set_name()
                self.player_two.set_name()
                game_mode_confirmed = True
            elif self.game_mode == '2':
                self.player_one.set_name()
                self.player_two = Human()
                self.player_two.set_name()
                game_mode_confirmed = True
            else:
                print("I'm sorry, I didn't get that.")
                game_mode_confirmed = False


    def choose_game_gesture(self):
        print("")
        time.sleep(1)
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        print("")


    def game_logic(self):
        while self.player_one.score <3 and self.player_two.score <3:
            self.choose_game_gesture()

            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("")
                print("Both players chose the same gesture! Please choose again.")
                print("")
                self.choose_game_gesture()


            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Scissors':
                print("")
                print('Rock crushes Scissors')
                self.player_one.score += 1
                print("")
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print("")
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("") 
            elif self.player_two.chosen_gesture == 'Rock' and self.player_one.chosen_gesture == 'Scissors':
                print("")
                print('Rock crushes Scissors')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")


            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Paper':
                print("")
                print('Scissors cuts Paper')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Scissors' and self.player_one.chosen_gesture == 'Paper':
                print("")
                print('Scissors cuts Paper')
                print("")
                time.sleep(2)
                self.player_two.score += 1
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")


            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Rock':
                print("")
                print('Paper covers Rock')
                print("")
                time.sleep(2)
                self.player_one.score += 1
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Paper' and self.player_one.chosen_gesture == 'Rock':
                print("")
                print('Paper covers Rock')
                print("")
                time.sleep(2)
                self.player_two.score += 1
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Rock' and self.player_two.chosen_gesture == 'Lizard':
                print("")
                print('Rock crushes Lizard')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')              
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Rock' and self.player_one.chosen_gesture == 'Lizard':
                print("")
                print('Rock crushes Lizard')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Spock':
                print("")
                print('Lizard poisons Spock')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Lizard' and self.player_one.chosen_gesture == 'Spock':
                print("")
                print('Lizard poisons Spock')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Scissors':
                print("")
                print('Spock smashes Scissors')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Spock' and self.player_one.chosen_gesture == 'Scissors':
                print("")
                print('Spock smashes Scissors')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Scissors' and self.player_two.chosen_gesture == 'Lizard':
                print("")
                print('Scissors decapitates Lizard')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Scissors' and self.player_one.chosen_gesture == 'Lizard':
                print("")
                print('Scissors decapitates Lizard')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Lizard' and self.player_two.chosen_gesture == 'Paper':
                print("")
                print('Lizard eats Paper')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Lizard' and self.player_one.chosen_gesture == 'Paper':
                print("")
                print('Lizard eats Paper')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Paper' and self.player_two.chosen_gesture == 'Spock':
                print("")
                print('Paper disproves Spock')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Paper' and self.player_one.chosen_gesture == 'Spock':
                print("")
                print('Paper disproves Spock')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")



            elif self.player_one.chosen_gesture == 'Spock' and self.player_two.chosen_gesture == 'Rock':
                print("")
                print('Spock vaporizes Rock')
                print("")
                self.player_one.score += 1
                time.sleep(2)
                print(f'{self.player_one.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')            
                print("")
                print("")
            elif self.player_two.chosen_gesture == 'Spock' and self.player_one.chosen_gesture == 'Rock':
                print("")
                print('Spock vaporizes Rock')
                print("")
                self.player_two.score += 1
                time.sleep(2)
                print(f'{self.player_two.name} wins round!')
                print(f'Current score: \n{self.player_one.name}: {self.player_one.score}\n{self.player_two.name}: {self.player_two.score}')             
                print("")
                print("")




    def display_winner(self):
        if self.player_one.score == 3:
            print(f'{self.player_one.name} wins game!')
        elif self.player_two.score == 3:
            print(f'{self.player_two.name} wins game!')


    def play_again(self):
        print("")
        play_again_choice = (input("Would you like to play again? Enter 'Y' or 'N': "))

        if play_again_choice == 'Y':
            self.player_two = AI()      # reset player_two as AI - will change in choose_game_mode if mulitplayer in second game
            self.player_one.score = 0
            self.player_two.score = 0
            self.run_game()
        elif play_again_choice == 'y':
            self.player_two = AI()
            self.player_one.score = 0
            self.player_two.score = 0
            self.run_game()
        else:
            print('Thanks for playing!')
            print("")
            pass
