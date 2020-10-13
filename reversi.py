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
                if BoardHelper.move_is_valid(i, j, chessboard, self.color):
                    self.candidate_list.append((i, j))

        # if len(self.candidate_list) > 1:
        #     Evaluator.init_weights()
        #
        #     best_score = 0x80000000
        #     move_list = BoardHelper.get_all_moves(chessboard, self.color)
        #     for move in move_list:
        #         new_board = BoardHelper.make_move(chessboard, move[0], move[1], self.color)
        #         new_score = Minimax.alpha_beta_cutoff_search(new_board, self.color, 3,
        #                                                      self.color == -1, 0x80000000, 0x7FFFFFFF)
        #         if new_score > best_score:
        #             best_score = new_score
        #             self.candidate_list.append(move)
