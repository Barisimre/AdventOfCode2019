import intcode as ic

text = ic.parser()
program = ic.IntCode(text, [2])
print(program.run())
