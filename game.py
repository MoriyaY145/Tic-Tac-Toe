from board import Board
from player import Player


class Game(Board, Player):
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

    def play(self):
        marker1 = self.player1.marker
        marker2 = self.player2.marker
        while self.board.is_winner(marker1) is False and self.board.is_winner(marker2) is False and self.board.is_draw() is False:
            print(self.board)
            print("enter place")
            place = int(input())
            if self.turn % 2 != 0:
                # self.board.make_move(self.player1, place)
                while True:
                    try:
                        self.board.make_move(self.player1, place)
                    except ValueError:
                        print("The slot is full")
                    except IndexError:
                        print("The index does not exist")
                    else:
                        break
                    print("enter place")
                    place = int(input())
            else:
                # self.board.make_move(self.player2, place)

                while True:
                    try:
                        self.board.make_move(self.player2, place)
                    except ValueError:
                        print("The slot is full")
                    except IndexError:
                        print("The index does not exist")
                    else:
                        break
                    print("enter place")
                    place = int(input())
            self.turn += 1
        if self.board.is_winner(marker1) is True:
            print("the winner is " + self.player1.name)
        elif self.board.is_winner(marker2) is True:
            print("the winner is " + self.player2.name)
        else:
            print("there is no winner")



