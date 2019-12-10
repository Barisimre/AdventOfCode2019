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
    # a = f,t
    # b = t,t
    # c = t,f
    # d = f,f
    a = []
    b = []
    c = []
    d = []
    for t in targets:
        if t[1] and t[2]:
            a.append((t, targets[t]))
        if not t[1] and t[2]:
            b.append((t, targets[t]))
        if not t[1] and not t[2]:
            c.append((t, targets[t]))
        if t[1] and not t[2]:
            d.append((t, targets[t]))
    sa = sorted(a)
    sb = sorted(b)
    sc = sorted(c)
    sd = sorted(d)

    i = 199 - (len(a)+len(d)+len(b))
    return sc[i] # pure magic calibrated through the given example


print(solve())