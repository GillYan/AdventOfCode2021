f = open("input.txt", "r")

start = f.readline().split(',')
pop = []
days = 80

def printPop():
    # print info
    for i, y in enumerate(pop):
        print(y, end='')

        if i < len(pop) - 1:
            print(',', end='')
    print('')

# get starting population
for x in start:
    pop.append(x)

# print initial state
# print('Initial state:\t', end='')
# printPop()

for x in range(days):
    numAdd = 0
    
    # loop through population and decrement
    for i, y in enumerate(pop):
        new = int(y) - 1

        # if it's -1 now, then reset timer
        if new < 0:
            new = 6
            numAdd += 1
        pop[i] = new
    
    #append the new fishes
    for i in range(numAdd):
        pop.append(8)

    # print info
    # print('After', x+1, 'days:\t', end='')
    # printPop()

print(len(pop))