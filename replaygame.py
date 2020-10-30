import math
from main import *
from zwhitepersp import *
from zblackpersp import *

# Read the replayfile
replayfile = open("savereplay.txt").read()

# Defining Variables
currentletter = ""
currentmove = ""
currentcounter = 0
repersp = "white"
turncounter = 0
lastturn = False
autoplay = False


# Turn printing function
def turnprint(currentcounter):
    turn = currentcounter / 10
    turn = math.floor(turn + 1)
    strturn = str(int(turn))
    if currentcounter % 2 == 0:
        global turnprintx
        turnprintx = "\nNext Turn: " + strturn + " Black\n\n"
        print("\nNext Turn: " + strturn + " Black")
    else:
        global turnprint
        turnprintx = "\nNext Turn: " + strturn + " White\n"
        print("\nNext Turn: " + strturn + " White")


Keylist = ["A", "B", "C", "D", "E", "F"]
Keycheck = ""
Keychecked = False
indexing = -1
# Checking the Key
# index = replayfile.find(Key)
Key = input("\nWhat is your game key?\n")

if len(Key) != 6:
    print("Please enter a valid game key.\n")
    mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)

for letter in replayfile:
    indexing += 1
    Keylist.pop(0)
    Keylist.append(replayfile[indexing])
    for keything in Keylist:
        Keycheck = Keylist[0] + Keylist[1] + Keylist[2] + Keylist[3] + Keylist[4] + Keylist[5]
    if Keycheck == Key:
        index = indexing + 1
        Keychecked = True
        replaying = True
        break
    else:
        Keycheck = ""

if not Keychecked:
    print("Please enter a valid game key.\n")
    mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)

print("\nNext Turn: 1 White\n\n")
whitepersp(whitecolor, blackcolor,board)

while lastturn == False:
    if autoplay == False:
        forward = input(
            "\nType 'n' or 'next' to continue, 'f' or 'flip' to change perspectives, 'e' or 'exit' to exit, 'a #' or 'auto #' to automatically play the rest of the game, with each move being made at the specified interval of time.\n")
        forward = forward.lower()
    else:
        forward = "n"
        time.sleep(autotimer)
    # Code for moving through replay by user input
    if forward == "e" or forward == "exit":
        break

    elif forward == "f" or forward == "flip":
        #os.system("clear")
        print(turnprintx)
        if repersp == "white":
            repersp = "black"
            blackpersp(whitecolor, blackcolor, board)
        elif repersp == "black":
            repersp = "white"
            print("")
            whitepersp(whitecolor, blackcolor, board)

    elif forward == "n" or forward == "next" and lastturn == False:
        #os.system("clear")
        turnprint(currentcounter)
        for i in range(5):
            if currentletter != "#":
                currentletter = replayfile[currentcounter + index]
                currentmove = currentmove + currentletter
                currentcounter += 1
            else:
                lastturn = True
                currentletter = replayfile[currentcounter + index]
                currentmove = currentmove + currentletter
                currentcounter += 1

        if currentmove != "0-0B " and currentmove != "0-0-B" and currentmove != "0-0W " and currentmove != "0-0-W" and currentmove != "#W   " and currentmove != "#B   ":
            board[currentmove[3:5]] = board[currentmove[0:2]]
            board[currentmove[0:2]] = "  "
            currentmove = ""
        elif currentmove == "0-0W ":
            board["e1"] = '  '
            board["f1"] = 'WR'
            board["g1"] = 'WK'
            board["h1"] = '  '
            currentmove = ""
        elif currentmove == "0-0B ":
            board["e8"] = '  '
            board["f8"] = 'BR'
            board["g8"] = 'BK'
            board["h8"] = '  '
            currentmove = ""
        elif currentmove == "0-0-W":
            board["a1"] = '  '
            board["b1"] = '  '
            board["c1"] = 'WK'
            board["d1"] = 'WR'
            board["e1"] = '  '
            currentmove = ""
        elif currentmove == "0-0-B":
            board["a8"] = '  '
            board["b8"] = '  '
            board["c8"] = 'BK'
            board["d8"] = 'BR'
            board["e8"] = '  '
            currentmove = ""

        if currentmove == "#W   ":
            print("\n\nGG, White won!")
        elif currentmove == "#B   ":
            print("\n\nGG, Black won!")

        if repersp == "white":
            print("\n")
            whitepersp(whitecolor, blackcolor, board)
        elif repersp == "black":
            print("\n")
            blackpersp(whitecolor, blackcolor, board)

    elif len(forward) >= 2 and forward[0] == "a" and forward[1] == " ":
        try:
            autotimer = int(forward[2:])
            autoplay = True
        except:
            print("Please enter a valid time value")

    elif len(forward) >= 5 and forward[0:4] == "auto" and forward[4] == " ":
        try:
            autotimer = int(forward[5:])
            autoplay = True
        except:
            print("Please enter a valid time value")

    else:
        print("please input a valid response")

mainmenu(Key, key, replaying, exited, settingexit, whitecolor, blackcolor, colorset)
