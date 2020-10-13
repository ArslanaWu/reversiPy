from ai_platform.aiplatform import AIPlatform, COLOR_BLACK, COLOR_WHITE
from ai_platform.hum import Hum
import reversi_combine_v2
import reversi_combine_v2

if __name__ == '__main__':
    pf = AIPlatform(8)
    pf.players[0] = ai_v2.AI(8, COLOR_BLACK, 5)
    pf.players[1] = Hum(8, COLOR_WHITE, 100)
    while pf.end_mark != 2:
        print(pf.chessboard)
        pf.go()
    print(pf.statistic())
