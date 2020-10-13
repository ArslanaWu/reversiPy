import BoardHelper
import numpy as np
import reversi_combine

chessboard = np.array(
    [[0, -1, 1, 0, 0, 0, 0, 1], [0, -1, -1, 0, 0, 0, 1, 0], [0, 0, 1, -1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1],
     [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])

print(reversi_combine.AI.get_all_moves(chessboard, -1))
