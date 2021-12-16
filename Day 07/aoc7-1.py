f = open("input.txt", "r")
cheapest = None
pos = f.readline().split(',')

# loop through positions
for i, x in enumerate(pos):
    fuel = 0
    for j, y in enumerate(pos):
        if i == j:
            continue
        
        # calculate fuel for each y to get to same position as x
        fuel += abs(int(x) - int(y))

    if cheapest == None or fuel < cheapest[1]:
        cheapest = [i, fuel]

print(cheapest)