from PuzzleInput import PuzzleInput
import re

puzzleInput = PuzzleInput.getInput(3)

mul = 0
mulToggled = 0

do = "do()"
dont = "don't()"

pattern = r"mul\((\d+),(\d+)\)"

for line in puzzleInput:
    #part 1
    matches = list(map(lambda k: (int(k[0]), int(k[1])), re.findall(pattern, line)))

    for m in matches:
        mul += m[0] * m[1]
    
    enabled = True

    #part 2
    for i in range(len(line)):
        instr = line[i:]

        if instr.startswith(do):
            enabled = True
        elif instr.startswith(dont):
            enabled = False

        m = re.match(pattern, instr)
        if m is not None and enabled:
            x, y = map(int, m.groups())

            mulToggled += x * y

print(mul)
print(mulToggled)