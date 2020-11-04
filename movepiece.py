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
from piecedefinitions import *
from zwhitepersp import *
from zblackpersp import *
from checkfunctions import *
from protectionfunctions import *
from main import mainmenu, key


def movepiece(board, storeboard, whitemove, whitecolor, blackcolor):
    usermove = input(
        "What move would you like to make? (startsquare endsquare to move a piece, resign to resign the game)\n")
    try:
        move1 = {2: len2, 3: len3, 4: len4, 5: len5, 6: len6, 7: len7}
        move1[len(usermove)](usermove, board, storeboard, whitemove, whitecolor, blackcolor)
    except Exception as e:
        print("Please enter valid move.")
        print(e)
        movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len2(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    try:
        piece = ""
        startpos = ""
        for key, value in board.items():
            if key[0] == usermove[0] and value[0:2] == str(whitemove.lower() + "p"):
                piece = value
                startpos = key
                break
        if len(usermove) == 4:
            usermove = usermove[2:4]
        if piece in storeboard[usermove]:
            print("hey")
            board[startpos] = '  '
            board[usermove] = piece
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
    movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len3(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if usermove == "0-0":
        if str(whitemove + "R2n") in storeboard["f1"] and board["e1"] == "WK1n" or str(whitemove + "R2n") in storeboard[
            "f8"] and board["e8"] == "BK1n":
            pass
    try:
        piece = ""
        startpos = ""
        x = True
        for i in storeboard[usermove[1:3]]:
            if i[0:2] == str(whitemove + usermove[0]):
                if x:
                    x = False
                    piece = i
                else:
                    print("Please specify the piece that is moving to this space.")
                    x = True
                    break
        if not x:
            for i in board:
                if board[i] == piece:
                    startpos = i
                    break
            board[startpos] = '  '
            board[usermove[1:3]] = piece[0:3]
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
    movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len4(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if usermove[1] == 'x':
        if usermove[0].islower():
            len2(usermove, board, storeboard, whitemove, whitecolor, blackcolor)
        else:
            usermove = usermove.replace('x', '')
            len3(usermove, board, storeboard, whitemove, whitecolor, blackcolor)
    else:
        try:
            piece = ""
            startpos = ""
            x = []
            for i in storeboard[usermove[1:3]]:
                if i[0:2] == whitemove + usermove[0]:
                    x.append(i)
            if not x:
                for i in board:
                    if board[i] == piece:
                        startpos = i
                        break
                board[startpos] = '  '
                board[usermove] = piece[0:3]
                if whitemove == "W":
                    blackpersp(whitecolor, blackcolor, board)
                    whitemove = "B"
                else:
                    whitemove = "W"
                    whitepersp(whitecolor, blackcolor, board)
                storeboard = storeboardset(board, storeboard, whitemove, 1)
                print("hi")
        except Exception as e:
            print("Please enter a valid move.")
            print(e)
        movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len5(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
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
    movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len6(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if usermove.lower() == "resign":
        if whitemove == "W":
            print("GG, Black wins.")
        else:
            print("GG, White wins.")
        time.sleep(10)
        mainmenu(key(6), key, False, False, False, whitecolor, blackcolor, "")
    else:
        print("hi6")
        movepiece(board, storeboard, whitemove, whitecolor, blackcolor)


def len7(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    print("hi7")


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
            if board[i][0:3] == whitemove.upper() + "K1":
                kingpos = i
    if len(storeboard[kingpos]) > 0:
        storeboard = check(board, storeboard, kingpos, whitemove)
    checkmate = False
    settings = ["?", storeboard, checkmate, stalemate]
    print(protdictfunc(board, storeboard, whitemove))

    return storeboard


def check(board, storeboard, kingpos, whitemove):
    print(kingpos)
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
            print("Ky")
            protdict = kingprot(board, protdict, board[i][0:3], i[0], int(i[1]), storeboard)
    return protdict
