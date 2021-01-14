import uuid
from animation import *
from movepiece import movepiece
from movepieceai import aimovepiece
from zwhitepersp import *

# Function Definitions
# exec(open("password.py").read())


def replaygame():
    exec(open("replaygame.py").read())

def key(string_length=10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]

def settingmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset):
    while not settingexit:
        try:
            print(colors[whitecolor] + "\nWhite Piece Color - " + whitecolor + colors[
                blackcolor] + "\nBlack Piece Color - " + blackcolor + u"\u001b[0m")
        except Exception:
            print("Please enter a valid color")
        for key, value in colors.items():
            if key != "electric blue":
                print(value + key, end=", ")
            else:
                print(value + key + u"\u001b[0m")
        print("\nType white,color or black,color to change the piece colors (ex. white,orange)")
        print("Type exit to return to the menu\n")
        setting = input("What would you like to do? \n")
        setting = setting.lower()
        if setting[:6] == "white,":
            whitecolor = setting[6:]
        elif setting[:6] == "black,":
            blackcolor = setting[6:]
        elif setting == "exit":
            settingexit = True
            print("")
        else:
            print("Please enter a valid response\n")
    global colorsets
    colorsets = whitecolor + "!" + blackcolor


# Board Dictionary
board_W = 8  # how wide the board is
board_H = 8  # how tall the board is
board = {
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"}

ogstoreboard = {
    "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
    "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
    "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
    "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
    "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
    "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
    "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
    "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}

storeboard = {
    "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
    "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
    "a6": ["bp1"], "b6": ["bp2"], "c6": ["bp3", "BN1"], "d6": ["bp4"], "e6": ["bp5"], "f6": ["bp6", "BN2"],
    "g6": ["bp7"], "h6": ["bp8"],
    "a5": ["bp1"], "b5": ["bp2"], "c5": ["bp3"], "d5": ["bp4"], "e5": ["bp5"], "f5": ["bp6"], "g5": ["bp7"],
    "h5": ["bp8"],
    "a4": ["wp1"], "b4": ["wp2"], "c4": ["wp3"], "d4": ["wp4"], "e4": ["wp5"], "f4": ["wp6"], "g4": ["wp7"],
    "h4": ["wp8"],
    "a3": ["wp1"], "b3": ["wp2"], "c3": ["wp3", "WN1"], "d3": ["wp4"], "e3": ["wp5"], "f3": ["wp6", "WN2"],
    "g3": ["wp7"], "h3": ["wp8"],
    "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
    "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}

# Colors Dictionary
colors = {"pink": u"\u001B[31m", "neon green": u"\u001B[32m", "orange": u"\u001B[33m", "blue": u"\u001B[34m",
          "purple": u"\u001B[35m", "lighter blue": u"\u001B[36m", "red": u"\u001B[91m", "green": u"\u001B[92m",
          "orange yellow": u"\u001B[93m", "lavender": u"\u001B[95m", "electric blue": u"\u001B[96m"}

# Variable Definitions
Key = key(6)
text = ["BR", "BN", "BB", "BQ", "BK", "bp", "WR", "WN", "WB", "WQ", "WK", "wp"]
piece = ["♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ ", "♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ "]
turnnumber = 0
turnappend = ""
turnnumberlist = ["Turn number:"]
whitemovelist = ["White Moves:"]
blackmovelist = ["Black Moves:"]
testvar1 = "hi"
testvar2 = "bye"
testvar3 = -1
counter1 = 0
whitemove = "W"
checkmate = False
wkcastle = True
wqcastle = True
bkcastle = True
bqcastle = True
firstturn = False
squarecheck = 0
whitecolor = "red"
blackcolor = "lighter blue"
replaying = False
whiteking = "e1"
blackking = "e8"
exited = False
colorset = ""
settingexit = False
capturing = False
moveable = False
turnrecorded = False
wkspaces = []
bkspaces = []

"""
class Piece: 

    def __init__(self,color,name,position,ascii):
      self.color = color
      self.name = name
      self.position = position
      #self.row = row
      self.ascii = ascii

WR1 = Piece('White','Rook','a1',"♜")
WN1 = Piece('White','Knight','b1',"♞ ")
WB1 = Piece('White','Bishop','c1',"♝ ")
WQ = Piece('White','Queen','d1',"♛ ")
WK = Piece('White','King','e1',"♚ ")
WB2 = Piece('White','Bishop','f1',"♝ ")
WN2 = Piece('White','Knight','g1',"♞ ")
WR3 = Piece('White','Rook','h1',"♜ ")
wp1 = Piece('White','pawn','a2',"♟")
wp2 = Piece('White','pawn','b2',"♟")
wp3 = Piece('White','pawn','c2',"♟")
wp4 = Piece('White','pawn','d2',"♟")
wp5 = Piece('White','pawn','e2',"♟")
wp6 = Piece('White','pawn','f2',"♟")
wp7 = Piece('White','pawn','g2',"♟")
wp8 = Piece('White','pawn','h2',"♟")
async def runTitle():
  exec(open("animation.py").read())
    menuAni()
"""
# runTitle()

# exec(open("password.py").read())

# exec(open("animation.py").read())


# exec(open("movepiece.py").read())
# menuAni()

# blackpersp(whitecolor,blackcolor)

"""
print('Enter your move:')
x = input()
print(x[0]+x[1])
print(x[3]+x[4])
"""


# time.sleep(3) #to diffrentiate the color changes


# print(ogstoreboard)

# exec(open("endAni.py").read())


def mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset):
    os.system("clear")

    replayfile = open("savereplay.txt").read()
    indexx = replayfile.find(Key)
    while indexx != -1:
        if indexx == -1:
            pass
        else:
            Key = key(6)

    # Welcome message
    print("Welcome to ASCII Chess! \n")
    print("================\nMenu:\n1. Start Game (Multiplayer)\n2. Start Singleplayer (Vs AI)\n3. Play Replay\n4. Rules\n5. Settings\n6. Exit\n================\n")
    start = input("What would you like to do?\n")
    start = start.lower()

    # Start Menu

    if start == "1" or start == "start game":
        print("")
        savefile = open("savereplay.txt", "a")
        savefile.write(Key)
        savefile.close()
        savefile = open("savenotation.txt", "a")
        savefile.write(Key)
        savefile.close()
        whitepersp(whitecolor, blackcolor, board)
        movepiece(board, storeboard, whitemove, whitecolor, blackcolor)

    elif start == "2" or start == "start singleplayer":
        print("")
        savefile = open("savereplay.txt", "a")
        savefile.write(Key)
        savefile.close()
        savefile = open("savenotation.txt", "a")
        savefile.write(Key)
        savefile.close()
        whitepersp(whitecolor, blackcolor, board)
        aimovepiece(board, storeboard, whitemove, whitecolor, blackcolor, 2, False)

    elif start == "3" or start == "play replay":
        replaygame()

    elif start == "4" or start == "rules":
        file = open("zzzrules.txt").read()
        print("\n" + file + "\n")
        exit = input("Type exit to return to the menu\n")
        exit = exit.lower()
        while not exited:
            if exit == "exit":
                print("")
                mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)
            else:
                print("Please enter a valid response\n")
            exit = input("Type exit to return to the menu\n")
            exit = exit.lower()

    elif start == "5" or start == "settings":
        indexerthing = 0
        settingmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)
        for letter in colorsets:
            indexerthing += 1
            if letter == "!":
                break
        whitecolor = colorsets[:indexerthing - 1]
        blackcolor = colorsets[indexerthing:]
        mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)

    elif start == "6" or start == "exit":
        print("\nwow rude")

    else:
        print("Please type a valid choice. \n")
        mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)


if __name__ == '__main__':
    menuAni()
    mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)
