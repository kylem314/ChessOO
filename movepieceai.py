"""
so basically class this somehow?
loop a function until game end
take user input
two notations:
  previous space to space notation
    check storeboard[endspace] for if the piece on startspace is in the list
      if it is, run check function
      if check function returns false, move piece, then run reassignment of storeboard
    have special stuff (like castling)
  actual chess notation
    try:
      if len(input) == 2:
        pawn move check, put correct variables
      elif len(input) == 3:
        check if castling
        piece movemeent
      elif len(input) == 4:
        capturing, figure out if pawn or actual piece
      elif len(input) == 5:
        check if queenside castling

"""

import time
import random
from piecedefinitions import *
from zwhitepersp import *
from zblackpersp import *
from checkfunctions import *
from protectionfunctions import *
#from main import mainmenu, key


def aimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aiturn):
    if aiturn == True:
        input("Press enter")
        #usermove = "a2 a4"
        usermove = primaryai(board, storeboard, whitemove, whitecolor, blackcolor, turnnum)
        # print(usermove + "UWUWUWU")
        ailen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum, False)
    else:
        usermove = input(
            "What move would you like to make? (startsquare endsquare to move a piece, resign to resign the game)\n")
        try:
            move1 = {2: len2, 3: len3, 4: len4, 5: len5, 6: len6, 7: len7}
            move1[len(usermove)](usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum)
        except Exception as e:
            # print("Please enter valid move.")
            print(e)
            aimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aiturn)


def len5(usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum):
    aiturn = False
    if usermove == "0-0-0":
        if str(whitemove + "R1n") in storeboard["d1"] and board["e1"] == "WK1n":
            try:
                for i in storeboard["d1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                for i in storeboard["c1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                for i in storeboard["b1"]:
                    if i[0].lower() == "b":
                        raise Exception("no")
                board["e1"] = "  "
                board["d1"] = "WR1"
                board["c1"] = "WK1"
                board["a1"] = "  "
                blackpersp(whitecolor, blackcolor, board)
                whitemove = "B"
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                aiturn = True
            except:
                print("Please enter a valid move.")
        elif str(whitemove + "R1n") in storeboard["d8"] and board["e8"] == "BK1n":
            try:
                for i in storeboard["d8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                for i in storeboard["c8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                for i in storeboard["b8"]:
                    if i[0].lower() == "w":
                        raise Exception("no")
                board["e8"] = "  "
                board["d8"] = "BR1"
                board["c8"] = "BK1"
                board["a8"] = "  "
                whitepersp(whitecolor, blackcolor, board)
                whitemove = "W"
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                aiturn = True
            except:
                print("Please enter a valid move.")
        else:
          print("Please enter a valid move.")
    try:
        if usermove[2] == ' ':
            piece = board[usermove[0:2]]
            startpos = usermove[0:2]
            if piece in storeboard[usermove[3:5]]:
                board[startpos] = '  '
                board[usermove[3:5]] = piece
                if whitemove == "W":
                    blackpersp(whitecolor, blackcolor, board)
                    whitemove = "B"
                else:
                    whitemove = "W"
                    whitepersp(whitecolor, blackcolor, board)
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                aiturn = True
            else:
                print("Please enter a valid move.")
    except Exception as e:
        print("Please enter a valid move.")
        print(e)
    aimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, turnnum + 1, aiturn)

def ailen5(usermove, board, storeboard, whitemove, whitecolor, blackcolor, turnnum, aicolor):
    try:
        if usermove[2] == ' ':
            piece = board[usermove[0:2]]
            startpos = usermove[0:2]
            if piece in storeboard[usermove[3:5]]:
                board[startpos] = '  '
                board[usermove[3:5]] = piece
                if whitemove == "W":
                    blackpersp(whitecolor, blackcolor, board)
                    whitemove = "B"
                else:
                    whitemove = "W"
                    whitepersp(whitecolor, blackcolor, board)
                storeboard = storeboardset(board, storeboard, whitemove, 1)
            else:
                print("Please enter a valid move.")
    except Exception as e:
        print("Please enter a valid move.")
        print(e)
    aimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, turnnum + 1, False)

def storeboardset(board, storeboard, whitemove, setting):
    storeboard = {
        "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
        "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
        "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
        "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
        "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
        "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
        "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
        "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
    piecefunc = {"wp": wpawn, "bp": bpawn, "WN": wknight, "BN": bknight, "WR": wrook, "BR": brook, "WB": wbishop,
                 "BB": bbishop, "WQ": wqueen, "BQ": bqueen, "WK": wking, "BK": bking}
    stalemate = True
    for i in board:
        piece = board[i][0:2]
        if piece != '  ':
            storeboard1 = storeboard
            storeboard = piecefunc[piece](board, storeboard, board[i], i[0], int(i[1]))
            if storeboard == storeboard1 and piece[0].upper() == whitemove:
                stalemate = False
            if board[i][0:3] == whitemove + "K1":
                kingpos = i
    #if len(storeboard[kingpos]) > 0:
        #storeboard = check(board, storeboard, kingpos, whitemove)  
    checkmate = False
    settings = ["?", storeboard, checkmate, stalemate]
    return storeboard


def check(board, storeboard, kingpos, whitemove):
    # print(kingpos)
    king = board[kingpos]
    storeboard1 = {
        "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
        "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
        "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
        "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
        "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
        "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
        "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
        "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
    check = True
    checkmate = True
    attacking = storeboard[kingpos[0]]
    try:
        attacking1 = storeboard[kingpos[1]]
    except Exception:
        doublecheck = False

    for i in storeboard.values():
        if king in i:
            try:
                for k in i:
                    if k[0].upper() == whitemove:
                        raise Exception("exception")
                storeboard1[i].append(king)
            except Exception:
                pass
            checkmate = False
    if not doublecheck:
        for key, value in board.items():
            if value == attacking:
                attackingpos = key
                break
        checkfunctions = {"N": Ncheck, "B": Bcheck, "R": Rcheck, "Q": Qcheck, "p": whitemove.lower() + check}
        checkfunctions[attacking[0]](kingpos, attackingpos, storeboard, storeboard1)

    return storeboard1


def aidictionarything(storeboard):
    dictionary = {
        "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
        "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
        "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
        "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
    for i in storeboard:
        for k in storeboard[i]:
            dictionary[k[0:3]].append(i)
    return dictionary


# this gets a dict with key = protected, term = list of protectors
def protdictfunc(board, storeboard, whitemove):
    protdict = {
        "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
        "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
        "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
        "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
    protfunc = {"wp": wpawnprot, "bp": bpawnprot, "WN": knightprot, "BN": knightprot, "WR": wrookprot, "BR": brookprot,
                "WB": wbishopprot, "BB": bbishopprot, "WQ": wqueenprot, "BQ": bqueenprot}

    for i in board:
        piece = board[i][0:2]
        if piece != '  ' and piece[1] != 'K':
            protdict = protfunc[piece](board, protdict, board[i][0:3], i[0], int(i[1]))
        elif piece[1] == 'K':
            # print("Ky")
            protdict = kingprot(board, protdict, board[i][0:3], i[0], int(i[1]), storeboard)
    return protdict

    """
      storeboard = storeboardset(board, storeboard, whitemove, 1)
      protectiondict = protdictfunc(board, storeboard, whitemove)
      piecedict = aidictionarything(storeboard)
      squaredict = storeboardset(board, storeboard, whitemove, 1)
      mypiecespaces = {}
      enemypiecespaces = {}
      attackedpieces = {}
      movescore = 0
      for piecevalue in enemypiecespaces.values():
        pre_enemyscore += piecevalue
      for key, value in board.items():
        if value != "  ":
          if value[0].lower == color:
            mypiecespaces.update({key : piecevalues[value[1].upper()]})
          elif value[0].lower != color:
            enemypiecespaces.update({key : piecevalues[value[1].upper()]})
      for key, value in squaredict:
        for piece in value:
          if key in mypiecespaces.keys() and piece[0] != color:
            attackedpieces.update({board[key][0:4] : piece})
    """

def primaryai(board, storeboard, whitemove, whitecolor, blackcolor, turnnum):
    # Values for each piece, to be used for evaluating
    piecevalues = {"P" : 1, "B" : 3, "N" : 3, "R" : 5, "Q" : 9, "K" : 5}
    # Dictionary of turns to piecevalues (protecting pieces, controlling center, taking pieces)
    scoremult = {30:[2, 1, 4], 20:[3, 1, 3], 10:[2.5, 1.5, 3], 0:[1, 2, 1.5]}
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
    # Dictionary of squares where AI/enemy has pieces, and their value
    mypiecespaces = {}
    enemypiecespaces = {}
    pre_enemyscore = 0
    # List of attacked pieces (to be used for evaluating) (Key = piece being attacked, Value = piece attacking it)
    attackedpieces = {}
    # ********* Change color to be whatever side the AI is in the future
    color = whitemove.lower()
      # Compiling every possible move in a valid entry format for validmoves

    for key, value in piecedict.items():
        if key[0].lower() == color:
            moveentry = ""
            for j, k in board.items():
                if k[0:3] == key:
                    current_piece_location = j
                    break
            for term in value:
                validmoves.append(current_piece_location + " " + term)
    # print(squaredict)
    # print(validmoves)

    # Calculating the enemy total piece score to find the differential
    for piecevalue in enemypiecespaces.values():
      pre_enemyscore += piecevalue

    # List of where the AI's pieces are (to find which pieces are being attacked and which are protected)
    for key, value in board.items():
      if value != "  ":
        if value[0].lower == color:
          mypiecespaces.update({key : piecevalues[value[1].upper()]})
        elif value[0].lower != color:
          enemypiecespaces.update({key : piecevalues[value[1].upper()]})
      

    # Notes: key = square, value = pieces that can move to the square, key2 = board square being analyzed, value2 = piece on the key2 board square
    for key, value in squaredict:
      for piece in value:
        if key in mypiecespaces.keys() and piece[0] != color:
          attackedpieces.update({board[key][0:4] : piece})

    # Function to get a score for attacked pieces
    def attackedscore(movename, color, attackedpieces, protectiondict):
      score = 0
      for piece in attackedpieces.keys():
        if piece not in protectiondict:
          score -= piecevalues[piece[1].upper()]
      # balancing
      score = score * 30
      return score

    def killscore(movename, color, enemypiecesspaces, pre_enemyscore):
      score = 0
      post_enemyscore = 0
      for piecevalue in enemypiecespaces.values():
        post_enemyscore += piecevalue
      # balancing
      score = pre_enemyscore - post_enemyscore
      score = score * -80
      return score
      
    def centercontrol(movename, color, board, squaredict, mypiecespaces, protectiondict):
      center = ["d4", "d5", "e4", "e5"]
      centerscore = 0
      centerpieces = []
      # If a piece is attacking the center
      for square, piece in squaredict.items():
        if square in center:
          for var3 in piece:
            if var3[0].lower() == color:
              centerscore += 4

      # If a piece is in the center
      for square in mypiecespaces.keys():
        if square in center:
          centerscore += 6
          for key, value in board.items():
            if key == square:
              centerpieces.append(value)
              
      # If a piece is defending an allied piece in the center
      for piece in centerpieces:
        for key, value in protectiondict.items():
          if key == piece:
            for piece2 in value:
              centerscore += 9
      centerscore = centerscore * 1.5 # bruh just move this like a line down
      return centerscore
            
        
        


    # Function to evaluate scores of moves.  Movename is the move being tested, color is the letter of the AI's side
    def evaluate(movename, color, board, storeboard, whitemove, pre_enemyscore, turnnum):  
      piecevalues = {"P" : 1, "B" : 3, "N" : 3, "R" : 5, "Q" : 9, "K" : 5}
      storeboard = storeboardset(board, storeboard, whitemove, 1)
      protectiondict = protdictfunc(board, storeboard, whitemove)
      piecedict = aidictionarything(storeboard)
      squaredict = storeboardset(board, storeboard, whitemove, 1)
      mypiecespaces = {}
      enemypiecespaces = {}
      attackedpieces = {}
      movescore = 0
      for key, value in board.items():
        if value != "  ":
          if value[0].lower() == color:
            mypiecespaces.update({key : piecevalues[value[1].upper()]})
          elif value[0].lower() != color:
            enemypiecespaces.update({key : piecevalues[value[1].upper()]})
      for piecevalue in enemypiecespaces.values():
        pre_enemyscore += piecevalue
      for key, value in squaredict:
        for piece in value:
          if key in mypiecespaces.keys() and piece[0] != color:
            attackedpieces.update({board[key][0:4] : piece})
      for turn, multiplier in scoremult.items():
        if turnnum >= turn:
          movescore += attackedscore(movename, color, attackedpieces, protectiondict) * multiplier[0]
          # print(movescore)
          movescore += killscore(movename, color, enemypiecespaces, pre_enemyscore) * multiplier [1]
          # print(movescore)
          movescore += centercontrol(movename, color, board, squaredict, mypiecespaces, protectiondict) * multiplier [2]
          # print(movescore)
          break 
      return {movename : movescore}
      
    
    # Check every possible move
    for move in validmoves:
        # print(move)
        aiboard = board.copy()
        aipiece = aiboard[move[0:2]]
        aiboard[move[0:2]] = '  '
        aiboard[move[3:5]] = aipiece
        ## print(aiboard)
        #movescoredict.update
        movescoredict.update(evaluate(move, color, aiboard, storeboard, color.upper(), pre_enemyscore, turnnum))
        
    #    movescoredict.update({move: random.randrange(0,1000)})

    ## print(movescoredict)
    bestmove = ["", -9999]
    for move, score in movescoredict.items():
      if score >= bestmove[1]:
        bestmove = [move, score]
        # print("Changed to " + str(score))

    # print(bestmove[0] + "  BESTMOVE!!!!!!!!!")
    return bestmove[0]

