import math
import numpy as np

def lines():
    words = []
    with open("input.txt") as fp:
        line = fp.readline().strip()
        while line:
            words.append(line)
            line = fp.readline().strip()
    return words

def cart2pol(a):
    x = a[0]
    y = a[1]
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)


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
        high = a[1] <= b[1]
        right = a[0] <= b[0]
        slope = (b[1]-a[1]) / (b[0]-a[0]) 
    except ZeroDivisionError:
        slope = -9999
    return (slope, high, right)

def dis(a,b):
    return math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2)

    
def solve():
    us = (11,13)
    words = parse() 
    targets = {} # <slope, coord>
    for target in words:
        if slope(us, target) in targets.keys():
            if dis(us, target) <= dis(us, targets[slope(us, target)]):
                targets[slope(us, target)] = target
        else:
            targets[slope(us, target)] = target
    count = 0
    pol = []
    pus = cart2pol(us)
    for i in targets:
        pol.append(cart2pol(targets[i]))
    yes = sorted(pol, key=lambda x : math.atan2(x[1]-pus[1], x[0]-pus[0]))
    print(yes)
    return yes[200]

def pol2cart(a):
    rho = a[0]
    phi = a[1]

    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

print(pol2cart(solve()))