import numpy as np
import random
import time
import BoardHelper
import Minimax
import Evaluator

COLOR_BLACK = -1
OLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)


# don't change the class name


class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []

    def go(self, chessboard):
        self.candidate_list.clear()

        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                if BoardHelper.move_is_valid(i, j, chessboard, self.chessboard_size, self.color):
                    self.candidate_list.append((i, j))

        if len(self.candidate_list) > 1:
            Evaluator.init_weights()

            best_move = Minimax.alpha_beta_cutoff_search(chessboard, self.color, 3,
                                                         self.color == -1, 0x80000000, 0x7FFFFFFF)
            self.candidate_list.append(best_move)

