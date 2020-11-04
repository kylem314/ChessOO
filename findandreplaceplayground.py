
def kingprot(board, protdict, piece, file, rank, storeboard):
    try:
        if board[file + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[file + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[file + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[file + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[file + str(rank - 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank - 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank - 1)]].append(piece)
    except Exception:
        pass
    return protdict