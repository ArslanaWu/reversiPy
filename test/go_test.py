import numpy as np

from reversi_combine_v2 import AI

chessboard = np.array(
    [[0, 0, -1, -1, -1, -1, 0, 0],
     [0, 0, -1, -1, -1, -1, 0, 1],
     [1, -1, -1, -1, -1, -1, 1, 1],
     [1, -1, -1, 1, -1, -1, -1, 1],
     [1, -1, 1, 1, 1, 1, -1, 1],
     [1, -1, 1, -1, -1, -1, 0, 1],
     [1, 1, -1, -1, 0, -1, 0, 1],
     [1, -1, -1, -1, -1, -1, 0, 0]])

ai = AI(8, -1, 5)
ai.go(chessboard)