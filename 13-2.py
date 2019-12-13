import intcode as ic
import os
import time
text = ic.parser()

program = ic.IntCode(text, [], 0, True)
grid = [[" " for k in range(42)] for j in range(26)]
paddle = 0
count = 0
direction = 0
score = 0


def update(x, y, t):
    c = ""
    if t == 0:
        c = " "
    elif t == 1:
        c = "█"
    elif t == 2:
        c = "▒"
    elif t == 3:
        global paddle
        paddle = x
        c = "═"
    else:
        ball(x, y)
        c = "●"

    grid[y][x] = c


def ball(x, y):

    global direction
    global paddle

    if paddle > x:
        direction = -1
    elif paddle < x:
        direction = 1
    else:
        direction = 0
    

def draw():
    global score
    print("Score:", score)
    for y in grid:
        line = ""
        for x in y:
            line = line + x
        print(line)

while True:
    
    program.give_input([direction])
    x = program.run()[0]
    y = program.run()[0]
    t = program.run()[0]

    # print(x,y,t)
    if x == "end" or y == "end" or t == "end":
        break
    update(x,y,t)

    if x == -1:
        score = t

    os.system("clear")
    draw()

print(score)

