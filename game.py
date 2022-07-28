# (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of 
# gestures within my code (display gesture options, assign player a gesture, etc).
# #NOte Do not use a Gesture class until you have reached MVP for all user stories and been checked off by an instructor!
# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player. See Framework document for game rules!
# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.
# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.



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
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.choose_gesture()

    def display_welcome(self):
        print("")
        print('Welcome to RPSLS! Only one will win! ')
        print("")
        print('Game rules:\nChoose # of players\nBest 2/3\nOptions are:')
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock')
        print("")

    def choose_game_mode(self):
        user_choice = input('How many players? 1, 2, or 3? ')

        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == '2':
            self.player_one = Human()
            self.player_two = Human()
        elif user_choice == '3':
            self.player_one = AI()
            self.player_two = AI()

    def choose_gesture(self):
        self.player_one_gesture = Human()
        self.player_two_gesture = AI()
        

