# This file was written by Arsenii

# --- Importing all modules ---
from Greeting import OutputGreeting
from ResetGlobals import ResetGlobals
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

    ResetGlobals()              # Resetting the globals between the games

print("\n See you later!")