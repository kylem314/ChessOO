import random
from movepiece import aidictionarything, protdictfunc, storeboardset
from movepieceai import aimovepiece

print("aibot is running")

def primaryai(board, storeboard, whitemove, whitecolor, blackcolor):
  # Values for each piece, to be used for evaluating
  piecevalues = {"P" : 1, "B" : 3, "N" : 3, "R" : 5, "Q" : 9, "K" : 5}
  # Dictionary of turns to piecevalues (protecting pieces, controlling center, taking pieces)
  scoremult = {10:[1, 2, 1.5], 20:[2.5, 1.5, 3], 30:[3, 1, 3], 40:[2, 1, 4]}
  # List of center squares
  center = ["d4", "d5", "e4", "e5"]
  # Dictionary of evaluated moves score
  movescoredict = {}
  # Variable for the accumulated score of moves
  movescore = 0
  # Dictionary of protected pieces, where key = piece, value = list of protectors
  storeboard = storeboardset(board, storeboard, whitemove, 1)
  protectiondict = protdictfunc(board, storeboard, whitemove)
  # Dictionary of squares where keys are pieces and values are lists of where the pieces can move
  piecedict = aidictionarything(storeboard)
  # Dictionary of squares where keys are squares and values are lists of which pieces can move to them
  squaredict = storeboardset(board, storeboard, whitemove, 1)
  # List of all the valid moves in the format to be used for move entry
  validmoves = []
  # Dictionary of squares where AI has pieces, and their value
  mypiecespaces = {}
  # List of attacked pieces (to be used for evaluating) (Key = piece being attacked, Value = piece attacking it)
  attackedpieces = {}
  # ********* Change color to be whatever side the AI is in the future
  color = "w"
  aibot(squaredict, piecedict, protectiondict, movescoredict, mypiecespaces, attackedpieces, validmoves, storeboard, movescore, color, board, whitecolor, blackcolor)

def aibot(squaredict, piecedict, protectiondict, movescoredict, mypiecespaces, attackedpieces, validmoves, storeboard, movescore, color, board, whitecolor, blackcolor):
  # Compiling every possible move in a valid entry format for validmoves
  '''
  for key, value in squaredict.items():
    for term in value:
      moveentry = ""
      if term[0].lower() == color:
        for key2, value2 in board.items():
          if value2 == term:
            current_piece_location = key2
            moveentry = moveentry + current_piece_location + " "
            validmoves.append(moveentry + key)
  '''
  for key, value in piecedict.items():
    if key[0].lower() == color:
      moveentry = ""
      for j, k in board.items():
        if k == key:
          current_piece_location = j
          break
      for term in value:
        validmoves.append(current_piece_location + " " + term)
  

  """
  for key, value in piecedict.items():
    if key[0] == color:
      
  """
  print(validmoves)

  """
  # List of where the AI's pieces are (to find which pieces are being attacked and which are protected)
  for key, value in board:
    if value[0].lower == color:
      mypiecespaces.update({key : piecevalues[value[1].upper()]})

  # Notes: key = square, value = pieces that can move to the square, key2 = board square being analyzed, value2 = piece on the key2 board square
  for key, value in squaredict:
    if key in mypiecespaces.keys:
      for piece in value:
        attackedpieces.update({board(key)[0:3] : piece})
    
  # Function to get a score for protecting pieces
  def protscore(movename, color):


  # Function to evaluate scores of moves.  Movename is the move being tested, color is the letter of the AI's side
  def evaluate(movename, color):
      # If a piece is being attacked, protect it
  """

  # Check every possible move
  for move in validmoves:
    movescoredict.update({move: random.randrange(0,1000)})

  print(movescoredict)

  bestmove = ["", 0]
  for move,score in movescoredict.items():
    if score >= bestmove[1]:
      bestmove = [move, score]

  print(bestmove[0] + "  BESTMOVE!!!!!!!!!")
  return bestmove
  #aimovepiece(board, storeboard, color, whitecolor, blackcolor)