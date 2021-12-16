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

    return stack, illegal

def closeChunks(stack):
    closers = []
    points = 0

    # get the characters needed to close the chunk
    for x in stack:
        if x == '(':
            closers.insert(0, ')')
        elif x == '[':
            closers.insert(0, ']')
        elif x == '{':
            closers.insert(0, '}')
        elif x == '<':
            closers.insert(0, '>')
            
    # calculate the points
    for x in closers:
        points *= 5
        if x == ')':
            points += 1
        elif x == ']':
            points += 2
        elif x == '}':
            points += 3
        elif x == '>':
            points += 4

    return points

def main():
    f = open("input.txt", "r")
    points = 0
    scores = []

    for y in f:
        y = y.rstrip()
        stack, illegal = parseLine(y)
        points += illegal

        # close chunks of uncorrupted lines
        if illegal == 0:
            scores.append(closeChunks(stack))
        else:
            continue
        
    # part 1
    print(points)
    
    # part 2
    # get the middle score
    points = (sorted(scores))[len(scores) // 2]
    print(points)
    
    f.close()

if __name__ == "__main__":
    main()