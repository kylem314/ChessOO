"""
Paul Morphy vs Duke Isouard, Paris, 1858
4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4 w k - 1 0
1. Qb8+ Nxb8 2. Rd8#
"""
["Henry Buckle vs NN, London, 1840","Louis Paulsen vs Blachy, New York, 1857","Paul Morphy vs Duke Isouard, Paris, 1858"]
"""
A FEN record contains six fields. The separator between fields is a space. The fields are:[5]

Piece placement (from White's perspective). Each rank is described, starting with rank 8 and ending with rank 1; within each rank, the contents of each square are described from file "a" through file "h". Following the Standard Algebraic Notation (SAN), each piece is identified by a single letter taken from the standard English names (pawn = "P", knight = "N", bishop = "B", rook = "R", queen = "Q" and king = "K"). White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk"). Empty squares are noted using digits 1 through 8 (the number of empty squares), and "/" separates ranks.
Active color. "w" means White moves next, "b" means Black moves next.
Castling availability. If neither side can castle, this is "-". Otherwise, this has one or more letters: "K" (White can castle kingside), "Q" (White can castle queenside), "k" (Black can castle kingside), and/or "q" (Black can castle queenside). A move that temporarily prevents castling does not negate this notation.
En passant target square in algebraic notation. If there's no en passant target square, this is "-". If a pawn has just made a two-square move, this is the position "behind" the pawn. This is recorded regardless of whether there is a pawn in position to make an en passant capture.[6]
Halfmove clock: This is the number of halfmoves since the last capture or pawn advance. The reason for this field is that the value is used in the fifty-move rule.[7]
Fullmove number: The number of the full move. It starts at 1, and is incremented after Black's move.
"""

"""
Data (Line 1) : String
Board (Line 2) : String without slashes named: setboard
Whitemove (Line 2) : Boolean - white = true, black = false
Castling availability (Line 2) : String
En Passant (Line 2) : Don't include
other things (Line 2) : Don't include
Solution (Line 3) : whatever u want
"""


'''

f = open(filename, 'r')
  text = f.read()
  year = re.search('Popularity in (\d\d\d\d)', text)
  if year:
    yearis = year.group(1)
  boynamepopularity = re.findall('<td>(\d+).+<td>(\w+).+<td>\w+', text)
  girlnamepopularity = re.findall('<td>(\d+).+<td>\w+.+<td>(\w+)', text)
  f.close()
  return yearis, girlnamepopularity, boynamepopularity

  re.findall("(.+\d\d\d\d)\n", hi)

  re.findall("(.+\d\d\d\d)\n", txtfile)
  re.findall("(.+/.+/.+/.+/.+/.+/.+/.+)\s", txtfile)
  re.findall(\S\s\S\s\S\s\S\s\S\s\S)


'''

from zwhitepersp import *

# Parsing data



# Line 1
for char in line1:
  print(char)

# Line 2

# Board

# setboard = "4kb1rp2n1ppp4q34p1B14P31Q6PPP2PPP2KR4" example

# List + Dictionary to turn the database stored values into real board values
conversionDict = {"P" : "wp", "N" : "WN", "B" : "WB", "R" : "WR", "Q" : "WQ", "K" : "WK", "p" : "bp", "n" : "BN", "b" : "BB", "r" : "BR", "q" : "BQ", "k" : "BK"}
blankspaces = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Board to be edited to match the database board
board = {
    "a8": "  ", "b8": "  ", "c8": "  ", "d8": "  ", "e8": "  ", "f8": "  ", "g8": "  ", "h8": "  ",
    "a7": "  ", "b7": "  ", "c7": "  ", "d7": "  ", "e7": "  ", "f7": "  ", "g7": "  ", "h7": "  ",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "  ", "b2": "  ", "c2": "  ", "d2": "  ", "e2": "  ", "f2": "  ", "g2": "  ", "h2": "  ",
    "a1": "  ", "b1": "  ", "c1": "  ", "d1": "  ", "e1": "  ", "f1": "  ", "g1": "  ", "h1": "  ", 
}

# Various variables to save temporary data
indexlist = []
counter = 0
savevar = "yes"
for square in board.keys():
  indexlist.append(square)

# Using data from the database to turn into the real board
for key in setboard:
  if key in blankspaces:
    for i in range(int(key)):
      savevar = indexlist[counter]
      board[savevar] = "  "
      counter += 1
  else:
    savevar = indexlist[counter]
    board[savevar] = conversionDict[key]
    counter += 1

# With the converted board, print it into a visual.  In the website, this would be replaced by the board shown there
whitepersp(whitecolor, blackcolor, board) 