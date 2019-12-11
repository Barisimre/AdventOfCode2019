import intcode as ic

text = ic.parser()
program = ic.IntCode(text, None, 0, True)
coords = {}
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
    # print(pos)

    out[0] = program.run()[0]
    if out[0] == -1: break

    out[1] = program.run()[0]
    if out[0] == -1: break

    # Paint
    coords[pos] = out[0]
    # print(out[0])

    if out[1] == 0:
        d = turn_right(d, 3)
        pos = add(pos, d)
        # print("left")
    else:
        d = turn_right(d, 1)
        pos = add(pos, d)
    # print(out)
    
print(len(coords.keys()))