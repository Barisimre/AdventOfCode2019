import time



class IntCode:
    memory = {}
    programCounter = 0
    originalProgram = {}
    relPointer = 0
    inputs = []
    outputs = []
    retWithOut = False
    p1 = 0
    p2 = 0

    POS = 0
    IMM = 1
    REL = 2

    def __init__(self, program, inputs=None, program_counter=0, return_with_output=False):

        self.memory = program.copy()
        self.originalProgram = program
        self.programCounter = program_counter
        self.inputs = inputs
        self.retWithOut = return_with_output

    def __str__(self):
        return "A string"

    def give_input(self, inp):
        self.inputs = inp

    def run(self):

        
        # Make local variables
        program = self.memory
        i = self.programCounter
        while True:

            # Parse the op code and the modes
            op = program[i]
            mode1 = int(op / 100) % 10
            mode2 = int(op / 1000) % 10
            mode3 = int(op / 10000) % 10
            op = op % 100

            # Quit
            if op == 99:
                self.outputs.append(-1)
                break

            if mode1 == self.IMM:
                a = i + 1
            elif mode1 == self.REL:
                a = program[i + 1] + self.relPointer
            else:
                a = program[i + 1]

            if mode2 == self.IMM:
                b = i + 2
            elif mode2 == self.REL:
                b = program[i + 2] + self.relPointer
            else:
                b = program[i + 2]

            if mode3 == self.IMM:
                c = i + 3
            elif mode3 == self.REL:
                c = program[i + 3] + self.relPointer
            else:
                c = program[i + 3]


            # Op codes and the functions for them
            if op == 1:
                program[c] = program[a] + program[b]
                i += 4

            elif op == 2:
                program[c] = program[a] * program[b]
                i += 4

            elif op == 3:
                program[a] = self.inputs.pop(0)
                i += 2

            elif op == 4:
                self.outputs.append(program[a])
                i += 2
                if self.retWithOut:
                    break

            elif op == 5:
                if program[a]:
                    i = program[b]
                else:
                    i += 3

            elif op == 6:
                if program[a] == 0:
                    i = program[b]
                else:
                    i += 3

            elif op == 7:
                program[c] = 1 if program[a] < program[b] else 0
                i += 4

            elif op == 8:
                program[c] = 1 if program[a] == program[b] else 0
                i += 4

            elif op == 9:
                self.relPointer = self.relPointer + program[a]
                i += 2

            else:
                print("Something went wrong could parse op code = ", op)
                break

        # Save the data after the program, if you don't want this there is a reset() function
        self.memory = program
        self.programCounter = i
        temp = self.outputs.copy()

        self.outputs.clear()

        return temp

    def reset(self):
        self.programCounter = 0
        self.relPointer = 0
        self.memory = self.originalProgram.copy()
        self.inputs = []
        self.outputs = []


def parser(file_name="input.txt"):
    with open("input.txt") as fp:
        line = fp.readline()
    res = {}
    words = line.split(',')
    pos = 0
    for word in words:
        res[pos] = int(word)
        pos += 1
    for i in range(pos, 10000):
        res[i] = 0
    return res

