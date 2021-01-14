import os

def blackpersp(whitecolor, blackcolor, board):
    os.system("clear")
    testvar1 = "hi"
    testvar2 = "bye"
    testvar3 = -1
    text = ["BR", "BN", "BB", "BQ", "BK", "bp", "WR", "WN", "WB", "WQ", "WK", "wp"]
    piece = ["♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ ", "♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ "]
    colors = {"pink": u"\u001B[31m", "neon green": u"\u001B[32m", "orange": u"\u001B[33m", "blue": u"\u001B[34m",
              "purple": u"\u001B[35m", "lighter blue": u"\u001B[36m", "red": u"\u001B[91m", "green": u"\u001B[92m",
              "orange yellow": u"\u001B[93m", "lavender": u"\u001B[95m", "electric blue": u"\u001B[96m"}
    # Define lists to reorder
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []

    # Appending dictionary to lists to reorder
    for i in board:  # for every space in board
        row = int(i[1])  # row is row number
        row = 9 - row  # rows are reversed
        column = (i[0])
        if row == 1:
            list1.insert(0, board[i][
                            0:2])  # list1 would now be [board[a8]] cuz that was inserted, and would add the rest each time it iterates thru
        elif row == 2:
            list2.insert(0, board[i][0:2])
        elif row == 3:
            list3.insert(0, board[i][0:2])
        elif row == 4:
            list4.insert(0, board[i][0:2])
        elif row == 5:
            list5.insert(0, board[i][0:2])
        elif row == 6:
            list6.insert(0, board[i][0:2])
        elif row == 7:
            list7.insert(0, board[i][0:2])
        elif row == 8:
            list8.insert(0, board[i][0:2])

    # Add lists together to create the full board
    blackpersp = list8 + list7 + list6 + list5 + list4 + list3 + list2 + list1
    # Paste the full board in the correct format
    yaxis = 1
    print("")
    for y in range(64):
        x = y + 1
        testvar1 = blackpersp[y]  # this is the piece name
        for t in text:  # this is iterating through the list of piece names
            if blackpersp[y] == '  ':
                testvar2 = '  '
                break
            testvar3 += 1  # this is keeping track of the index of where in the list it is
            if t == testvar1:  # testing if piece name in list is same as the piece name intended
                testvar2 = piece[testvar3]  # string for the piece name is set to the piece character
                testvar3 = -1  # this resets the counter
                break  # this exists the forloop so it moves to the next one
        if testvar1[0].lower() == "w":
            print(end=colors[whitecolor])
        elif testvar1[0].lower() == "b":
            print(end=colors[blackcolor])
        else:
            print(end=u"\u001B[0m")

        if x % 8 == 0:
            if (yaxis) % 2 == 0:
                print(u"\u001B[107m", testvar2, u"\u001B[0m" + " ", str(round(
                    x / 8)))  # color switch white, space, testvar2, space, color switch black, space, space, row, enter
            else:
                print(testvar2 + u"\u001B[0m", " ", str(round(x / 8)))  # testvar2, space, space, row, enter
            if x != 64:
                print("----|----|----|----|----|----|----|----")  # add spacing
                if ((x % 8) + yaxis) % 2 == 1:
                    print(end=" ")  # formatting
            else:
                print("\n", " h    g    f    e    d    c    b    a")
            yaxis += 1
        else:
            if ((x % 8) + yaxis) % 2 == 0:
                print(u"\u001B[107m", testvar2, u"\u001B[0m",
                      end="| ")  # color switch white, space, testvar2, space, color switch black, space, |, space
            else:
                print(testvar2 + u"\u001B[0m", end=" |")
    print("\n")
