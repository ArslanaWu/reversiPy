import numpy as np
import random
import time

COLOR_BLACK = -1
OLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

MIN_VALUE = float("-inf")
MAX_VALUE = float("inf")

weight_list = np.array([[8, 85, -40, 10, 210, 520],
                        [8, 85, -40, 10, 210, 520],
                        [33, -50, -15, 4, 416, 2153],
                        [46, -50, -1, 3, 612, 4141],
                        [51, -50, 62, 3, 595, 3184],
                        [33, -5, 66, 2, 384, 2777],
                        [44, 50, 163, 0, 443, 2568],
                        [13, 50, 66, 0, 121, 986],
                        [4, 50, 31, 0, 27, 192],
                        [8, 500, 77, 0, 36, 299]])

stage_list = [0, 55, 56, 57, 58, 59, 60, 61, 62, 63]

weight_for_stage = np.zeros((65, weight_list.shape[1]))

opening_list = [
    "C4e3F6e6F5g6E7c5",
    "C4e3F6e6F5g6",
    "C4e3F6e6F5c5F4g6F7g5",
    "C4e3F6e6F5c5F4g6F7d3",
    "C4e3F6e6F5c5F4g6F7",
    "C4e3F6e6F5c5F4g5G4f3C6d3D6b3C3b4E2b6",
    "C4e3F6e6F5c5F4g5G4f3C6d3D6",
    "C4e3F6e6F5c5D6",
    "C4e3F6e6F5c5D3",
    "C4e3F6e6F5c5C3g5",
    "C4e3F6e6F5c5C3c6D6",
    "C4e3F6e6F5c5C3c6D3d2E2b3C1c2B4a3A5b5A6a4A2",
    "C4e3F6e6F5c5C3c6",
    "C4e3F6e6F5c5C3b4D6c6B5a6B6c7",
    "C4e3F6e6F5c5C3b4",
    "C4e3F6e6F5c5C3",
    "C4e3F6e6F5",
    "C4e3F6b4",
    "C4e3F5e6F4c5D6c6F7g5G6",
    "C4e3F5e6F4c5D6c6F7f3",
    "C4e3F5e6F4",
    "C4e3F5e6D3",
    "C4e3F5b4F3f4E2e6G5f6D6c6",
    "C4e3F5b4F3",
    "C4e3F5b4",
    "C4e3F4c5E6",
    "C4e3F4c5D6f3E6c6",
    "C4e3F4c5D6f3E6c3D3e2D2",
    "C4e3F4c5D6f3E6c3D3e2B6f5G5f6",
    "C4e3F4c5D6f3E6c3D3e2B6f5G5",
    "C4e3F4c5D6f3E6c3D3e2B6f5B4f6G5d7",
    "C4e3F4c5D6f3E6c3D3e2B6f5",
    "C4e3F4c5D6f3E6c3D3e2B5f5B4f6C2e7D2c7",
    "C4e3F4c5D6f3E6c3D3e2B5f5B3",
    "C4e3F4c5D6f3E6c3D3e2B5f5",
    "C4e3F4c5D6f3E6c3D3e2B5",
    "C4e3F4c5D6f3E6c3D3e2",
    "C4e3F4c5D6f3E2",
    "C4e3F4c5D6f3D3c3",
    "C4e3F4c5D6f3D3",
    "C4e3F4c5D6f3C6",
    "C4e3F4c5D6e6",
    "C4e3",
    "C4c5",
    "C4c3F5c5",
    "C4c3E6c5",
    "C4c3D3c5F6f5",
    "C4c3D3c5F6e3C6f5F4g5",
    "C4c3D3c5F6e2C6",
    "C4c3D3c5F6",
    "C4c3D3c5D6f4F5e6F6",
    "C4c3D3c5D6f4F5e6C6d7",
    "C4c3D3c5D6f4F5d2G4d7",
    "C4c3D3c5D6f4F5d2B5",
    "C4c3D3c5D6f4F5d2",
    "C4c3D3c5D6f4F5",
    "C4c3D3c5D6f4B4e3B3",
    "C4c3D3c5D6f4B4c6B5b3B6e3C2a4A5a6D2",
    "C4c3D3c5D6f4B4b6B5c6F5",
    "C4c3D3c5D6f4B4b6B5c6B3",
    "C4c3D3c5D6f4B4",
    "C4c3D3c5D6e3",
    "C4c3D3c5D6",
    "C4c3D3c5B6e3",
    "C4c3D3c5B6c6B5",
    "C4c3D3c5B6",
    "C4c3D3c5B5",
    "C4c3D3c5B4e3",
    "C4c3D3c5B4d2E2",
    "C4c3D3c5B4d2D6",
    "C4c3D3c5B4d2C2f4D6c6F5e6F7",
    "C4c3D3c5B4",
    "C4c3D3c5B3f4B5b4C6d6F5",
    "C4c3D3c5B3f3",
    "C4c3D3c5B3",
    "C4c3D3c5B2",
    "C4c3"
]


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
        AI.init_weights()

    def go(self, chessboard):
        self.time_out = time.time() + 4.7

        self.candidate_list.clear()

        move_list = []
        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                if AI.move_is_valid(i, j, chessboard, self.color):
                    self.candidate_list.append((i, j))
                    move_list.append((i, j))

        if len(move_list) > 1:
            best_score = MIN_VALUE
            have_corner = False

            corner_list = [(0, 0), (0, self.chessboard_size - 1), (self.chessboard_size - 1, 0),
                           (self.chessboard_size - 1, self.chessboard_size - 1)]

            for corner in corner_list:
                if corner in move_list:
                    have_corner = True
                    new_board = AI.make_move(chessboard, corner[0], corner[1], self.color)
                    new_score = AI.evaluate(new_board, self.color)
                    if new_score > best_score:
                        self.candidate_list.append(corner)
                        print("move to (" + str(corner[0]) + ", " + str(corner[1]) + "), corner")

            if not have_corner:
                depth = 1

                while True:
                    if time.time() > self.time_out or depth > 100:
                        break

                    best_score = MIN_VALUE
                    best_move = None
                    for move in move_list:
                        flipped_board = AI.make_move(chessboard, move[0], move[1], self.color)
                        new_score = self.min_value(flipped_board, -self.color, depth, MIN_VALUE, MAX_VALUE)
                        # print("v3 move to (" + str(move[0]) + ", " + str(move[1]) + "): score " + str(new_score)
                        #       + ", depth = " + str(depth))
                        if new_score >= best_score:
                            best_score = new_score
                            best_move = move

                    if time.time() < self.time_out:
                        self.candidate_list.append(best_move)

                    depth += 1

                    print("v3 move to (" + str(best_move[0]) + ", " + str(best_move[1]) + "): score " + str(best_score)
                          + ", depth = " + str(depth))

    # BoardHelper
    @staticmethod
    def can_move(chessboard, color):
        for i in range(0, 8):
            for j in range(0, 8):
                if AI.move_is_valid(i, j, chessboard, color):
                    return True
        return False

    @staticmethod
    def move_is_valid(i, j, chessboard, color):
        if chessboard[i][j] != 0:
            return False

        move_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        op_color = -1 * color
        chessboard_size = chessboard.shape[0]

        for move in move_list:
            mi = i + move[0]
            mj = j + move[1]
            changed = False
            while (0 <= mi < chessboard_size and 0 <= mj < chessboard_size) and \
                    chessboard[mi][mj] == op_color:
                mi = mi + move[0]
                mj = mj + move[1]
                changed = True
            if (0 <= mi <= chessboard_size - 1 and 0 <= mj <= chessboard_size - 1) and \
                    chessboard[mi][mj] == color and changed:
                return True
        return False

    @staticmethod
    def get_all_moves(chessboard, color):
        chessboard_size = chessboard.shape[0]

        move_list = []
        for i in range(0, chessboard_size):
            for j in range(0, chessboard_size):
                if AI.move_is_valid(i, j, chessboard, color):
                    move_list.append((i, j))
        return move_list

    @staticmethod
    def get_stable_pieces(chessboard, color):
        chessboard_size = chessboard.shape[0]

        corner_list = [(0, 0), (0, chessboard_size - 1), (chessboard_size - 1, 0),
                       (chessboard_size - 1, chessboard_size - 1)]
        move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stable_piece_list = []

        for corner in corner_list:
            i = corner[0]
            j = corner[1]
            if chessboard[i][j] == color:
                if (i, j) not in stable_piece_list:
                    stable_piece_list.append((i, j))
                for move in move_list:
                    mi = i + move[0]
                    mj = j + move[1]
                    while (0 <= mi < chessboard_size and 0 <= mj < chessboard_size) and \
                            chessboard[mi][mj] == color:
                        if (mi, mj) not in stable_piece_list:
                            stable_piece_list.append((mi, mj))
                        mi = mi + move[0]
                        mj = mj + move[1]

        return stable_piece_list

    @staticmethod
    def get_frontier_places(chessboard, color):
        frontier_list = []
        move_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        op_color = -1 * color
        chessboard_size = chessboard.shape[0]

        for i in range(0, chessboard_size):
            for j in range(0, chessboard_size):
                if chessboard[i][j] == op_color:
                    for move in move_list:
                        mi = i + move[0]
                        mj = j + move[1]
                        if 0 <= mi < chessboard_size and 0 <= mj < chessboard_size \
                                and chessboard[mi][mj] == 0 and (mi, mj) not in frontier_list:
                            frontier_list.append((mi, mj))

        return frontier_list

    @staticmethod
    def get_piece_num(chessboard, color, op_color):
        chessboard_size = chessboard.shape[0]

        num = [0, 0]

        for i in range(0, chessboard_size):
            for j in range(0, chessboard_size):
                if chessboard[i][j] == color:
                    num[0] = num[0] + 1
                elif chessboard[i][j] == op_color:
                    num[1] = num[1] + 1

        return num

    @staticmethod
    def game_is_finished(chessboard):
        return not (AI.can_move(chessboard, 1)
                    or AI.can_move(chessboard, -1))

    @staticmethod
    def make_move(chessboard, i, j, color):
        new_board = chessboard.copy()
        new_board[i][j] = color
        AI.make_turn(new_board, i, j, color)
        return new_board

    @staticmethod
    def make_turn(chessboard, i, j, color):
        move_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        chessboard_size = chessboard.shape[0]
        op_color = -1 * color

        for move in move_list:
            mi = i + move[0]
            mj = j + move[1]
            changed = False
            turn_list = []
            while (0 <= mi < chessboard_size and 0 <= mj < chessboard_size) and \
                    chessboard[mi][mj] == op_color:
                turn_list.append((mi, mj))
                mi = mi + move[0]
                mj = mj + move[1]
                changed = True
            if (0 <= mi <= chessboard_size - 1 and 0 <= mj <= chessboard_size - 1) and \
                    chessboard[mi][mj] == color and changed:
                for turn in turn_list:
                    chessboard[turn[0]][turn[1]] = color

    # Minimax
    def min_value(self, chessboard, color, depth, alpha, beta):
        if time.time() > self.time_out:
            return AI.evaluate(chessboard, self.color)
        if depth <= 0 or AI.game_is_finished(chessboard):
            return AI.evaluate(chessboard, self.color)

        best_score = MAX_VALUE

        move_list = AI.get_all_moves(chessboard, color)
        for move in move_list:
            flipped_board = AI.make_move(chessboard, move[0], move[1], color)
            new_score = self.max_value(flipped_board, -color, depth - 1, alpha, beta)

            best_score = min(best_score, new_score)
            if best_score <= alpha:
                return best_score
            beta = min(beta, best_score)
        return best_score

    def max_value(self, chessboard, color, depth, alpha, beta):
        if time.time() > self.time_out:
            return AI.evaluate(chessboard, self.color)
        if depth <= 0 or AI.game_is_finished(chessboard):
            return AI.evaluate(chessboard, self.color)

        best_score = MIN_VALUE

        move_list = AI.get_all_moves(chessboard, color)
        for move in move_list:
            flipped_board = AI.make_move(chessboard, move[0], move[1], color)
            new_score = self.min_value(flipped_board, -color, depth - 1, alpha, beta)

            best_score = max(best_score, new_score)
            if best_score >= beta:
                return best_score
            alpha = max(alpha, best_score)
        return best_score

    # def alpha_beta_cutoff_search(self, chessboard, color, depth, alpha, beta):

    # op_color = -1 * color
    # alpha = MIN_VALUE
    #
    # if depth <= 0 or AI.game_is_finished(chessboard):
    #     return AI.evaluate(chessboard, color)
    #
    # move_list = AI.get_all_moves(chessboard, color)
    # for move in move_list:
    #     flipped_board = AI.make_move(chessboard, move[0], move[1], color)
    #     new_score = AI.alpha_beta_cutoff_search(flipped_board, op_color, depth - 1, -alpha)
    #     if new_score > alpha:
    #         alpha = new_score
    #         if alpha >= beta:
    #             break
    # return alpha

    # op_color = -1 * color
    #
    # if depth <= 0 or AI.game_is_finished(chessboard):
    #     return AI.evaluate(chessboard, color)
    #
    # move_list = AI.get_all_moves(chessboard, color)
    # if is_max:
    #     best_score = MAX_VALUE
    #     for move in move_list:
    #         flipped_board = AI.make_move(chessboard, move[0], move[1], color)
    #         new_score = AI.alpha_beta_cutoff_search(flipped_board, op_color, not is_max, depth - 1, alpha, beta)
    #         best_score = min(best_score, new_score)
    #
    #         if best_score > alpha:
    #             alpha = best_score
    #         if alpha >= beta:
    #             return best_score
    #
    #     return best_score
    # else:
    #     best_score = MIN_VALUE
    #     for move in move_list:
    #         flipped_board = AI.make_move(chessboard, move[0], move[1], color)
    #         new_score = AI.alpha_beta_cutoff_search(flipped_board, op_color, not is_max, depth - 1, alpha, beta)
    #         best_score = max(best_score, new_score)
    #
    #         if best_score < beta:
    #             beta = best_score
    #         if alpha >= beta:
    #             return best_score
    #
    #     return best_score
    #
    #     # for move in move_list:
    #     #     flipped_board = AI.make_move(chessboard, move[0], move[1], color)
    #     #     new_score = -AI.alpha_beta_cutoff_search(flipped_board, op_color, depth - 1, -alpha, -beta)
    #     #
    #     #     if new_score > alpha:
    #     #         if new_score >= beta:
    #     #             return new_score
    #     #         else:
    #     #             alpha = max(new_score, alpha)
    #     #     else:
    #     #         max_score = max(new_score, max_score)
    #     #
    #     # return max_score

    # Evaluator

    @staticmethod
    def init_weights():
        for i in range(0, 65):
            w = 0
            for j in range(0, len(stage_list)):
                if i <= stage_list[j]:
                    w = j
                    break

            if w == 0:
                weight_for_stage[i] = weight_list[0]
                continue
            else:
                factor = float(i - stage_list[w - 1]) / (stage_list[w] - stage_list[w - 1])
                for j in range(0, weight_list.shape[1]):
                    weight_for_stage[i][j] = round(factor * weight_list[w][j]
                                                   + (1 - factor) * weight_list[w - 1][j])

    @staticmethod
    def evaluate(chessboard, color):
        piece_num_list = AI.get_piece_num(chessboard, color, -color)
        weight = weight_for_stage[piece_num_list[0] + piece_num_list[1]]

        # score = weight[0] * AI.mobility(chessboard, color)
        # + weight[1] * AI.frontier(chessboard, color)
        # + weight[2] * AI.pieces(chessboard, color)
        # + weight[3] * AI.placement(chessboard, color)
        # + weight[4] * AI.stability(chessboard, color)
        # + weight[5] * AI.corner(chessboard, color)

        score = AI.map_weight(chessboard, color) \
                + 10 * AI.stability(chessboard, color) \
                + 30 * AI.mobility(chessboard, color)

        if (piece_num_list[0] + piece_num_list[1]) > 50:
            score = AI.map_weight(chessboard, color) \
                    + 10 * AI.stability(chessboard, color) \
                    + 20 * AI.pieces(chessboard, color)
        return score

    @staticmethod
    def stability(chessboard, color):
        my_score = len(AI.get_stable_pieces(chessboard, color))
        op_score = len(AI.get_stable_pieces(chessboard, -color))

        return my_score - op_score

    @staticmethod
    def mobility(chessboard, color):
        my_score = len(AI.get_all_moves(chessboard, color))
        op_score = len(AI.get_all_moves(chessboard, color * -1))

        return my_score - op_score

    @staticmethod
    def map_weight(chessboard, color):
        chessboard_score1 = np.array([[100, -50, 8, 6, 6, 8, -50, 100],
                                      [-50, -75, -4, -4, -4, -4, -75, -50],
                                      [8, -4, 6, 4, 4, 6, -4, 8],
                                      [6, -4, 4, 0, 0, 4, -4, 6],
                                      [6, -4, 4, 0, 0, 4, -4, 6],
                                      [8, -4, 6, 4, 4, 6, -4, 8],
                                      [-50, -75, -4, -4, -4, -4, -75, -50],
                                      [100, -50, 8, 6, 6, 8, -50, 100]])

        chessboard_score2 = np.array([[500, -25, 10, 5, 5, 10, -25, 500],
                                      [-25, -45, -1, -1, -1, -1, -45, -25],
                                      [10, -1, 3, 2, 2, 3, -1, 10],
                                      [5, -1, 2, 1, 1, 2, -1, 5],
                                      [5, -1, 2, 1, 1, 2, -1, 5],
                                      [10, -1, 3, 2, 2, 3, -1, 10],
                                      [-25, -45, -1, -1, -1, -1, -45, -25],
                                      [500, -25, 10, 5, 5, 10, -25, 500]])

        chessboard_score3 = np.array([[10000, -5000, 5000, 0, 0, 5000, -5000, 10000],
                                      [-5000, -5000, 5000, 0, 0, 5000, -5000, -5000],
                                      [5000, 5000, 5000, 0, 0, 5000, 5000, 5000],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 0],
                                      [5000, 5000, 5000, 0, 0, 5000, 5000, 5000],
                                      [-5000, -5000, 5000, 0, 0, 5000, -5000, -5000],
                                      [10000, -5000, 5000, 0, 0, 5000, -5000, 10000]])

        score = 0

        for i in range(0, 8):
            for j in range(0, 8):
                if chessboard[i][j] == color:
                    score += chessboard_score2[i][j] * color
                if chessboard[i][j] == -color:
                    score += chessboard_score2[i][j] * (-color)

        return score * color

    # @staticmethod
    # def corner(chessboard, color):
    #     chessboard_size = chessboard.shape[0]
    #     corner_list = [(0, 0), (0, chessboard_size - 1), (chessboard_size - 1, 0),
    #                    (chessboard_size - 1, chessboard_size - 1)]
    #     for cor in corner_list:
    #         if AI.move_is_valid(cor[0], cor[1], chessboard, color):
    #             return 100
    #     return 0

    @staticmethod
    def frontier(chessboard, color):
        my_score = len(AI.get_frontier_places(chessboard, color))
        op_score = len(AI.get_frontier_places(chessboard, color * -1))

        return 100 * (my_score - op_score) / (my_score + op_score + 1)

    @staticmethod
    def pieces(chessboard, color):
        num = AI.get_piece_num(chessboard, color, -color)

        return num[0] - num[1]