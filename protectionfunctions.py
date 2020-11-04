#
def wpawnprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == 'w':
            protdict[board[chr(ord(file) + 1) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == 'w':
            protdict[board[chr(ord(file) - 1) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def bpawnprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == 'b':
            protdict[board[chr(ord(file) + 1) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == 'b':
            protdict[board[chr(ord(file) - 1) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def knightprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 1) + str(rank + 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 1) + str(rank + 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 1) + str(rank - 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 1) + str(rank - 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 2) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 2) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 2) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 2) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def wrookprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    return protdict


def brookprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    return protdict


def wbishopprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)

    return protdict


def bbishopprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


def wqueenprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


def bqueenprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


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