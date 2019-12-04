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
    wires = []
    for x in pre_words:
        wires.append(x.split(','))
    return wires


def draw_wire(wire):
    coord = {}
    index = [0, 0]
    raw = []
    for action in wire:
        a = action[0]
        number = int(action[1:])
        for i in range(number):
            if a == 'U':
                index = (index[0], index[1]+1)
            elif a == 'D':
                index = (index[0], index[1]-1)
            elif a == 'R':
                index = (index[0]+1, index[1])
            elif a == 'L':
                index = (index[0]-1, index[1])
            raw.append(index)
            if index[0] in coord.keys():
                coord[index[0]].append(index[1])
            else:
                coord[index[0]] = [index[1]]
    return (coord, raw)


def draw(wires):

    wire1 = draw_wire(wires[0])[0]
    wire2 = draw_wire(wires[1])[0]
    return (wire1, wire2)


def dist(x,y):
    return abs(0-x) + abs(0-y)


def solve():
    wires = parse()
    (a,b) = draw(wires)
    res = []
    for i in a.keys():
        if i in b.keys():
           for x in a[i]:
               if x in b[i]:
                   res.append([i, x])

    wire1 = draw_wire(wires[0])[1]
    wire2 = draw_wire(wires[1])[1]
    mini = 99999
    for sol in res:
        i = wire1.index((sol[0], sol[1]))
        j = wire2.index((sol[0], sol[1]))
        if (i+j)<=mini:
            print(sol)
            mini = i+j

    return mini+2
print(solve())