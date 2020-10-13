class Hum:

    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list.
        # System will get the end of your candidate_list as your deision .
        self.candidate_list = []

    def go(self, chessboard):
        x = input("input x : ")
        y = input("input y : ")
        self.candidate_list.append((int(x), int(y)))
