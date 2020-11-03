def wpcheck(kingpos, attackingpos, storeboard, storeboard1, whitemove, king):
    if king in storeboard[attackingpos]:
        pass

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
    print("white pawn")


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
