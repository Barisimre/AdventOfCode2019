import itertools
from copy import copy

progs = []


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
    # for i in range(pos, 500):
    #     res[i] = -1
    return res

def compiler(program, p, inputs):
    res = None
    words = program.copy()
    pointer = p

    while True:
        allop = str(words[pointer])
        op = int(allop[len(allop) - 1])

        if op == 3:
            words[words[pointer + 1]] = inputs.pop(0)
            print("here", words[words[pointer + 1]])

            pointer += 2

        # Fix the opcode lengths
        while len(allop) < 5:
            allop = '0' + allop

        param1 = int(allop[2])
        param2 = int(allop[1])

        a = words[pointer + 1] if param1 == 1 else words[words[pointer + 1]]
        b = words[pointer + 2] if param2 == 1 else words[words[pointer + 2]]
        try:
            c = words[pointer + 3]
        except KeyError:
            print("Really..")
            pass

        if op == 9:
            break

        if op == 1:
            total = a + b
            words[c] = total
            pointer += 4

        elif op == 2:
            total = a * b
            words[c] = total

        if op == 4:
            res = words[words[pointer + 1]]
            pointer += 2
            break

        if op == 5:
            if a != 0:
                pointer = b
            else:
                pointer += 3

        elif op == 6:
            if a == 0:
                pointer = b
            else:
                pointer += 3

        if op == 7:
            if a < b:
                words[c] = 1
            else:
                words[c] = 0
            pointer += 4

        elif op == 8:
            if a == b:
                words[c] = 1
            else:
                words[c] = 0
            pointer += 4
    print("pointer", pointer)
    return words, pointer, inputs, res


def solve():
    program = parse()
    res = 0
    current = 0
    for sq in itertools.permutations([5, 6, 7, 8, 9]):

        inputs = []
        programs = []

        for i in range(5):
            programs.append(copy(program))
            inputs.append([sq[i]])

        pointers = [0, 0, 0, 0, 0]
        out = 0

        # Quit if the last amp gives None
        while out is not None:
            for j in range(5):
                inputs[j].append(out)
                print(inputs)

                programs[j], pointers[j], inputs[j], out = compiler(programs[j], pointers[j], inputs[j])
            current = current if out is None else out
        res = max(res, current)
    print(res)


solve()
