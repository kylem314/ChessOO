#
def wpawn(board, storeboard, piece, file, rank):
    if board[file + str(rank + 1)].lower() == '  ':
        storeboard[file + str(rank + 1)].append(piece)
        if rank == 2:
            if board[file + str(rank + 2)].lower() == '  ':
                storeboard[file + str(rank + 2)].append(piece)
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bpawn(board, storeboard, piece, file, rank):
    if board[file + str(rank - 1)].lower() == '  ':
        storeboard[file + str(rank - 1)].append(piece)
        if rank == 7:
            if board[file + str(rank - 2)].lower() == '  ':
                storeboard[file + str(rank - 2)].append(piece)
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def wknight(board, storeboard, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bknight(board, storeboard, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def wrook(board, storeboard, piece, file, rank):
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
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    return storeboard


def brook(board, storeboard, piece, file, rank):
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
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    return storeboard


def wbishop(board, storeboard, piece, file, rank):
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
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def bbishop(board, storeboard, piece, file, rank):
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
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def wqueen(board, storeboard, piece, file, rank):
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
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def bqueen(board, storeboard, piece, file, rank):
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
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
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
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def wking(board, storeboard, piece, file, rank):
    try:
        if board[file + str(rank + 1)][0].lower() != 'w':
            storeboard[file + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() != 'w':
            storeboard[file + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bking(board, storeboard, piece, file, rank):
    try:
        if board[file + str(rank + 1)][0].lower() != 'b':
            storeboard[file + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() != 'b':
            storeboard[file + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard
