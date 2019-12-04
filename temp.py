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
    words = pre_words
    return words

    
def solve():
    words = parse()

print(solve())