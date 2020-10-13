import numpy as np


class square:
    def __init__(self, n, board, x=False):
        self.n = n
        self.board = board
        if not x:
            self.x = n
        else:
            self.x = x


class board:
    def __init__(self, size, chutes_and_ladders={}):
        self.squares = []
        self.size = size
        for i in range(1, size + 1):
            if i in chutes_and_ladders.keys():
                self.squares.append(square(i, self, chutes_and_ladders[i]))
            else:
                self.squares.append(square(i, self))
        self.squares = np.array(self.squares)

    def getTransfer(self):
        tMatrix = []
        for i in range(1, self.size + 1):
            tRow = np.zeros(self.size)
            for j in range(1, 7):
                end = self.squares[min(i - 1 + j, self.size - 1)].x
                tRow[end - 1] += 1 / 6.0
            tMatrix.append(tRow)
        self.tMatrix = np.array(tMatrix)
