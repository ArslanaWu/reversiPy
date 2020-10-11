def can_move(chessboard, color):
    for i in range(0, 8):
        for j in range(0, 8):
            if move_is_valid(i, j, chessboard, color):
                return True
    return False


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
        while (0 < mi < chessboard_size - 1 and 0 < mj < chessboard_size - 1) and \
                chessboard[mi][mj] == op_color:
            mi = mi + move[0]
            mj = mj + move[1]
            changed = True
        if (0 <= mi <= chessboard_size - 1 and 0 <= mj <= chessboard_size - 1) and \
                chessboard[mi][mj] == color and changed:
            return True

    # # move up
    # mi = i - 1
    # mj = j
    # changed = False
    # while mi > 0 and chessboard[mi][mj] == op_color:
    #     mi = mi - 1
    #     changed = True
    # if mi >= 0 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move down
    # mi = i + 1
    # mj = j
    # changed = False
    # while mi < chessboard_size - 1 and chessboard[mi][mj] == op_color:
    #     mi = mi + 1
    #     changed = True
    # if mi <= chessboard_size - 1 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move left
    # mi = i
    # mj = j - 1
    # changed = False
    # while mj > 0 and chessboard[mi][mj] == op_color:
    #     mj = mj - 1
    #     changed = True
    # if mj >= 0 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move right
    # mi = i
    # mj = j + 1
    # changed = False
    # while mj < chessboard_size - 1 and chessboard[mi][mj] == op_color:
    #     mj = mj + 1
    #     changed = True
    # if mj <= chessboard_size - 1 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move up left
    # mi = i - 1
    # mj = j - 1
    # changed = False
    # while mi > 0 and mj > 0 and chessboard[mi][mj] == op_color:
    #     mi = mi - 1
    #     mj = mj - 1
    #     changed = True
    # if mi >= 0 and mj >= 0 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move up right
    # mi = i - 1
    # mj = j + 1
    # changed = False
    # while mi > 0 and mj < chessboard_size - 1 and chessboard[mi][mj] == op_color:
    #     mi = mi - 1
    #     mj = mj + 1
    #     changed = True
    # if mi >= 0 and mj <= chessboard_size - 1 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move down left
    # mi = i + 1
    # mj = j - 1
    # changed = False
    # while mi < chessboard_size - 1 and mj > 0 and chessboard[mi][mj] == op_color:
    #     mi = mi + 1
    #     mj = mj - 1
    #     changed = True
    # if mi <= chessboard_size - 1 and mj >= 0 and chessboard[mi][mj] == color and changed:
    #     return True
    #
    # # move down right
    # mi = i + 1
    # mj = j + 1
    # changed = False
    # while mi < chessboard_size - 1 and mj < chessboard_size - 1 and chessboard[mi][mj] == op_color:
    #     mi = mi + 1
    #     mj = mj + 1
    #     changed = True
    # if mi <= chessboard_size - 1 and mj <= chessboard_size - 1 and chessboard[mi][mj] == color and changed:
    #     return True
    return False


def get_all_moves(chessboard, color):
    move_list = []
    for i in range(0, 8):
        for j in range(0, 8):
            if move_is_valid(i, j, chessboard, color):
                move_list.append((i, j))
    return move_list


def get_stable_pieces(chessboard, color):
    chessboard_size = chessboard.shape[0]

    corner_list = [(0, 0), (0, chessboard_size - 1), (chessboard_size - 1, 0),
                   (chessboard_size - 1, chessboard_size - 1)]
    move_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    stable_piece_list = []

    for corner in corner_list:
        i = corner[0]
        j = corner[1]
        for move in move_list:
            mi = i + move[0]
            mj = j + move[1]
            while (0 < mi < chessboard_size - 1 and 0 < mj < chessboard_size - 1) and \
                    chessboard[mi][mj] == color:
                if (mi, mj) in stable_piece_list:
                    stable_piece_list.append((mi, mj))
                mi = mi + move[0]
                mj = mj + move[1]

    return stable_piece_list


def get_piece_num(chessboard, color, op_color):
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

    for i in chessboard_size:
        for j in chessboard_size:
            if chessboard[i][j] == color:
                num[0] = num[0] + chessboard_score[i][j]
            elif chessboard[i][j] == op_color:
                num[1] = num[1] + chessboard_score[i][j]

    return num


def game_is_finished(chessboard):
    return not (can_move(chessboard, 1) or can_move(chessboard, -1))


def make_move(chessboard, i, j, color):
    new_board = chessboard.copy()
    new_board[i][j] = color
    make_turn(new_board, i, j, color)
    return new_board


def make_turn(chessboard, i, j, color):
    move_list = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    chessboard_size = chessboard.shape[0]
    op_color = -1 * color

    for move in move_list:
        mi = i + move[0]
        mj = j + move[1]
        while (0 < mi < chessboard_size - 1 and 0 < mj < chessboard_size - 1) and \
                chessboard[mi][mj] == op_color:
            chessboard[i][j] = color
            mi = mi + move[0]
            mj = mj + move[1]
