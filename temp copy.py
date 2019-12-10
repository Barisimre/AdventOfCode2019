def lines():
    words = []
    with open("input.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words


def parse():
    pre_words = lines()
    print(pre_words)
    return pre_words

    
def solve():
    words = parse()

print(solve())