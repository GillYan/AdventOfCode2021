from collections import deque

f = open("input.txt", "r")

start = f.readline().split(',')
# corresponding to each day 0 to 9
pop = [0,0,0,0,0,0,0,0,0]
days = 256

def printPop():
    # print info
    for i, y in enumerate(pop):
        print(y, end='')

        if i < len(pop) - 1:
            print(',', end='')
    print('')

# get starting population
for x in start:
    pop[int(x)] += 1

# print initial state
# print('Initial state:\t', end='')
# printPop()


for x in range(days):

    # save num of fishes to add
    spawn = pop[0]

    # rotate list one to the left
    temp = deque(pop)
    temp.rotate(-1)
    pop = list(temp)

    # spawn the fishes and reset 0 timer fishes
    pop[8] = spawn
    pop[6] += spawn

# sum the fishes
total = 0
for x in pop:
    total += x

print('num:', total)

f.close()