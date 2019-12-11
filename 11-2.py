import intcode as ic

text = ic.parser()
program = ic.IntCode(text, None, 0, True)
coords = {(500, 500):1}
pos = (500, 500)
out = [-1, -1]
d = (0, 1)

def turn_right(a, i):
    an = a
    for k in range(i):
        an = (an[1], -1*an[0])
    return an
    
def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

while True:
    if pos not in coords.keys():
        coords[pos] = 0
    program.give_input([coords[pos]])

    out[0] = program.run()[0]
    if out[0] == -1: break

    out[1] = program.run()[0]
    if out[0] == -1: break

    # Paint
    coords[pos] = out[0]

    if out[1] == 0:
        d = turn_right(d, 3)
        pos = add(pos, d)
    else:
        d = turn_right(d, 1)
        pos = add(pos, d)

maxx, maxy = 0, 0
minx, miny = 999, 999

for a in coords:
    maxx = max(maxx, a[0])
    maxy = max(maxy, a[1])
    minx = min(minx, a[0])
    miny = min(miny, a[1])

print(maxx, maxy, minx, miny)


print(len(coords.keys()))

for i in range(minx,maxx+1): 
    for j in range(miny,maxy+1):
        if not (i, j) in coords.keys():
            coords[(i,j)] = 0

for i in range(miny,maxy+1): 
    print("".join([('#' if coords[(j, i)] == 1 else ' ') for j in range(minx,maxx+1)]))

# This is upside down and mirrorred. Good luck have fun








    
