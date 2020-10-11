import BoardHelper
import Evaluator


def alpha_beta_cutoff_search(chessboard, color, depth, is_max, alpha, beta):
    op_color = -1 * color

    if depth <= 0 or BoardHelper.game_is_finished(chessboard):
        return Evaluator.evaluate(chessboard, color)

    if (is_max and not BoardHelper.can_move(chessboard, color)) or \
            (not is_max and not BoardHelper.can_move(chessboard, op_color)):
        return alpha_beta_cutoff_search(chessboard, color, depth - 1,
                                        not is_max, alpha, beta)

    if is_max:
        score = 0x80000000
        moves = BoardHelper.get_all_moves(chessboard, color)
        best_move = (0, 0)

        for move in moves:
            new_board = BoardHelper.make_move(chessboard, move[0], move[1], color)
            new_score = alpha_beta_cutoff_search(new_board, color, depth - 1,
                                                 not is_max, alpha, beta)
            if new_score > score:
                score = new_score
                best_move = move

            if score > alpha:
                alpha = score
            if beta <= alpha:
                return best_move
        return best_move
    else:
        score = 0x7FFFFFFF
        moves = BoardHelper.get_all_moves(chessboard, op_color)
        best_move = (0, 0)

        for move in moves:
            new_board = BoardHelper.make_move(chessboard, move[0], move[1], color)
            new_score = alpha_beta_cutoff_search(new_board, op_color, depth - 1,
                                                 not is_max, alpha, beta)
            if new_score < score:
                score = new_score
                best_move = move

            if score < beta:
                beta = score
            if beta <= alpha:
                return best_move
        return best_move
