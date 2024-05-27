# This file was written by Vakaris

import globals
import time

def ShowBoard():
    FormattedBoard = f"""
    Board:
    | 4 | {globals.Board[0][3]} | {globals.Board[1][3]} | {globals.Board[2][3]} | {globals.Board[3][3]} |
    | 3 | {globals.Board[0][2]} | {globals.Board[1][2]} | {globals.Board[2][2]} | {globals.Board[3][2]} |
    | 2 | {globals.Board[0][1]} | {globals.Board[1][1]} | {globals.Board[2][1]} | {globals.Board[3][1]} |
    | 1 | {globals.Board[0][0]} | {globals.Board[1][0]} | {globals.Board[2][0]} | {globals.Board[3][0]} |
    |   | A    | B    | C    | D    |   
    """
    print(FormattedBoard)
    time.sleep(1)

# This procedure formats the global 2D board list into a table, and shows it to the user