def wpcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
  for i in storeboard[attackingpos]: # checks for pieces that can move to 
    if i[0].upper() == whitemove:
      storeboard1[attackingpos].append(i)
  for i in storeboard.values():
    if king in i and i != attackingpos:
      try:
        for k in i:
          if k[0].upper() == whitemove:
            raise Exception("exception")
        storeboard1[i].append(king)
        checkmate = False
      except Exception:
        pass
  print("white pawn")
  return storeboard1


def bpcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    print("black pawn")


def Bcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    print("bishop")


def Ncheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    print("knight")


def Rcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    print("rook")


def Qcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    print("queen")
