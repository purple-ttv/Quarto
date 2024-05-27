# This file was written by Vakaris

import globals

def ResolveStatus(Counter):
    if (Counter % 2 == 0):
        globals.Status = 2
    elif (Counter % 2 == 1):
        globals.Status = 1


# This procedure is called when a Quarto is detected
# By taking the move counter (Counter) as a parameter, it changes the global variable Status
# Thus breaking out of the loop and determining the ending message
