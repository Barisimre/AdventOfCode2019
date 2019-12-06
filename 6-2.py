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
def travel(parent, _c):
    c = _c.copy()
    for child in planets[parent]:
        if child in planets.keys():
            c.append(child)
            travel(child, c)
            c.remove(child)
        else:
            if child == "SAN" or child == "YOU":
                nc = c.copy()
                res.append(nc)
    return res


def calc_path(l1, l2):

    x = l1.copy()
    y = l2.copy()
    x.reverse()
    y.reverse()
    for i in x:
        for j in y:
            if i == j:
                return x.index(i) + y.index(j)

def solve():

    parse()
    arr = travel("COM", [])
    print(calc_path(arr[0], arr[1]))
        
solve()