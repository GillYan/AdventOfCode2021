f = open("input.txt", "r")

horizontal = 0;
vertical = 0;
aim = 0;

for x in f:
    tok = x.split()

    #get distance
    dist = int(tok[1])
    
    #get direction
    if tok[0].lower() == 'forward':
        horizontal += dist;
        vertical += aim*dist;
    elif tok[0].lower() == 'down':
        aim += dist;
    elif tok[0].lower() == 'up':
        aim -= dist;

print('pos: ', horizontal*vertical)