f = open("input.txt", "r")

log = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = []
epsilon = []

for x in f:
    for i, y in enumerate(x):
        if y:
            if y == '0':
                log[i] -= 1
            elif y == '1':
                log[i] += 1

for i, x in enumerate(log):
    if x > 0:
        gamma.append('1')
        epsilon.append('0')
    elif x < 0:
        gamma.append('0')
        epsilon.append('1')

g = int(''.join(gamma), 2)
e = int(''.join(epsilon), 2)

print('power consumption: ', g * e)
f.close()