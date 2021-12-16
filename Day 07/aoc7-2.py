f = open("input.txt", "r")
cheapest = None
sumD = {}

def getSummation(num):
    # check if summation for num is in the dictionary
    if num not in sumD:
        # calculate and add new summation
        summation = 0
        for x in range(num+1):
            summation += x
        
        sumD[num] = summation
    
    return sumD[num]

# get starting positions
pos = f.readline().split(',')

# get the biggest furthest position
biggest = 0
for x in pos:
    if int(x) > biggest:
        biggest = int(x)

# loop through positions
for x in range(biggest+1):
    fuel = 0
    dist = 0
    for j, y in enumerate(pos):
        # calculate fuel for each y to get to the same position as x
        dist = abs(int(x) - int(y))

        # get the summation for the distance
        fuel += getSummation(dist)


    if cheapest == None or fuel < cheapest[1]:
        cheapest = [x, fuel]

print(cheapest)