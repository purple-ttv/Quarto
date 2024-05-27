# this file was written by Arsenii

import globals

def CheckBoard(): #Board[XCoordinate][YCoordinate]
    #check horizontal
    for YIndex in range(4): #checking among the same YCoordinate (same line)
        for CharacterIndex in range(4):
            if (
                globals.Board[0][YIndex][CharacterIndex] 
                == globals.Board[1][YIndex][CharacterIndex] 
                == globals.Board[2][YIndex][CharacterIndex] 
                == globals.Board[3][YIndex][CharacterIndex]
                != "-"
            ): #comparison of all four plus making sure that it is not a null value
                return True

    #check vertical
    for XIndex in range(4): #checking among the same XCoordinate (same column)
        for CharacterIndex in range(4):
            if (
                globals.Board[XIndex][0][CharacterIndex] 
                == globals.Board[XIndex][1][CharacterIndex] 
                == globals.Board[XIndex][2][CharacterIndex] 
                == globals.Board[XIndex][3][CharacterIndex]
                != "-"
            ): #comparison of all four plus making sure that it is not a null value
                return True
    #check diagonal

    for CharacterIndex in range(4): #there are just two diagonals 
        if (
            globals.Board[0][0][CharacterIndex] 
            == globals.Board[1][1][CharacterIndex] 
            == globals.Board[2][2][CharacterIndex] 
            == globals.Board[3][3][CharacterIndex]
            != "-"
        ): #comparison of all four plus making sure that it is not a null value
            return True
        if (
            globals.Board[0][3][CharacterIndex] 
            == globals.Board[1][2][CharacterIndex] 
            == globals.Board[2][1][CharacterIndex] 
            == globals.Board[3][0][CharacterIndex]
            != "-"
        ): #comparison of all four plus making sure that it is not a null value
            return True        
    return False


