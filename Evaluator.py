import numpy as np
import BoardHelper

# weight_list = np.array([ 8,  85, -40, 10, 210,  520],
#                        [ 8,  85, -40, 10, 210,  520],
#                        [33, -50, -15,  4, 416, 2153],
#                        [46, -50,  -1,  3, 612, 4141],
#                        [51, -50,  62,  3, 595, 3184],
#                        [33,  -5,  66,  2, 384, 2777],
#                        [44,  50, 163,  0, 443, 2568],
#                        [13,  50,  66,  0, 121,  986],
#                        [ 4,  50,  31,  0,  27,  192],
#                        [ 8, 500,  77,  0,  36,  299])
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


def evaluate(chessboard, color):
    piece_num_list = BoardHelper.get_piece_num(chessboard, color, color * -1)
    weight = weight_for_stage[piece_num_list[0] + piece_num_list[1]]

    score = weight[0] * mobility(chessboard, color)
    + weight[3] * placement(chessboard, color)
    + weight[4] * stability(chessboard, color)
    + weight[5] * corner(chessboard, color)

    return score


def stability(chessboard, color):
    my_score = len(BoardHelper.get_stable_pieces(chessboard, color))
    op_score = len(BoardHelper.get_stable_pieces(chessboard, color * -1))

    return 100 * (my_score - op_score) / (my_score + op_score + 1)


def mobility(chessboard, color):
    my_score = len(BoardHelper.get_all_moves(chessboard, color))
    op_score = len(BoardHelper.get_all_moves(chessboard, color * -1))

    return 100 * (my_score - op_score) / (my_score + op_score + 1)


def placement(chessboard, color):
    chessboard_size = chessboard.shape[0]

    chessboard_score = [[100, -10, 8, 6, 6, 8, -10, 100],
                        [-10, -25, -4, -4, -4, -4, -25, -10],
                        [8, -4, 6, 4, 4, 6, -4, 8],
                        [6, -4, 4, 0, 0, 4, -4, 6],
                        [6, -4, 4, 0, 0, 4, -4, 6],
                        [8, -4, 6, 4, 4, 6, -4, 8],
                        [-10, -25, -4, -4, -4, -4, -25, -10],
                        [100, -10, 8, 6, 6, 8, -10, 100]]

    num = [0, 0]

    for i in range(0, chessboard_size):
        for j in range(0, chessboard_size):
            if chessboard[i][j] == color:
                num[0] = num[0] + chessboard_score[i][j]
            elif chessboard[i][j] == color*-1:
                num[1] = num[1] + chessboard_score[i][j]

    return num[0] - num[1]


def corner(chessboard, color):
    chessboard_size = chessboard.shape[0]
    corner_list = [(0, 0), (0, chessboard_size - 1), (chessboard_size - 1, 0),
                   (chessboard_size - 1, chessboard_size - 1)]
    for cor in corner_list:
        if BoardHelper.move_is_valid(cor[0], cor[1], chessboard, color):
            return 100
    return 0
