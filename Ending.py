# This file was written by Vakaris

import time

def Ending(Status):
    time.sleep(3)
    if (Status == 0):
        print("Error 404 - NullStatus")
    elif (Status == 1):
        print("""
        (\_/)
        (*-*)
        _/🏆 Congratulations to player 1, you won!
        """)
    elif (Status == 2):
        print("""
        (\_/)
        (*-*)
        _/🏆 Congratulations to player 2, you won!
        """)
    elif (Status == 3):
        print(">__< It's a draw this time, friendship wins! \n")

# This procedure is used to showcase the result of the game:
# If someone won - the Winner + no. of moves needed
# If it was a draw - it was a draw