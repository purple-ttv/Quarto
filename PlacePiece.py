# this file was written by Arsenii

import globals

def PlacePiece(Piece):
    
    StringCoordinates = input(f"Where would you like to place {Piece}? ")
    while not (StringCoordinates in globals.AvailableCoordinates):
        StringCoordinates = input(f"Invalid coordinates, please try again placing {Piece}: ")
    globals.AvailableCoordinates.remove(StringCoordinates)

    XCoordinate = ord(StringCoordinates[0]) - 65 #ord() gives an ASCII value for the character, A code is 65
    YCoordinate = int(StringCoordinates[1]) - 1 #taking the second character from StringCoordinates, but subtracting one because list index starts from 0

    globals.Board[XCoordinate][YCoordinate] = Piece

    #print(globals.Board)


# This procedure places the piece (taken as parameter), and places it on the board
# i.e. inserts into the correct position in the global 2D array
# Also ensure that a valid and available coordinate value is entered
