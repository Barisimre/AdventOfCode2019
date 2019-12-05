def lines():
    words = []
    with open("input.txt") as fp:
        return fp.readline()



def parse():
    pre_words = lines()
    res = {}
    words = pre_words.split(',')
    pos = 0
    for word in words:
        res[pos] = int(word)
        pos += 1
    # Add some memory
    # for i in range(10):
    #     res[pos] = -1
    #     pos += 1

    return res

    
def solve():
    program = '\n'
    words = parse()
    pointer = 0
    while pointer < len(words):
        
        allop = str(words[pointer])
        op = int(allop[len(allop)-1])

        if op == 3:
            words[words[pointer+1]] = 1 # TODO
            print("Input address", words[pointer+1], "input = 1")
            # print(words[words[pointer+1]])
            program = program + "  3  " +  "1" +'\n'
            pointer += 2
            continue

        if op == 4:
            if allop == "104":
                print("OUTPUT = ", words[pointer+1])
            else:
                print("OUTPUT = ", words[words[pointer+1]])

            program = program + "  4  addr=" + str(words[pointer+1]) +  '\n'
            pointer += 2
            continue

        if op == 9:
            print("Nien nien")
            print(program, " 99\n")
            return words

        # Fix the opcode lengths
        while len(allop) < 5:
            allop = '0' + allop
            
        param1 = int(allop[2])
        param2 = int(allop[1])
        param3 = int(allop[0])
       
        a = words[pointer+1] if param1 == 1 else words[words[pointer+1]]
        b = words[pointer+2] if param2 == 1 else words[words[pointer+2]]
        c = words[pointer+3]

        if op == 1:
            total = a + b
            words[c] = total


        elif op == 2:
            total = a * b
            words[c] = total


        program = program + "  " + allop + "  " + str(a) + "  " + str(b) + "  " + str(c) + '\n'
        pointer += 4


#print(solve())
solve()