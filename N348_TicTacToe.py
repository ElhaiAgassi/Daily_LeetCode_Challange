import numpy
from numpy import *


class TicTacToe:

    def __init__(self, n: int):
        self.board = zeros([n, n], numpy.int8)

    def move(self, row: int, col: int, player: int) -> int:
        player_code = 1 if (player == 1) else -1
        board = self.board
        board[row, col] = player_code
        n = len(board[0])

        if n * player_code in [sum(board.diagonal()), sum(numpy.fliplr(board).diagonal(0))] or n * player_code in board.sum(
                0) or n * player_code in board.sum(1):
            return player
        return 0


myclass = TicTacToe(2)
A = [[0,1,1],[1,1,2],[1,0,1]]
for i in A:
    myclass.move(i[0], i[1], i[2])
