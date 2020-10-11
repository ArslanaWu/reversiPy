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
weight_list = np.array([8, 85, -40, 10, 210, 520],
                       [8, 85, -40, 10, 210, 520],
                       [33, -50, -15, 4, 416, 2153],
                       [46, -50, -1, 3, 612, 4141],
                       [51, -50, 62, 3, 595, 3184],
                       [33, -5, 66, 2, 384, 2777],
                       [44, 50, 163, 0, 443, 2568],
                       [13, 50, 66, 0, 121, 986],
                       [4, 50, 31, 0, 27, 192],
                       [8, 500, 77, 0, 36, 299])

stage_list = [0, 55, 56, 57, 58, 59, 60, 61, 62, 63]

weight_for_stage = np.zeros(65, len(stage_list))


def init_weights():
    for i in range(0, 64):
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
            for j in range(0, len(weight_list)):
                weight_for_stage[i][j] = round(factor * weight_list[w][j]
                                               + (1 - factor) * weight_list[w - 1][j])


def evaluate(chessboard, color):
    return None


def stability(chessboard, color):
    my_score = len(BoardHelper.get_stable_pieces(chessboard, color))
    op_score = len(BoardHelper.get_stable_pieces(chessboard, color * -1))

    return 100 * (my_score - op_score) / (my_score + op_score + 1)


def mobility(chessboard, color):
    my_score = len(BoardHelper.get_all_moves(chessboard, color))
    op_score = len(BoardHelper.get_all_moves(chessboard, color * -1))

    return 100 * (my_score - op_score) / (my_score + op_score + 1)


def placement(chessboard, color):
    score = BoardHelper.get_piece_num(chessboard, color, color * -1)

    return score[0]-score[1]


