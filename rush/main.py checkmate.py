# var
PPos = ""
BPos = ""
RPos = ""
QPos = ""
KPos = ""
boardArr = [[]]

def checkmate(board):
    global boardArr
    boardArr = board2arr(board)

    ## check valid row and column
    if (len(boardArr) < 4):
        print("Check >> Board at least 4 rows") 
        return
    
    if (len(boardArr[0]) < 4):
        print("Check >> Board at least 4 columns") 
        return
    
    boardColumn = len(boardArr[0])
    for row in boardArr:
        if (boardColumn != (len(row))):
            print("Check >> Columns each row must be the same length")
            return
        
        ## checkmate ##
    if PPos != "" and PKillZone(PPos):
        print("Success, Checkmate by Pawn")
    elif BPos != "" and BKillZone(BPos):
        print("Success, Checkmate by Bishop")
    elif RPos != "" and RKillZone(RPos):
        print("Success, Checkmate by Rook")
    elif QPos != "" and (BKillZone(QPos) or RKillZone(QPos)):
        print("Success, Checkmate by Queen")
    else:
        print("...Fail...")

def getPosition(ItemPos,XY):
    if XY == "X" or XY == "x":
        return ItemPos.split(',')[0]
    else:
        return ItemPos.split(',')[1]
    
def isValidZone(killzoneX, killzoneY):
    if killzoneX >= 0 and killzoneX <= (len(boardArr[1])-1) and killzoneY >= 0 and killzoneY <= (len(boardArr[1])-1):
        return True
    else:
        return False
    
def isBKill(X, Y):

    if isValidZone(X, Y):
        if (boardArr[X][Y] == "K"):
            return True

    return False

def BKillZone(Pos):
    PosX = getPosition(Pos, "X")
    PosY = getPosition(Pos, "Y")

    killzone = []
    
    tempX = int(PosX) - 1
    tempY = int(PosY) - 1
    while tempX >= 0 and tempY >=0:
        if isBKill(tempX, tempY): return True;
        tempX -= 1
        tempY -= 1

    ############################

    tempX = int(PosX) + 1
    tempY = int(PosY) - 1
    while tempX <= (len(boardArr[0])-1) and tempY >= 0:
        if isBKill(tempX, tempY): return True;
        tempX += 1
        tempY -= 1

    ############################

    tempX = int(PosX) - 1
    tempY = int(PosY) + 1
    while tempY <= (len(boardArr[0])-1) and tempX >= 0:
        if isBKill(tempX, tempY): return True;
        tempX -= 1
        tempY += 1

    ############################

    tempX = int(PosX) + 1
    tempY = int(PosY) + 1
    while tempX <= (len(boardArr[0])-1) and tempY <= (len(boardArr[0])-1):
        if isBKill(tempX, tempY): return True;
        tempX += 1
        tempY += 1
    
    return False

def RKillZone(Pos):
    PosX = getPosition(Pos, "X")
    PosY = getPosition(Pos, "Y")

    isCheckmate = False

    for x in range(0, len(boardArr[1])-1):
        if boardArr[int(PosX)][x] == "K":
            isCheckmate = True
            break
        
    for y in range(0, len(boardArr[1])-1):
        if boardArr[y][int(PosY)] == "K":
            isCheckmate = True
            break
    
    return isCheckmate
      
def PKillZone(Pos):
    PosX = getPosition(Pos,"X")
    PosY = getPosition(Pos,"Y")

    X = int(PosX) - 1;
    Y1 = int(PosY) - 1;
    Y2 = int(PosY) + 1;
    if isValidZone(X, Y1) and isValidZone(X, Y2):
        if (boardArr[X][Y1] == "K") or (boardArr[X][Y2] == "K"):
            return True
        
    return False

def board2arr(board):
    boardList = list(board)

    row = 0
    column = 0
    result = [[]]
    for item in boardList:
        if (item == "\n"):
            result.append([])
            row +=1
            column = 0
        else:
            currentPos = str(row) + "," + str(column)
            
            if (item == "P"):
                global PPos
                PPos = currentPos
            elif (item == "B"):
                global BPos
                BPos = currentPos
            elif (item == "R"):
                global RPos
                RPos = currentPos
            elif (item == "Q"):
                global QPos
                QPos = currentPos
            elif (item == "K"):
                global KPos
                KPos = currentPos
                
            result[row].append(item)
            column += 1
   
    return result

def main():
    board = """\
......
......
......
...K..
...P..
......\
"""
    checkmate(board)

if __name__ == "__main__":
    main()