# ╔ ╗ ╚ ╝ ╠ ╣ ╬ ═ ║ ╦ ╩
# ⬤

import random
import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

board = [[]]

def doTests():
    global board

    # BLOCK TESTS
    # HORIZONTAL TESTS
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'R', 'R', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 3

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', ' ', 'R', 'R', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'R', ' ', 'R', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 2

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'R', ' ', 'R', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == -1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'R', ' ', 'R', ' ', ' ', ' '], [' ', ' ', 'Y', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 2

    # VERTICAL TESTS

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', ' ', ' ', ' ', ' ', ' ', ' '], ['R', ' ', ' ', ' ', ' ', ' ', ' '], ['R', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 0

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'R'], [' ', ' ', ' ', ' ', ' ', ' ', 'R'], [' ', ' ', ' ', ' ', ' ', ' ', 'R']]
    assert checkIfCanBlockWin() == 6

    # DIAGONAL TESTS

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'R', 'Y', ' ', ' ', ' '], [' ', 'R', ' ', ' ', ' ', ' ', ' '], ['R', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 3

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'R', ' ', ' ', ' '], [' ', ' ', 'R', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'Y', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'R', ' ', ' ', ' ', ' '], [' ', 'R', ' ', ' ', ' ', ' ', ' '], ['R', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == -1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'R', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'R', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'R', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == 0

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'R', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'R', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'R', ' ', ' ', ' ']]
    assert checkIfCanBlockWin() == -1

    # WIN TESTS
    # HORIZONTAL TESTS
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'Y', 'Y', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == 3

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', 'Y', 'Y', ' ', ' ', ' ']]
    assert checkIfCanWin() == 1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'Y', ' ', 'Y', ' ', ' ', ' ']]
    assert checkIfCanWin() == 2

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'Y', ' ', 'Y', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == -1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'Y', ' ', 'Y', ' ', ' ', ' '], [' ', ' ', 'R', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == 2

    # VERTICAL TESTS

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == 0

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'Y'], [' ', ' ', ' ', ' ', ' ', ' ', 'Y'], [' ', ' ', ' ', ' ', ' ', ' ', 'Y']]
    assert checkIfCanWin() == 6

    # DIAGONAL TESTS

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'Y', 'R', ' ', ' ', ' '], [' ', 'Y', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == 3

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'Y', ' ', ' ', ' '], [' ', ' ', 'Y', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['Y', 'R', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == 1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'Y', ' ', ' ', ' ', ' '], [' ', 'Y', ' ', ' ', ' ', ' ', ' '], ['Y', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert checkIfCanWin() == -1

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], ['R', 'Y', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'Y', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'Y', ' ', ' ', ' ']]
    assert checkIfCanWin() == 0

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'Y', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'Y', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'Y', ' ', ' ', ' ']]
    assert checkIfCanWin() == -1

    print("ALL TESTS PASSED")

def initBoard():
    global board
    board = []
    for i in range(6):
        row = []
        for j in range (7):
            row.append(" ")
        board.append(row)

#print(board)
# [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

R = bcolors.FAIL + "⬤" + bcolors.ENDC
Y = bcolors.WARNING + "⬤" + bcolors.ENDC
R_GREEN = bcolors.FAIL + "⬤" + bcolors.OKGREEN
Y_GREEN = bcolors.WARNING + "⬤" + bcolors.OKGREEN

def printBoard_OLD():
    print("")
    print("   0      1      2      3      4      5      6")
    print("╔══════╦══════╦══════╦══════╦══════╦══════╦══════╗")
    for y in range(6):
        #print(y, end='')
        for c in range(7): print("║ ", Y if board[y][c]=="Y" else (R if board[y][c]=="R" else " "), "  ", end = '')
        print("║ {0}".format(y))
        #print("║ ", board[0][y], " ║ ", board[1][y], " ║ ", board[2][y], " ║")
        if y != 5:  print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        else:       print("╚══════╩══════╩══════╩══════╩══════╩══════╩══════╝\n")
    return

def printBoard():
    boardString = "\n"
    print("")
    boardString = boardString + ("   0      1      2      3      4      5      6\n")
    boardString = boardString + ("╔══════╦══════╦══════╦══════╦══════╦══════╦══════╗\n")
    for y in range(6):
        #print(y, end='')
        for c in range(7): 
            if board[y][c] == "Y": boardString = boardString + ("║  {0}   ".format(Y))
            elif board[y][c] == "R": boardString = boardString + ("║  {0}   ".format(R))
            else: boardString = boardString + ("║      ")
            #boardString = boardString + ("║ ", Y if board[y][c]=="Y" else (R if board[y][c]=="R" else " "), "  ")
        boardString = boardString + ("║ {0}\n".format(y))
        #print("║ ", board[0][y], " ║ ", board[1][y], " ║ ", board[2][y], " ║")
        if y != 5:  boardString = boardString + ("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╣\n")
        else:       boardString = boardString + ("╚══════╩══════╩══════╩══════╩══════╩══════╩══════╝\n")
    print(boardString)
    return

def animateCounter(RY, r, col):
    for i in range(r):
        board[i][col] = RY
        cls()
        print()
        printBoard()
        time.sleep(0.1)
        board[i][col] = " "
    return

def dropCounter(RY, col):
    dropped = False
    r = 5
    while (not dropped and r >= 0): 
        if board[r][col] == " ":
            dropped = True
            #animateCounter(RY, r, col)
            board[r][col] = RY
        else: r=r-1

def checkVerticals():
    #if board[0][0] == board[0][1] == board[0][2]: return board[0][0]
    #elif board[1][0] == board[1][1] == board[1][2]: return board[1][0]
    #elif board[2][0] == board[2][1] == board[2][2]: return board[2][0]
    #else: return "_"
    for c in range (7):
        for r in range (3):
            if (board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]) and board[r][c] != " ": return board[r][c]
    return "_"

def checkHorizontals():
    #if board[0][0] == board[1][0] == board[2][0]: return board[0][0]
    #elif board[0][1] == board[1][1] == board[2][1]: return board[1][0]
    #elif board[0][2] == board[1][2] == board[2][2]: return board[2][0]
    #else: return "_"
    for r in range (6):
        for c in range (4):
            if (board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]) and board[r][c] != " ": return board[r][c]
    return "_"

def checkDiagonals():
    #if board[0][0] == board[1][1] == board[2][2]: return board[1][1]
    #elif board[0][2] == board[1][1] == board[2][0]: return board[1][1]
    #else: return "_"
    for c in range(4):
        for r in range(3):
            if (board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]) and board[r][c] != " ": return board[r][c]

    for c in range(4):
        for r in range(3):
            r = 5-r
            #if True: True
            if (board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]) and board[r][c] != " ": return board[r][c]
    return "_"

def checkDraw():
    T = True
    for r in range(6):
        for c in range(7):
            T = T and (board[r][c] == "R" or board[r][c] == "Y")
    return T

def checkEnd():
    H = checkHorizontals()
    V = checkVerticals()
    D = checkDiagonals()
    
    if H == "R" or V == "R" or D == "R":
        print(bcolors.OKGREEN + "Player 2 (",R_GREEN," ) wins!" + bcolors.ENDC)
        return "R"
    elif H == "Y" or V == "Y" or D == "Y":
        print(bcolors.OKGREEN + "Player 1 (",Y_GREEN," ) wins!" + bcolors.ENDC)
        return "Y"
    elif checkDraw(): 
        print(bcolors.WARNING + "It's a draw!" + bcolors.ENDC)
        return "D"
    else:
        return "_"

def getMove():
    valid = False
    while not valid:
        try:
            col = int(input("Enter column to play: "))
            #x = (cell-1) % 3
            #y = (cell-1) // 3
            if board[0][col] != " ":
                print(bcolors.FAIL + "Invalid move - column full" + bcolors.ENDC)
            elif 0 <= col <= 6:
                valid = True
            else:
                print(bcolors.FAIL + "Invalid entry. Try again" + bcolors.ENDC)
        except KeyboardInterrupt:
            raise
        except:
            print(bcolors.FAIL + "Invalid entry. Try again" + bcolors.ENDC)
    return col

def checkVerticalsForWin():
    for c in range (7):
        for r in range (3):
            if ((board[r+3][c] == board[r+1][c] == board[r+2][c]) and board[r+1][c] == "Y") and board[r][c] == " ": return c,2

    for c in range (7):
        for r in range (3):
            if ((board[r+2][c] == board[r+3][c]) and board[r+2][c] == "Y") and board[r+1][c] == " ": return c,1
            
    return -1,0

def checkHorizontalsForWin():
    for r in range (6):
        for c in range (4):
            cells = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                elif a == " ": c_drop = c + cells.index(a)
            if ys == 3 and rs == 0:
                #print("3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                if (r == 5): return c_drop,2
                elif (board[r+1][c_drop] != " "): return c_drop,2

    for r in range (6):
        for c in range (4):
            cells = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if ys == 2 and rs == 0:
                #print("2 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                if (r == 5): return c_drop,1
                elif (board[r+1][c_drop] != " "): return c_drop,1
            #if rs == 2 and board[r+1][c] != " ": return c_drop

    return -1,0

def checkDiagonalsForWin():
    for c in range(4):
        for r in range(3):
            cells = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if ys == 3 and rs == 0:
                diff = c_drop - c
                r_new = r+diff
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if ys == 3 and rs == 0:
                diff = c_drop - c
                r_new = r-diff
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2

    for c in range(4):
        for r in range(3):
            cells = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if ys == 2 and rs <= 1:
                diff = c_drop - c
                r_new = r+diff
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if ys == 2 and rs <= 1:
                diff = c_drop - c
                r_new = r-diff
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2
    return -1,0

def _checkDiagonalsForWin(): # OLD
    for c in range(4):
        for r in range(3):
            cells = {board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]}
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "Y": ys = ys + 1
                if a == " " and c_drop == -1: c_drop = c
            if ys == 3 and board[r+1][c] == " ": return c_drop,2

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = {board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]}
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "Y": ys = ys + 1
                if a == " " and c_drop == -1: c_drop = c
            if ys == 3 and board[r+1][c] == " ": return c_drop,2

    for c in range(4):
        for r in range(3):
            cells = {board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]}
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "Y": ys = ys + 1
                if a == " " and c_drop == -1: c_drop = c
            if ys == 2 and board[r+1][c] == " ": return c_drop,1

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = {board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]}
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "Y": ys = ys + 1
                if a == " " and c_drop == -1: c_drop = c
            if ys == 2 and board[r+1][c] == " ": return c_drop,1
    return -1,0

def checkVerticalsForBlock():
    for c in range (7):
        for r in range (3):
            if ((board[r+3][c] == board[r+1][c] == board[r+2][c]) and board[r+1][c] == "R") and board[r][c] == " ": return c,2

    for c in range (7):
        for r in range (3):
            if ((board[r+2][c] == board[r+3][c]) and board[r+2][c] == "R") and board[r+1][c] == " ": return c,1
            
    return -1,0

def checkHorizontalsForBlock():
    for r in range (6):
        for c in range (4):
            cells = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                elif a == " ": c_drop = c + cells.index(a)
            if rs == 3 and ys == 0:
                #print("3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                if (r == 5): return c_drop,2
                elif (board[r+1][c_drop] != " "): return c_drop,2

    for r in range (6):
        for c in range (4):
            cells = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            if rs == 2 and ys == 0:
                #print("2 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                if (r == 5): return c_drop,1
                elif (board[r+1][c_drop] != " "): return c_drop,1
            #if rs == 2 and board[r+1][c] != " ": return c_drop

    return -1,0

def checkDiagonalsForBlock():
    for c in range(4):
        for r in range(3):
            cells = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
            #print("CHECKING: {0},{1} : {2},{3} : {4},{5} : {6},{7}".format(r,c,r+1,c+1,r+2,c+2,r+3,c+3))
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            #print("RS: {0}".format(rs))
            if rs == 3 and ys == 0:
                #print("diagonal 3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                diff = c_drop - c
                #print("0.diff = {0}".format(diff))
                r_new = r+diff
                #print("0.r_new = {0}".format(r_new))
                #print("checking: {0},{1}".format(r_new+1,c_drop))
                #print("'{0}'".format(board[r_new+1][c_drop]))
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2
            #if rs == 3 and board[r+1][c] != " ": 
            #    print("diagonal 3 in 4 detected starting at c = {0}".format(c))
            #    print("c_drop should be {0}".format(c_drop))
            #    return c_drop,2

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
            #print("CHECKING: {0},{1} : {2},{3} : {4},{5} : {6},{7}".format(r,c,r-1,c+1,r-2,c+2,r-3,c+3))
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            #print("RS: {0}".format(rs))
            if rs == 3 and ys == 0:
                #print("diagonal 3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                diff = c_drop - c
                r_new = r-diff
                #print("1.r_new = {0}".format(r_new))
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2
            #if rs == 3 and board[r+1][c] != " ": 
            #    print("diagonal 3 in 4 detected starting at c = {0}".format(c))
            #    print("c_drop should be {0}".format(c_drop))
            #    return c_drop,2

    for c in range(4):
        for r in range(3):
            cells = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
            #print("CHECKING: {0},{1} : {2},{3} : {4},{5} : {6},{7}".format(r,c,r+1,c+1,r+2,c+2,r+3,c+3))
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            #print("RS: {0}".format(rs))
            if rs == 2 and ys <= 1:
                #print("diagonal 3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                diff = c_drop - c
                r_new = r+diff
                #print("2.r_new = {0}".format(r_new))
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2
            #if rs == 2 and board[r+1][c] != " ": 
            #    print("diagonal 2 in 4 detected starting at c = {0}".format(c))
            #    print("c_drop should be {0}".format(c_drop))
            #    return c_drop,1

    for c in range(4):
        for r in range(3):
            r = 5-r
            cells = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
            #print("CHECKING: {0},{1} : {2},{3} : {4},{5} : {6},{7}".format(r,c,r-1,c+1,r-2,c+2,r-3,c+3))
            rs = 0
            ys = 0
            c_drop = -1
            for a in cells: 
                if a == "R": rs = rs + 1
                if a == "Y": ys = ys + 1
                if a == " ": c_drop = c + cells.index(a)
            #print("RS: {0}".format(rs))
            if rs == 2 and ys <= 1:
                #print("diagonal 3 in 4 detected starting at c = {0}".format(c))
                #print("c_drop should be {0}".format(c_drop))
                diff = c_drop - c
                r_new = r-diff
                #print("3.r_new = {0}".format(r_new))
                if r_new == 5: return c_drop,2
                elif board[r_new+1][c_drop] in ["R","Y"]: return c_drop,2
            #if rs == 2 and board[r+1][c] != " ": 
            #    print("diagonal 2 in 4 detected starting at c = {0}".format(c))
            #    print("c_drop should be {0}".format(c_drop))
            #    return c_drop,1
    return -1,0

def checkIfCanWin():
    v, vp = checkVerticalsForWin() # Unknown, but likely not working
    h, hp = checkHorizontalsForWin() # Unknown, but likely not working
    d, dp = checkDiagonalsForWin() # Unknown, but likely not working
    #print("WINS: v = {0}, h = {1}, d = {2}".format(v,h,d))
    if vp == 2: return v
    elif hp == 2: return h
    elif dp == 2: return d
    elif vp == 1: return v
    elif hp == 1: return h
    elif dp == 1: return d
    else: return -1

def checkIfCanBlockWin():
    v, vp = checkVerticalsForBlock() # This WORKS
    h, hp = checkHorizontalsForBlock() # This WORKS (but doesnt always pick the correct cell to drop to best block)
    d, dp = checkDiagonalsForBlock() # Not working
    #print("BLOCK: v = {0}, h = {1}, d = {2}".format(v,h,d))
    m = max(vp, hp, dp)
    if vp == 2: return v
    elif hp == 2: return h
    elif dp == 2: return d
    elif vp == 1: return v
    elif hp == 1: return h
    elif dp == 1: return d
    else: return -1
    #if v != -1: return v
    #elif h != -1: return h
    #elif d != -1: return d

def checkCloseToWin():
    # TODO
    return -1

def makeOtherMove():
    c = random.randint(0,6)
    return c

def doAI():
    # TODO
    canwin = checkIfCanWin()
    canblock = checkIfCanBlockWin()
    #closewin = checkCloseToWin()
    other = makeOtherMove()
    #print("TOTALS: canwin = {0}, canblock = {1}, other = {2}".format(canwin, canblock, other))
    col = -1
    if canwin != -1: col = canwin
    elif canblock != -1: col = canblock
    #elif closewin != -1: col = closewin
    else: col = other
    dropCounter("Y", col)

def play():
    #for r in range(3): print(5-r)
    #print("?")
    doTests()
    initBoard()
    printBoard()
    player1 = True
    end = False
    print("P1 is ",R,", P2 is ",Y,"\n")
    while not end:
        if player1:
            print("P1's Turn (",R," ):")
            col = getMove()
            dropCounter("R", col)
            player1 = False
        else:
            #print("P2's Turn (",Y," ):")
            #col = getMove()
            #dropCounter("Y", col)
            doAI()
            player1 = True
        
        cls()
        print()
        printBoard()
        if checkEnd() != "_": 
            end = True

play()