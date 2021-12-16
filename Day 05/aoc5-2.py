f = open("input.txt", "r")
board = []

#get dimensions
bigx = 0
bigy = 0
for x in f:
    temp = x.split()
    temp.remove('->')

    #start coord
    coord = temp[0].split(',')
    if int(coord[0]) > bigx:
        bigx = int(coord[0])
    if int(coord[1]) > bigy:
        bigy = int(coord[1])

    #end coord
    coord = temp[1].split(',')
    if int(coord[0]) > bigx:
        bigx = int(coord[0])
    if int(coord[1]) > bigy:
        bigy = int(coord[1])

#initialize board
for y in range(bigy+1):
    temp = []
    for x in range(bigx+1):
        temp.append(0)
    board.append(temp)

# go back to start of file
f.seek(0)

for x in f:
    temp = x.split()
    temp.remove('->')

    #start coord
    coord = temp[0].split(',')
    x1 = int(coord[0])
    y1 = int(coord[1])

    #end coord
    coord = temp[1].split(',')
    x2 = int(coord[0])
    y2 = int(coord[1])

    #horizontal line y1 == y2
    if y1 == y2:
        if x1 > x2:
            while(x1 - x2 >= 0):
                board[y1][x1] += 1
                x1 -= 1
        elif x1 < x2:
            while(x2 - x1 >= 0):
                board[y2][x2] += 1
                x2 -= 1

    #vertical line x1 == x2
    if x1 == x2:
        if y1 > y2:
            while(y1 - y2 >= 0):
                board[y1][x1] += 1
                y1 -= 1
        elif y1 < y2:
            while(y2 - y1 >= 0):
                board[y2][x2] += 1
                y2 -= 1

    #diagonal line diff of x and y is the same
    if abs(x1-x2) == abs(y1-y2):
        if y1 > y2:
            while(y1 - y2 >= 0):
                board[y1][x1] += 1

                #bottom left to top right
                if x1 < x2:
                    x1 += 1
                #bottom right to top left
                else:
                    x1 -= 1
                y1 -= 1

                
        elif y1 < y2:
            while(y2 - y1 >= 0):
                board[y2][x2] += 1

                #bottom left to top right
                if x2 < x1:
                    x2 += 1
                #bottom right to top left
                else:
                    x2 -= 1
                y2 -= 1
        
danger = 0

for j in board:
    for k in j:
        if k >= 2:
            danger += 1

print('danger:', danger)