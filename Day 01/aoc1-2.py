f = open("input.txt", "r")
last = -1
one = -1;
two = -2;
three = -3;


higher = 0;

for x in f:
    one = two
    two = three
    three = int(x)

    if (one > 0 and two > 0 and three > 0):
        sum = one + two + three
        print(sum,'')

        if (last > 0):
            if (sum > last):
                print('increased')
                higher += 1
        
        last = sum

print('higher = ', higher)

        