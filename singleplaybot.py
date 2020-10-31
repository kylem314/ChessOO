# Compiling the movement for each of the pieces and starting positions
piecevalues = {"P" : 1, "B" : 3, "N" : 3, "R" : 5, "Q" : 9, "K" : 5}
center = ["d4", "d5", "e4", "e5"]
movescore = 0
validmoves = []
# Dictionary of squares where AI has pieces, and their value
mypiecespaces = {}
# ********* Change color to be whatever side the AI is in the future
color = "w"


# Compiling every possible move in a valid entry format (9 lines but a lot of logic)
for key, value in piecedefinitions.items():
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