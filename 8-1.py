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
    print(layers[3])
    return layers


    
def solve():
    layers = parse()
    linedex = 0
    maxCount = (9999, [])
    for l in layers:
        count = 0
        for t in l:
            for w in t:
                if w == 0:      
                    count += 1
        if count <= maxCount[0]:
            maxCount= (count, l)
    print(maxCount)
    one = 0
    two = 0
    res = maxCount[1]
    for i in res:
        for j in i:
            if j == 1:
                one += 1
            elif j == 2:
                two += 1
    return one*two





print(solve())