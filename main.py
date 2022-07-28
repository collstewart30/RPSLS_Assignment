from game import Game
from ai import AI
from human import Human
from player import Player

game_one = Game()
game_one.display_welcome()

#we have chosen human vs AI

player_one = Human()
player_one.set_name()
player_two = AI()
player_two.set_name()