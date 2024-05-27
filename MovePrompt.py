# This file was written by Vakaris

import time

def WhoseMove(Counter):
    time.sleep(1)
    if (Counter % 2 == 1):
        print("")
        print("--- Player 1's move ---")
    elif (Counter % 2 == 0):
        print("")
        print("--- Player 2's move ---")