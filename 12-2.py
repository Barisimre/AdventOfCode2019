
import numpy as np

def add(x, y):
    return [x[0]+y[0], x[1]+y[1], x[2]+y[2]]


# Alternate for axis
def hsh(moon, a):
    return (str(moon[0][a]) + str(moon[1][a]))


def hsh2(moons, a):
    res = ""
    for m in moons:
        res += hsh(m, a)
    return res


def run(_moons, _megaMoons, a):
    moons = _moons.copy()
    megaMoons = _megaMoons.copy()

    for i in range(100000000000000000000000000):

        megaMoons.add(hsh2(moons, a))

        for m in moons:
            for o in moons[moons.index(m)+1:]:
                if m[0][0] < o[0][0]:
                    m[1][0] += 1
                    o[1][0] -= 1
                if m[0][1] < o[0][1]:
                    m[1][1] += 1
                    o[1][1] -= 1
                if m[0][2] < o[0][2]:
                    m[1][2] += 1
                    o[1][2] -= 1

                if m[0][0] > o[0][0]:
                    m[1][0] -= 1
                    o[1][0] += 1
                if m[0][1] > o[0][1]:
                    m[1][1] -= 1
                    o[1][1] += 1
                if m[0][2] > o[0][2]:
                    m[1][2] -= 1
                    o[1][2] += 1
                
        for k in moons:
            k[0] = add(k[0], k[1])


        if hsh2(moons, a) in megaMoons:
            return i+1
    
a = [[-17, 9, -5], [0, 0, 0]]
b = [[-1, 7, 13],  [0, 0, 0]]
c = [[-19, 12, 5], [0, 0, 0]]
d = [[-6, -6, -4], [0, 0, 0]]

moons = [a, b, c ,d]
megaMoons = set()
res = []
for i in [0,1,2]:
    res.append(run(moons.copy(), megaMoons.copy(), i))

print(np.lcm.reduce(res))








# Find the period of x 186028
# Find the period of y 231614
# Find the period of z 60424