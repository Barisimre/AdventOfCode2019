
def add(x, y):
    return [x[0]+y[0], x[1]+y[1], x[2]+y[2]]

def total_energy(moon):
    pot = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
    kin = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
    return pot*kin


# test
# a = [[-1,0, 2], [0, 0, 0]]
# b = [[2,-10, -7],  [0, 0, 0]]
# c = [[4,-8, 8], [0, 0, 0]]
# d = [[3,5, -1], [0, 0, 0]]


# real
a = [[-17, 9, -5], [0, 0, 0]]
b = [[-1, 7, 13],  [0, 0, 0]]
c = [[-19, 12, 5], [0, 0, 0]]
d = [[-6, -6, -4], [0, 0, 0]]

moons = [a, b, c ,d]

# after number of steps
for i in range(1000):
    
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

tots = 0
for m in moons:
    tots+=total_energy(m)
print(tots)