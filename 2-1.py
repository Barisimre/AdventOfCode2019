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
    print(res)
    return res

    
def solve():
    words = parse()

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
            return words
        pointer += 4
print(solve())