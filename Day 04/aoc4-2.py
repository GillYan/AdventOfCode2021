f = open("input.txt", "r")
board = []
slowest = 0
score = 0
last = 0

def getBoard():
    for x in range(5):
        temp = f.readline().split()
        #skip blank line
        if len(temp) == 0:
            temp = f.readline().split()

        temp[-1] = temp[-1].rstrip()
        board.append(temp)

def checkBoard():
    product = 1
    c1 = 1
    c2 = 1
    c3 = 1
    c4 = 1
    c5 = 1

    #check rows
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            #get product of row
            product *= int(col)

            #get product of columns
            if x == 0:
                c1 *= int(col)
            elif x == 1:
                c2 *= int(col)
            elif x == 2:
                c3 *= int(col)
            elif x == 3:
                c4 *= int(col)
            elif x == 4:
                c5 *= int(col)

        if product == -1:
            return 1;
    
    #check columns
    if c1 == -1 or c2 == -1 or c3 == -1 or c4 == -1 or c5 == -1:
        return 1;

    return -1;

def calcScore():
    total = 0
    for y in board:
        for x in y:
            #sum unmarked
            if x != -1:
                total += int(x)
    
    #multiply sum by last number drawn
    total *= last
    return total

# get draw numbers and take out newline from last number
draw = f.readline().split(',')
draw[-1] = draw[-1].rstrip()

for x in f:
    check = 0
    #get next board
    board.clear()
    getBoard()

    #mark board
    for i, num in enumerate(draw):
        #mark on board
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if col == num:
                    board[y][x] = -1

        check = checkBoard()
        if check == 1:
            #set new fastest
            if (i > slowest):
                slowest = i
                last = int(num)
                #get score
                score = calcScore()
            break
    
print('score:', score)