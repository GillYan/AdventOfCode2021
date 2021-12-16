f = open("input.txt", "r")

log = [0,0,0,0,0,0,0,0,0,0,0,0]
mc = []
lc = []
ogr = []
csr = []

def getBalance(ite):
    for x in ite:
        for i, y in enumerate(x):
            if y:
                if y == '0':
                    log[i] -= 1
                elif y == '1':
                    log[i] += 1

def getMCLC(all):
    mc.clear()
    lc.clear()

    #get most common and least common of each bit
    for i, x in enumerate(all):
        if int(x) > 0:
            mc.append(1)
            lc.append(0)
        elif int(x) < 0:
            mc.append(0)
            lc.append(1)
        elif int(x) == 0:
            mc.append(-1)
            lc.append(-1)

getBalance(f)
getMCLC(log)

f.seek(0)

# append matching first bit for ogr and csr
for x in f:
    if int(x[0]) == mc[0]:
        ogr.append(x.rstrip())
    elif int(x[0]) == lc[0]:
        csr.append(x.rstrip())

# get oxygen generation rate
i = 1
while (len(ogr) > 1):
    log.clear()
    log = [0,0,0,0,0,0,0,0,0,0,0,0]
    remove = []
    getBalance(ogr)
    getMCLC(log)

    for x in ogr:
        if int(x[i]) != mc[i]:
            if mc[i] == -1 and int(x[i]) == 1:
                continue
            else:
                remove.append(x)

    for x in remove:
        ogr.remove(x)

    i += 1
    
# get co2 scrubber rate
i = 1
while (len(csr) > 1):
    log.clear()
    log = [0,0,0,0,0,0,0,0,0,0,0,0]
    remove = []
    getBalance(csr)
    getMCLC(log)

    for x in csr:
        if int(x[i]) != lc[i]:
            if lc[i] == -1 and int(x[i]) == 0:
                continue
            else:
                remove.append(x)

    for x in remove:
        csr.remove(x)

    i += 1

o = int(ogr[0], 2)
co2 = int(csr[0], 2)
print(o * co2)
