from game import Game
from player import Player


def main():
    name1 = input("player1 enter your name:")
    name2 = input("player2 enter your name:")
    player1 = Player(name1, 'x')
    player2 = Player(name2, 'o')
    game = Game(player1, player2)
    game.play()


if __name__ == '__main__':
    main()
