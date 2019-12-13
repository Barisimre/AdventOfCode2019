import intcode as ic
import os
import time
text = ic.parser()

program = ic.IntCode(text, [], 0, True)
grid = [[" " for k in range(42)] for j in range(26)]
# print(grid[0])
count = 0

def update(x, y, t):
    c = ""
    if t == 0:
        c = " "
    elif t == 1:
        c = "'"
    elif t == 2:
        c = "#"
    elif t == 3:
        c = "_"
    else:
        c = "*"

    grid[y][x] = c

def draw():
    for y in grid:
        line = ""
        for x in y:
            line = line + x
        print(line)

while True:

    x = program.run()[0]
    y = program.run()[0]
    t = program.run()[0]

    # print(x,y,t)
    if x == "end" or y == "end" or t == "end":
        break
    update(x,y,t)

    if t == 2:
        count +=1
    os.system("clear")
    draw()

print(count)

