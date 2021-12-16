f = open("input.txt", "r")
last = -1
higher = 0;

for x in f:
    if (int(last) > 0):
        print(x, end='')

        if (x > last):
            higher += 1
            print("increased")
        else:
            print("decreased")
        
    else:
        print(x, end = '')
        print('N/A')

    last = x

print('total higher = ', higher)