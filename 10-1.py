def lines():
    words = []
    with open("input.txt") as fp:
        line = fp.readline().strip()
        while line:
            words.append(line)
            line = fp.readline().strip()
    return words


def parse():
    pre_words = lines()
    locs = []
    y = 0
    for line in pre_words:
        x = 0
        for c in line:
            if c == '#':
                locs.append((x, y))
            x +=1
        y +=1

    return locs

def slope(a, b):
    try:
        lower = a[1] >= b[1]
        sider = a[0] >= b[0]
        slope = (b[1]-a[1]) / (b[0]-a[0]) 
    except ZeroDivisionError:
        slope = -9999
    return (slope, lower, sider)

    
def solve():
    words = parse() 
    res = 0
    for ast in words:
        slopes = set()
        for other in words:
            if other != ast:
                slopes.add(slope(ast, other))
        res = max(res, len(slopes))
    return res

print(solve())