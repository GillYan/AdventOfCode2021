f = open("input.txt", "r")
total = 0

for x in f:
    # extract the output
    temp = x.split('|')
    temp[0] = temp[0].rstrip()
    temp[1] = temp[1].rstrip().lstrip()
    input = temp[0].split()
    output = temp[1].split()
    
    digit = ['','','','','','','','','','']
    buff = []

    # parse the input to get letters of 1,4,7, and 8
    for y in input:
        lets = set(y)
        i = len(lets)
        j = 0

        # get letters used in 1, 4, 7, or 8
        if i == 2: j = 1
        elif i == 4: j = 4
        elif i == 3: j = 7
        elif i == 7: j = 8

        if j != 0:
            digit[j] = lets

    # get the letters for the other numbers
    ind = 0
    while '' in digit:
        y = input[ind % 10]
        lets = set(y)
        i = len(lets)

        if i == 6:
            # found letters for digit 9
            if len(digit[4] & lets) == 4:
                digit[9] = lets
            elif digit[9] != '':
                # found letters for digit 0 or 6
                if len(digit[1] & lets) == 2:
                    digit[0] = lets
                else:
                    digit[6] = lets
        elif i == 5:
            # found letters for digit 3
            if len(digit[1] & lets) == 2:
                digit[3] = lets
            # found letters for digit 2 or 5
            elif digit[3] != '' and digit[9] != '':
                if len(digit[9] & lets) == 4:
                    digit[2] = lets
                else:
                    digit[5] = lets
        
        ind += 1

    # letters for each digit found, decode the output
    for x in output:
        buff.append(str(digit.index(set(x))))

    total += int(''.join(buff))

print(total)

f.close()