class Board:
    def __init__(self):
        self.board = [''] * 9

    def __str__(self):
        str_ = ""
        for i in range(0, 7, 3):
            str_ += f"| {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} | \n"
        return str_

    def make_move(self, player, place):
        if self.board[place] != '':
            raise ValueError
        if place < 0 or place > 8:
            raise IndexError
        self.board[place] = player.marker

    def is_winner(self, marker):
        for i in range(3):
            if self.board[i] == marker and self.board[i + 3] == marker and self.board[i + 6] == marker:
                return True
        for i in range(0, 7, 3):
            if self.board[i] == marker and self.board[i + 1] == marker and self.board[i + 2] == marker:
                return True
        if self.board[0] == marker and self.board[4] == marker and self.board[8] == marker:
            return True
        if self.board[2] == marker and self.board[4] == marker and self.board[6] == marker:
            return True
        return False

    def is_draw(self):
        flag = True
        for i in self.board:
            if i == '':
                flag = False
                break
        if flag is True and self.is_winner("x") is False and self.is_winner("O") is False:
            return True
        return False
