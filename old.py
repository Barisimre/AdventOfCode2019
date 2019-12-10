import itertools
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
    return res

    
def compile(inputs, program):
    res = 0
    words = program.copy()
    inputCounter = 0
    pointer = 0
    while pointer < len(words):
        
        allop = str(words[pointer])
        op = int(allop[len(allop)-1])

        if op == 3:
            words[words[pointer+1]] = inputs[inputCounter]
            inputCounter+=1
            pointer += 2
            continue

        if op == 4:
            # print("OUTPUT = ", words[words[pointer+1]])
            res = words[words[pointer+1]]

            pointer += 2
            continue

        if op == 9:
            return res

        # Fix the opcode lengths
        while len(allop) < 5:
            allop = '0' + allop
            
        param1 = int(allop[2])
        param2 = int(allop[1])
        param3 = int(allop[0])
       
        a = words[pointer+1] if param1 == 1 else words[words[pointer+1]]
        b = words[pointer+2] if param2 == 1 else words[words[pointer+2]]
        c = words[pointer+3]

        if op == 5:
            if a != 0:
                pointer = b
            else:
                pointer += 3
            continue

        elif op == 6:
            if a == 0:
                pointer = b
            else:
                pointer += 3
            continue

        if op == 7:
            if a < b:
                words[c] = 1
            else:
                words[c] = 0

        elif op == 8:
            if a == b:
                words[c] = 1
            else:
                words[c] = 0

        if op == 1:
            total = a + b
            words[c] = total

        elif op == 2:
            total = a * b
            words[c] = total

        pointer += 4

def solve():
    phases = [0, 1, 2, 3, 4]
    squences = list(itertools.permutations([0,1,2,3,4]))
    program = parse()
    out = 0
    maxOut = (0, [0,0,0,0,0])
    pointer = 0
    for sq in squences:
        for j in range(5):
            nProgram = program.copy()
            out = compile([sq[j],out], nProgram)
        if out >= maxOut[0]:
            maxOut = (out, sq)
        out = 0
    print(maxOut) 
    pass




solve()