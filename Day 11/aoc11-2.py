def printPos(pos):
    for row in pos:
        print(row)

def getAdjacent(pos, row, col):
    # 0 1 2
    # 3 n 4
    # 5 6 7
    adj = [(),(),(),(),(),(),(),()]

    # set each coordinate
    adj[0] = ((row - 1), (col -1))
    adj[1] = ((row - 1), col)
    adj[2] = ((row - 1), (col + 1))
    adj[3] = (row, (col - 1))
    adj[4] = (row, (col + 1))
    adj[5] = ((row + 1), (col - 1))
    adj[6] = ((row + 1), col)
    adj[7] = ((row + 1), (col + 1))

    # check if any coords are invalid
    for i, x in enumerate(adj):
        for y in x:
            if y < 0 or y > (len(pos) - 1):
                adj[i] = ()

    return adj

def takeStep(pos):
    flash = []
    numFlash = 0

    # increment each spot by 1
    for row, y in enumerate(pos):
        for col, x in enumerate(y):
            pos[row][col] += 1
            
            if (x + 1) > 9:
                flash.append((row, col))

    while flash:
        # get the next spot to flash
        (fr, fc) = flash.pop()
        numFlash += 1
        
        # get the coords of surrounding and increment them
        adj = getAdjacent(pos, fr, fc)

        pos[fr][fc] = -1
        for x in adj:
            # not empty
            if x:
                nr, nc = x
                val = pos[nr][nc]

                # position hasnt already been flashed
                if val > -1 and (nr, nc) not in flash:
                    val += 1
                    pos[nr][nc] = val

                    # flash this position if possible
                    if val > 9:
                        flash.append((nr, nc))
                    

    # reset flashes
    for row, x in enumerate(pos):
        for col, y in enumerate(x):
            if y == -1:
                pos[row][col] = 0
    
    return numFlash


def main():
    f = open("input.txt", "r")

    pos = []
    numSteps = 100
    numFlashes = 0

    # read the file into variable without newlines
    for row in f:
        temp = []
        row = row.rstrip()
        for col in row:
            temp.append(int(col))
        pos.append(temp)

    i = 0
    while True:
        i += 1
        numFlashes = takeStep(pos)
        if numFlashes == 100:
            print('All of the octopuses flashed on step', i)
            break

    f.close()

if __name__ == "__main__":
    main()