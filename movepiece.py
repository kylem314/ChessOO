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

"""
        savefile = open("savereplay.txt", "a")
        savefile.write(Key)
        savefile.close()


        savefile = open("savenotation.txt", "a")
        savefile.write(turnnumberlist[turnnumber - 1] + ". " + whitemovelist[turnnumber - 1] + "\n" + "Black resigned" + "\n")
        savefile.close()
        savefile = open("savereplay.txt", "a")
        savefile.write("#W   ")
        savefile.close()

        savefile = open("savenotation.txt", "a")
        savefile.write("White resigned" + "\n")
        savefile.close()
        savefile = open("savereplay.txt", "a")
        savefile.write("#B   ")
        savefile.close()

          savefile = open("savereplay.txt", "a")
          savefile.write("0-0W ")
          savefile.close()
          savefile = open("savenotation.txt", "a")
          savefile.write("turnnumberlist[turnnumber - 1] + ". " + whitemovelist[turnnumber - 1] + "\n" + "Black resigned" + "\n"")

          savefile = open("savereplay.txt", "a")
          savefile.write("0-0B ")
          savefile.close()
"""

import time
import random
from piecedefinitions import *
from zwhitepersp import *
from zblackpersp import *
from checkfunctions import *
from protectionfunctions import *
import json
#from main import mainmenu, key


def movepiece(board, storeboard, whitemove, whitecolor, blackcolor):
    usermove = input(
        "What move would you like to make? (startsquare endsquare to move a piece, resign to resign the game)\n")
    try:
        move1 = {5: len5}
        move1[len(usermove)](usermove, board, storeboard, whitemove, whitecolor, blackcolor)
    except Exception as e:
        print("Please enter valid move.")
        print(e)
        movepiece(board, storeboard, whitemove, whitecolor, blackcolor)

def len5(usermove, board, storeboard, whitemove, whitecolor, blackcolor):
    if str(whitemove + "R1n") in storeboard["d1"] and board["e1"] == "WK1n" and usermove == "e1 c1":
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
            storeboard = storeboardset(board, whitemove, 1)
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R1n") in storeboard["d8"] and board["e8"] == "BK1n" and usermove == "e8 c8":
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
            storeboard = storeboardset(board, whitemove, 1)
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R1n") in storeboard["f1"] and board["e1"] == "WK1n" and usermove == "e1 g1":
        try:
            for i in storeboard["f1"]:
                if i[0].lower() == "b":
                    raise Exception("no")
            for i in storeboard["g1"]:
                if i[0].lower() == "b":
                    raise Exception("no")
            board["e1"] = "  "
            board["f1"] = "WR1"
            board["g1"] = "WK1"
            board["h1"] = "  "
            blackpersp(whitecolor, blackcolor, board)
            whitemove = "B"
            storeboard = storeboardset(board, whitemove, 1)
        except:
            print("Please enter a valid move.")
    elif str(whitemove + "R1n") in storeboard["f8"] and board["e8"] == "BK1n" and usermove == "e8 g8":
        try:
            for i in storeboard["f8"]:
                if i[0].lower() == "w":
                    raise Exception("no")
            for i in storeboard["g8"]:
                if i[0].lower() == "w":
                    raise Exception("no")
            board["e8"] = "  "
            board["f8"] = "BR1"
            board["g8"] = "BK1"
            board["ah8"] = "  "
            whitepersp(whitecolor, blackcolor, board)
            whitemove = "W"
            storeboard = storeboardset(board, whitemove, 1)
        except:
            print("Please enter a valid move.")
    try:
        if usermove[2] == ' ':
            piece = board[usermove[0:2]]
            startpos = usermove[0:2]
            if piece in storeboard[usermove[3:5]]:
                board[startpos] = '  '
                board[usermove[3:5]] = piece
                savefile = open("savereplay.txt", "a")
                savefile.write(usermove)
                savefile.close()
                '''
                savefile = open("savenotation.txt", "a")
                savefile.write()
                savefile.close()
                '''
                if whitemove == "W":
                    blackpersp(whitecolor, blackcolor, board)
                    whitemove = "B"
                else:
                    whitemove = "W"
                    whitepersp(whitecolor, blackcolor, board)
                storeboard = storeboardset(board, whitemove, 1)
            else:
                print("Please enter a valid move.")
    except Exception as e:
        print("Please enter a valid move.")
        print(e)
    movepiece(board, storeboard, whitemove, whitecolor, blackcolor)

def storeboardset(board, whitemove, setting):
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
    checkmate = False
    settings = ["?", storeboard, checkmate, stalemate]
    if setting != 2:
        if len(storeboard[kingpos]) > 0:
            storeboard = check(board, storeboard, kingpos, whitemove)
        tool = open("zzzztool.txt", "a")
        tool.write(json.dumps(board) + "\n\n")
        tool.close()
        return storeboard
    else:
        return kingpos, storeboard
    return storeboard


def check(board, storeboard, kingpos, whitemove):
    # note that because it is calculating the upcoming move, whitemove is the side that will be in check
    king = board[kingpos]
    piecedict = aidictionarything(storeboard)
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
    board1 = dict(board)
    for piece in piecedict.keys():
        if piece[0].upper() == whitemove:
            for space in board.keys():
                if board[space][0:3] == piece:
                    piecepos = space
                    break
            for move in piecedict[piece]:
                board1 = dict(board)
                board1[piecepos] = '  '
                board1[move] = board[piecepos]
                kingpos2, storeboard2 = storeboardset(board1, whitemove, 2)
                if len(storeboard2[kingpos2]) == 0:
                    storeboard1[move].append(piece)
    print(storeboard1)
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
