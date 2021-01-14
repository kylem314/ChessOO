import os

def whitepersp(whitecolor,blackcolor,board):
  os.system("clear")
  testvar1 = "hi"
  testvar2 = "bye"
  testvar3 = -1
  text = ["BR", "BN", "BB", "BQ", "BK", "bp", "WR", "WN", "WB", "WQ", "WK", "wp"]
  piece = ["♜ ","♞ ","♝ ","♛ ","♚ ","♟ ","♜ ","♞ ","♝ ","♛ ","♚ ","♟ "]
  colors = {"pink":u"\u001B[31m", "neon green":u"\u001B[32m","orange":u"\u001B[33m", "blue":u"\u001B[34m", "purple":u"\u001B[35m", "lighter blue":u"\u001B[36m", "red":u"\u001B[91m", "green":u"\u001B[92m", "orange yellow":u"\u001B[93m", "lavender":u"\u001B[95m", "electric blue":u"\u001B[96m"}
  for i in board:
    string = str(i) #so this is the letter representation of space
    row = int(string[1]) #this is the num of space
    column = (string[0]) #this is the letter of space
    testvar1 = board[i][0:2] # this is the piece name
    for t in text: # this is iterating through the list of piece names
      if testvar1 == '  ': 
        testvar2 = '  '
        break
      testvar3 += 1 # this is keeping track of the index of where in the list it is
      if t == testvar1: # this is checking if the piece name in the list is the same as the piece name it should be
        testvar2 = piece[testvar3]  # when it finds the right one, the string for the piece name is set to the piece character
        testvar3 = -1 # this resets the counter
        break # this exists the forloop so it moves to the next one
    
    if testvar1[0].lower() == "w":
      print(end = colors[whitecolor])
    elif testvar1[0].lower() == "b":
      print(end = colors[blackcolor])
    else:
      print(end = u"\u001B[0m")
    if column != "h": # if it isn't the last column,
      if (ord(i[0]) + int(i[1]) - 96) % 2 == 1:
        print(u"\u001B[107m", testvar2, u"\u001B[0m", end = "| ") #color switch white, space, testvar2, space, color switch black, space, |, space
      else:
        print(testvar2 + u"\u001B[0m", end = " |")
    elif column == "h": # if it is the last column,
      if (ord(i[0]) + int(i[1]) - 96) % 2 == 1:
        print(u"\u001B[107m", testvar2, u"\u001B[0m" + " ", str(row) + u"\u001B[0m") #color switch white, space, testvar2, space, color switch black, space, space, row, enter
      else:
        print(testvar2 + u"\u001B[0m", " ", str(row)) #testvar2, space, space, row, enter
      if row != 1: # if it isn't the bottom row
        print("----|----|----|----|----|----|----|----") # add spacing
        if (ord(i[0]) + int(i[1]) - 96) % 2 == 0:
          print(end = " ") # formatting
        

      else: # if it is the last row
        print("\n","a    b    c    d    e    f    g    h") # print row names
  print("\n") # formatting


#notes: 31 pink, 32 green, 33 orange, 34 darkest blue, 35 purple, 36 lighter but not light blue, 91 red, 92 slightly less neon green, 93 orangey yellow, 94 blue, 95 lavender, 96 electric blue