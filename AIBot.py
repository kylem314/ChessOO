"""
Most of the time was thinking about the logic for the AI Bot rather than actually coding, so there isn't as much tangible code here yet.
Wanted to use tensorflow, so I looked into that for a couple days but it's very complicated so I decided to use this instead -
Essentially, the computer will look at a certain set of moves, and then evaluate which is the best one out of them based on certain factors, and then execute the highest scoring move.
"""

"""
Factors taken into consideration, in order of weight

Checkmating
Capturing pieces
Checking
Defending own pieces / saving pieces
Controlling center
"""

"""
How to choose which moves to analyze
Depends on how long the run time of the actual scoring system is, if we need to lower the amound of moves checked to make it compute faster, then -

If a piece is being attacked
If a piece can attack a high value piece
If a piece other than king can move away from the back line
"""

"""
Potentially have different systems for choosing moves in the beginning, mid, and endgame

Beginning - Focus more on moving pieces away from starting positions
Midgame - Focus on protecting pieces and attacking high value pieces
Endgame - Focus on protecting pieces, attacking high value pieces, protecting king, blocking enemy kings movement

Gamestate can be determined by piece values on board
"""

"""
Integrate into code when finished by adding a menu option that will start a normal game, but call this program to choose a move every time it is the computers turn.
"""

piecevalues = {"P" : 1, "B" : 3, "N" : 3, "R" : 5, "Q" : 9, "K" : 5}
center = ["d4", "d5", "e4", "e5"]
movescore = 0
squaredict = storeboardset(board, storeboard, whitemove, 1)
piecedict = aidictionarything(storeboard)
validmoves = []
# Dictionary of squares where AI has pieces, and their value
mypiecespaces = {}
# ********* Change color to be whatever side the AI is in the future
color = "w"

"""
aidictionarything(storeboard)    
function to get dictionary where keys are pieces and values are lists of where the pieces can move

dict = storeboardset(board,storeboard,whitemove,setting)
function to set dict to where keys are squares and values are lists of the pieces that can move to it
"""

# Compiling every possible move in a valid entry format (9 lines but a lot of logic)
for key, value in piecedict.items():
  moveentry = ""
  if key[0].lower == color:
    for key2, value2 in board.items():
      if value2[0:2] == key:
        current_piece_location = key2
        moveentry = moveentry + current_piece_location + " "
    for possible_move in value:
      validmoves.append(moveentry + possible_move)

# List of where the AI's pieces are (to find which pieces are being attacked and which are protected)
for key, value in board:
  if value[0].lower == color:
    mypiecespaces.update({key : piecevalues[value[1].upper()]})

# List of attacked pieces (to be used for evaluating) (Key = piece being attacked, Value = piece attacking it)
attackedpieces = {}
# Notes: key = square, value = pieces that can move to the square, key2 = board square being analyzed, value2 = piece on the key2 board square
for key, value in squaredict:
  if key in mypiecespaces.keys:
    for piece in value:
      attackedpieces.update({board(key)[0:3] : piece})
  

    

# Function to evaluate score of moves.  Movename is the move being tested, color is the letter of the AI's side
def evaluate(movename, color):
  # If a piece is being attacked, protect it
