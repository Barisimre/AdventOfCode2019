def lines():
    words = []
    with open("input.txt") as fp:
        return fp.readline()



def parse():
    pre_words = lines()
    res = []
    words = pre_words.split(',')
    for word in words:
        res.append(int(word))
    return res

    
def run(words, i, j):
    words[1]= i
    words[2]= j
    pointer = 0
    while pointer < len(words):
        op = words[pointer]
        if op == 1:
            total = words[words[pointer+1]] + words[words[pointer+2]]
            words[words[pointer+3]] = total
        elif op == 2:
            total = words[words[pointer+1]] * words[words[pointer+2]]
            words[words[pointer+3]] = total
        elif op == 99:
            return words[0]
        pointer += 4


words = parse()

for i in range(100):
    for j in range(100):
        cp = words.copy()
        if run(cp, i, j) == 19690720:
            print(i, j)