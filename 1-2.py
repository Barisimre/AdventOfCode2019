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

    
def calc_fuel(mass):
    new = math.floor(mass/3) - 2
    total = 0
    while new > 0:
        total += new
        new = math.floor(new/3) - 2

    return total

def solve():
    words = process()
    total = 0
    for word in words:
        total += calc_fuel(int(word))
    return total
print(solve())