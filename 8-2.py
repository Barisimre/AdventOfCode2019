import numpy as np
def lines():
    with open("input.txt") as fp:
        line = fp.readline()
        return line

tall = 6
wide = 25

def parse():
    rawData = lines()

    groups = []
    for i in np.arange(0, len(rawData), wide):
        groups.append([int(rawData[x]) for x in range(i, i+wide)])


    print(len(rawData), len(groups))
    layers = []
    temp = []
    p = 0
    for k in groups:
        temp.append(k)
        p +=1
        if p == tall:
            layers.append(temp.copy())
            temp.clear()
            p = 0
    return layers


    
def solve():
    layers = parse()
    linedex = 0
    maxCount = (9999, [])
    colors = [[2 for x in range(wide)] for y in range(tall)]

    for l in layers:
        # print(l)

        count = 0
        for t in range(tall):
            for w in range(wide):
                if colors[t][w] ==2:
                    colors[t][w] = l[t][w]
                    
    res = ""
    for i in range(tall):
        for j in range(wide):
            if colors[i][j] == 0:
                colors[i][j] = " "
            else:
                colors[i][j] = "*"
    
    for i in range(tall):
        line = ""
        for j in range(wide):
            line = line + colors[i][j]
        print(line)
        


    return res

print(solve())