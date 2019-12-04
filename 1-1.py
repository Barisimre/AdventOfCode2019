import math

def lines():
    words = []
    with open("input.txt") as fp:
        line = fp.readline()
        while line:
            words.append(line)
            line = fp.readline()
    return words


def process():
    pre_words = lines()
    words = pre_words
    return words


def solve():
    words = process()
    res = []
    for word in words:
        fuel = int(word)
        res.append(math.floor(fuel/3) - 2)
    total = 0
    for fuel in res:
        total += fuel
    return total
print(solve())