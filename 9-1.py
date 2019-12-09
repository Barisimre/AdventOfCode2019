

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
    for i in range(pos, 10000):
        res[i] = 0
    return res



p1 = 0
p2 = 0

POS = 0
IMM = 1
REL = 2
mode = POS



def run(reg, i, inputs):
    rB = 0
    values = []
    # print(i)
    while True:
        ins = reg[i]
        mp1 = int(ins / 100) % 10
        mp2 = int(ins / 1000) % 10
        mp3 = int(ins / 10000) % 10
        ins = ins % 100

        if ins == 99:
            print(i)
            break

        # r2 = i+2 if mp2 == IMM else reg[i+2]
        # r1 = i+1 if mp1 == IMM else reg[i+1]

        if mp1 == IMM:
            r1 = i+1
        elif mp1 == REL:
            r1 = reg[i+1]+rB
        else:
            r1 = reg[i+1]

        if mp2 == IMM:
            r2 = i+2
        elif mp2 == REL:
            r2 = reg[i+2]+rB
        else:
            r2 = reg[i+2]


        try:
            if mp3 == IMM:
                r3 = i+3
            elif mp3 == REL:
                r3 = reg[i+3]+rB
            else:
                r3 = reg[i+3]
        except IndexError:
            print("Lol")
            pass



        if ins == 1:
            reg[r3] = reg[r1] + reg[r2]
            i += 4
        elif ins == 2:
            reg[r3] = reg[r1] * reg[r2]
            i += 4
        elif ins == 3:
            reg[r1] = inputs.pop(0)
            i += 2
        elif ins == 4:
            values.append(reg[r1])
            i += 2
        elif ins == 5:
            if reg[r1]:
                i = reg[r2]
            else:
                i += 3
        elif ins == 6:
            if reg[r1] == 0:
                i = reg[r2]
            else:
                i += 3
        elif ins == 7:
            reg[r3] = 1 if reg[r1] < reg[r2] else 0
            i += 4
        elif ins == 8:
            reg[r3] = 1 if reg[r1] == reg[r2] else 0
            i += 4

        elif ins == 9:
            rB = rB + reg[r1]
            i += 2
        else:
            print(f'Bad opcode: {ins} - FAILED')
            break
    return reg, values



def solve():
    program = parse()
    words = run(program, 0, [1])
    print(words[1])
solve()