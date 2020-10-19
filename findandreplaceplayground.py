
  #up and to the right
  if up != 0 and right != 0:
    if up > right:
      displacement = right
    elif up < right:
      displacement = up
    else:
      displacement = right
    for i in range(1,displacement+1):
      if board[chr(ord(file)+i) + str(rank+i)].lower() != '  ':
        if board[chr(ord(file)+i) + str(rank+i)][0].lower() == 'b':
          break
        elif board[chr(ord(file)+i) + str(rank+i)][0].lower() == 'w':
          storeboard[chr(ord(file)+i) + str(rank+i)].append(piece)
          break
      else:
        storeboard[chr(ord(file)+i) + str(rank+i)].append(piece)
  #down and to the right
  if down != 0 and right != 0:
    if down > right:
      displacement = right
    elif down < right:
      displacement = down
    else:
      displacement = right
    for i in range(1,displacement+1):
      if board[chr(ord(file)+i) + str(rank-i)].lower() != '  ':
        if board[chr(ord(file)+i) + str(rank-i)][0].lower() == 'b':
          break
        elif board[chr(ord(file)+i) + str(rank-i)][0].lower() == 'w':
          storeboard[chr(ord(file)+i) + str(rank-i)].append(piece)
          break
      else:
        storeboard[chr(ord(file)+i) + str(rank-i)].append(piece)