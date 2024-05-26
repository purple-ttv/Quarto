import time

def OutputGreeting():
    Greeting = f"""
    Welcome to Quarto!
    In order to win, you have to connect four pieces of idential properties.
    Best of luck! May the games begin!
    """
    print(Greeting)
    time.sleep(3)


def InitializeBoard():
    global Board, FormattedBoard, LeftPieces, IsOver
    IsOver = False
    Board = [["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"]]
    LeftPieces = ["LHSN","LHCN","LTSN","LTCN","LHSY","LHCY","LTSY","LTCY","DHSN","DHCN","DTSN","DTCN","DHSY","DHCY","DTSY","DTCY"]
    FormattedBoard = f"""
    Board:
    | 4 | {Board[0][3]} | {Board[1][3]} | {Board[2][3]} | {Board[3][3]} |
    | 3 | {Board[0][2]} | {Board[1][2]} | {Board[2][2]} | {Board[3][2]} |
    | 2 | {Board[0][1]} | {Board[1][1]} | {Board[2][1]} | {Board[3][1]} |
    | 1 | {Board[0][0]} | {Board[1][0]} | {Board[2][0]} | {Board[3][0]} |
    |   | A    | B    | C    | D    |   
    """


def UpdatePieceList(Piece):
    LeftPieces.remove(Piece)


def TakeFirstInput():
    print(f"Possible pieces: {LeftPieces}")
    Prompt = "Choose your first piece (e.g. LHSN): "
    FirstPiece = input(Prompt)
    UpdatePieceList(FirstPiece)
    return FirstPiece


def TakePieceInput():
    print(f"Possible pieces: {LeftPieces}")
    Piece = input("Choose the piece for your opponent to place: ")
    UpdatePieceList(Piece)
    return Piece


# --- MAIN ---
# Showing a greeting message before the game starts
OutputGreeting()

# Board setup and showcase for first player
InitializeBoard()
print(FormattedBoard)

# Player one chooses his first piece
Piece = TakeFirstInput()

# PlacePiece is called and board updated and checked

# In loop, players choose their piece from a possible list
Piece = TakePieceInput()

# PlacePiece is called and board updated and checked

# Finally, when game is over, a final message is output:
# Player who won and in how many moves / it was a draw