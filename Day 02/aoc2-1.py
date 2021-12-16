f = open("input.txt", "r")

horizontal = 0;
vertical = 0;

for x in f:
    tok = x.split()

    #get distance
    dist = int(tok[1])
    
    #get direction
    if tok[0].lower() == 'forward':
        horizontal += dist;
    elif tok[0].lower() == 'down':
        vertical += dist;
    elif tok[0].lower() == 'up':
        vertical -= dist;

print('pos: ', horizontal*vertical)
f.close()