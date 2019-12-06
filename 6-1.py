planets = {}

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
    for line in pre_words:
        a = (line.split(')')[0]).strip()
        b = (line.split(')')[1]).strip()
        if a in planets.keys():
            planets[a].append(b)
        else:
            planets[a] = [b]

res = []
def travel(parent, c):
    for child in planets[parent]:
        if child in planets.keys():
            res.append(c+1)
            travel(child, c+1)
        else:
            res.append(c+1)
    return res
def solve():

    parse()
    arr = travel("COM", 0)
    print(sum(arr))
        
solve()