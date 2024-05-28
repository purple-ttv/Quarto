# This file was written by Arsenii

# --- Importing all modules ---
from Greeting import OutputGreeting
import globals

# --- MAIN ---
OutputGreeting()                # Showing a greeting message before the game starts

GameMode = input("Would you like to play PvP or PvE? ")

while GameMode != "END":
        

    if GameMode == "PvP":
        with open("PvP.py") as file:
            exec(file.read())
    elif GameMode == "PvE":
        with open("PvE.py") as file:
            exec(file.read())

    GameMode = input("Would you like to play PvP or PvE? (you may write END to exit the game) ")

    #resettin the globals between the games
    globals.Board = [["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"]] 
    globals.LeftPieces = ["LHSN","LHCN","LTSN","LTCN","LHSY","LHCY","LTSY","LTCY","DHSN","DHCN","DTSN","DTCN","DHSY","DHCY","DTSY","DTCY"]
    globals.AvailableCoordinates = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]

print("See you later!")
