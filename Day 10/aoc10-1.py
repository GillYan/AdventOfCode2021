def parseLine(line):
    stack = []
    illegal = 0

    for x in line:
        if x == '(' or x == '[' or x == '{' or x == '<':
            stack.append(x)
        elif x == ')' or x == ']' or x == '}' or x == '>':
            # get last added
            check = stack.pop()

            # find expected
            if check == '(':
                opp = ')'
            elif check == '[':
                opp = ']'
            elif check == '{':
                opp = '}'
            elif check == '<':
                opp = '>'

            # found corruption
            if opp != x:
                # print('expected:', opp, 'got:', x)
                stack.append(check)
                stack.append(x)
                
                # calculate illegal syntax points
                if x == ')':
                    illegal = 3
                elif x == ']':
                    illegal = 57
                elif x == '}':
                    illegal = 1197
                elif x == '>':
                    illegal = 25137
                break

    return illegal

def main():
    f = open("input.txt", "r")
    points = 0

    for y in f:
        y = y.rstrip()
        illegal = parseLine(y)
        points += illegal

        
    print(points)
    
    f.close()

if __name__ == "__main__":
    main()