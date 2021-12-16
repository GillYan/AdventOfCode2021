f = open("input.txt", "r")

pre = []
cur = []
nex = []
low = []
basins = []

# up down left right
pos = [10,10,10,10]
risk = 0
row = 0

def getPositions(pos, i, pre, cur, nex):
    # get up
    if pre:
        pos[0] = pre[i]
    else:
        pos[0] = 10

    # get down
    if nex:
        pos[1] = nex[i]
    else:
        pos[1] = 10

    # get left
    if i != 0:
        pos[2] = cur[i - 1]
    else:
        pos[2] = 10

    # get right
    if i != (len(cur) - 1):
        pos[3] = cur[i + 1]
    else:
        pos[3] = 10

def processLine(pre, cur, nex, low, risk, row):
    for i, x in enumerate(cur):
        # get numbers in up down left and right of spot
        getPositions(pos, i , pre, cur, nex)
    
        # check if x is the lowest number in the surroundings
        if all(y > x for y in pos):
            low.append([row, i])
            risk += x + 1
    return risk

file = f.readlines()

for x in file:
    x = x.rstrip()
    
    # save new line
    pre = cur
    cur = nex
    nex = [int(digit) for digit in x]

    # skip the first line
    if not cur:
        continue

    # process all lines except last
    risk = processLine(pre, cur, nex, low, risk, row)
    row += 1

# process last line
pre = cur
cur = nex
nex = []
risk = processLine(pre, cur, nex, low, risk, row)

# calculate basins row = y, col = x -> file[y][x]
for (row, col) in low:
    bsize = 0
    checked = set()
    toCheck = [(row, col)]

    # explore the basin
    while toCheck:
        # get the coordinates of a point
        point = toCheck.pop()

        # check if the point has been checked yet
        if point in checked:
            continue
        else:
            checked.add(point)
            y = point[0]
            x = point[1]

            # ignore if the point's value is 9
            if int(file[y][x]) != 9:
                bsize += 1

                # check the value above
                if y > 0:
                    toCheck.append((y-1,x))

                # check the value below
                if y < len(file) - 1:
                    toCheck.append((y+1,x))

                # check the value to the left
                if x > 0:
                    toCheck.append((y,x-1))

                # check the value to the right
                if x < (len(file[y].rstrip()) - 1):
                    toCheck.append((y,x+1))

    basins.append(bsize)

basins = sorted(basins)
multi = basins[-3] * basins[-2] * basins[-1]

print('risk level sum:', risk)
#print('basins:', basins)
print('multi:', multi)