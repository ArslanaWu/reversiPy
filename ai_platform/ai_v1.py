from typing import List

import numpy as np
import random
import time
from threading import Timer

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)

MIN_NODE = -1
MAX_NODE = 1

MAX_VAL = 2 ** 32
MIN_VAL = - MAX_VAL

MAX_DEEPTH = 10

TIME_LEFT = 0.002  # the left time to return

DIR = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)


class TimeoutException(Exception):
    def __init__(self, msg):
        self.msg = msg


class AI(object):

    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        self.time_limit = None
        # You need add your decision into your candidate_list.
        # System will get the end of your candidate_list as your deision .
        self.candidate_list = []

        self.val_map = self.init_val_map()

    def init_val_map(self):
        return np.array([
            [500000, -25000, 10000, 5000, 5000, 10000, -25000, 500000],
            [-25000, -45000, 1000, 1000, 1000, 1000, -45000, -25000],
            [10000, 1000, 3000, 2000, 2000, 3000, 1000, 10000],
            [5000, 1000, 2000, 1000, 1000, 2000, 1000, 5000],
            [5000, 1000, 2000, 1000, 1000, 2000, 1000, 5000],
            [10000, 1000, 3000, 2000, 2000, 3000, 1000, 10000],
            [-25000, -45000, 1000, 1000, 1000, 1000, -45000, -25000],
            [500000, -25000, 10000, 5000, 5000, 10000, -25000, 500000],
        ])

    # The input is current chessboard.
    def go(self, chessboard):
        self.time_limit = time.time() + self.time_out - TIME_LEFT
        try:
            self.candidate_list.clear()

            root = AI.Node(self, None, None, chessboard, MAX_NODE)
            root.expend_root()
        except TimeoutException as e:
            print(e.msg)

    class Node:

        def __init__(self, ai, parent, position, chessboard, node_type):
            self.ai = ai
            self.cb_size = ai.chessboard_size
            self.color = ai.color
            self.val_map = ai.val_map
            self.time_limit = ai.time_limit

            self.parent = parent
            self.position = position
            self.chessboard = chessboard
            self.node_type = node_type

            self.alpha = MIN_VAL
            self.beta = MAX_VAL

            self.best_move = None
            self.move_list = []

            self.value = None
            self.children = []

        def expend_root(self):
            self.move_list = self.get_valid_places()

            if not self.move_list:
                return

            # it is root, add all valid before expend deeper node
            self.ai.candidate_list += self.move_list

            self.create_children()

            for max_deepth in range(0, MAX_DEEPTH):
                for child in self.children:
                    child.expend(max_deepth, max_deepth)
                self.update_after()
                if self.best_move:
                    print('v1 best move choose in deepth', max_deepth, ':', self.best_move,
                          'max score:', self.value)
                    self.ai.candidate_list.append(self.best_move)

        def expend(self, ttl, deepth):
            if time.time() > self.time_limit:
                raise TimeoutException(f'time out when ttl = {ttl}, deepth = {deepth}')

            if ttl == 0:
                # the end of this expend, not visit here before
                self.value = self.get_eval()
                return

            if ttl == 1:
                # is leaf in last iteration, now we create its children
                self.move_list = self.get_valid_places()
                self.create_children()
                # self.update_before()

            # expend it
            for child in self.children:
                # child.alpha = self.alpha
                # child.beta = self.beta

                child.expend(ttl - 1, deepth)

            self.update_after()

        def update_before(self):
            """
            Update the alpha and the beta from parent before expending children
            """
            if self.node_type == MAX_NODE:
                # get the beta from parent
                if self.parent:
                    self.beta = self.parent.beta
            else:
                # get the alpha from parent
                if self.parent:
                    self.alpha = self.parent.alpha

        def update_after(self):
            """
            Update the value and the action after expending children (just one level)
            """

            if self.node_type == MAX_NODE:
                max_val = MIN_VAL
                best_move = None
                for child in self.children:
                    child_val = child.get_eval()

                    # # max node, update alpha
                    # if self.alpha < child_val:
                    #     self.alpha = child_val

                    if max_val < child_val:
                        max_val = child_val
                        best_move = child.position

                # # update the parent's beta
                # if self.parent and self.parent.beta > self.alpha:
                #     self.parent.beta = self.alpha

                self.value = max_val
                self.best_move = best_move
            else:
                min_val = MAX_VAL
                min_move = None
                for child in self.children:
                    child_val = child.get_eval()

                    # # min node, update beta
                    # if self.beta > child_val:
                    #     self.beta = child_val

                    if min_val > child_val:
                        min_val = child_val
                        min_move = child.position

                # # update the parent's alpha
                # if self.parent and self.parent.alpha < self.beta:
                #     self.parent.alpha = self.beta

                self.value = min_val
                self.best_move = min_move

        def create_children(self):
            """
            Before call it, the self.move_list should be computed.
            """
            new_type = -1 * self.node_type
            colour = self.color * self.node_type
            for position in self.move_list:
                row, col = position
                new_cb = self.generate_new_chessboard(row, col, colour)
                new_child = AI.Node(self.ai, self, position, new_cb, new_type)
                self.children.append(new_child)

        def get_valid_places(self) -> List[tuple]:
            """
            The color will be auto handled, so no need to input it
            :return: all valid positions
            """

            empty_list = np.where(self.chessboard == COLOR_NONE)
            empty_list = list(zip(empty_list[0], empty_list[1]))

            # if it is MIN_NODE, pick valid places for enemy
            colour = self.color * self.node_type

            ret = []
            for pos in empty_list:
                row, col = pos
                if self.check_valid(row, col, colour):
                    ret.append(pos)
            return ret

        def check_valid(self, row, col, colour) -> bool:
            """
            Check 8 directions
            :return: True is this position is valid for this colour
            """
            for dx, dy in DIR:
                i, j = row + dx, col + dy
                in_mid = False
                while True:
                    if i < 0 or i >= self.cb_size \
                            or j < 0 or j >= self.cb_size:
                        break
                    clr = self.chessboard[i][j]
                    if not in_mid:
                        if clr == -1 * colour:
                            in_mid = True
                            i += dx
                            j += dy
                        else:
                            break
                    else:
                        if clr == -1 * colour:
                            i += dx
                            j += dy
                            continue
                        elif clr == colour:
                            return True
                        else:
                            break
            return False

        def generate_new_chessboard(self, row, col, color) -> np.ndarray:
            """
            Suppose the place is valid.
            :return: A new copy of the current chessboard, with place a chess on (row, col)
            """

            new_cd = np.copy(self.chessboard)
            new_cd[row, col] = color

            for dx, dy in DIR:
                i, j = row + dx, col + dy
                step = 0
                while True:
                    if not (0 <= i < self.cb_size and 0 <= j < self.cb_size) \
                            or new_cd[i][j] == COLOR_NONE:
                        # dir is not valid
                        break
                    if new_cd[i][j] == color:
                        # find another same color chess, update all chesses between them
                        i, j = row + dx, col + dy
                        while step > 0:
                            new_cd[i][j] = color
                            i += dx
                            j += dy
                            step -= 1
                        break
                    else:
                        # keep on finding another same color chess
                        i += dx
                        j += dy
                        step += 1

            return new_cd

        def get_eval(self):
            """
            If value is None, get chessboard evaluation,
            otherwise, return it.
            Notice that the value can be refresh in function update()
            """
            if not self.value:
                self.value = 1.0 * self.get_map_value()
            return self.value

        def get_map_value(self):
            return sum(sum(self.chessboard * self.val_map)) * self.color
