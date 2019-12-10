import intcode as ic
from itertools import permutations

text = ic.parser()
program = ic.IntCode(text, [], 0, True)
res = 0
for perm in permutations([0, 1, 2, 3, 4]):
    out = 0
    for phase in perm:

        program.reset()
        program.give_input([phase, out])
        out = program.run()[0]

    res = max(res, out)
print(res)
