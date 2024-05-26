# this file was written by Arsenii

import globals

def PlacePiece(Piece):
    
    StringCoordinates = input(f"Where would you like to place {Piece}? ")
    while not (StringCoordinates in globals.AvailableCoordinates):
        input("Invalid coordinates, please try again placing {Piece}: ")
    globals.AvailableCoordinates.remove(StringCoordinates)

    XCoordinate = ord(StringCoordinates[0]) - 65 #ord() gives an ASCII value for the character, A code is 65
    YCoordinate = int(StringCoordinates[1]) - 1 #taking the second character from StringCoordinates, but subtracting one because list index starts from 0

    globals.Board[XCoordinate][YCoordinate] = Piece

    print(globals.Board)


