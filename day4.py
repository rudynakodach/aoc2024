from PuzzleInput import PuzzleInput
puzzleInput = PuzzleInput.getInput(4)

word = "XMAS"

Xmas = 0
occuranes = 0

def in_bounds(x: int, y: int, w: int, h: int) -> bool:
    return 0 <= x < w and 0 <= y < h

height = len(puzzleInput)

for y in range(len(puzzleInput)):
    width = len(puzzleInput[y])
    for x in range(len(puzzleInput[y])):

        #part 2
        chars = []
        dirs = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
        if (puzzleInput[y][x] == "A"):
            if all(in_bounds(x + dirs[i][0], y + dirs[i][1], width, height) for i in range(len(dirs))):
                for dir in dirs:
                    dX = dir[0]
                    dY = dir[1]
                                    
                    chars.append(puzzleInput[y + dY][x + dX])

            if len(chars) == 4:
                t = "".join(chars)

                if "MMSS" in t or "SSMM" in t or "MSMS"in t or "SMSM" in t:
                    print(chars)
                    Xmas += 1

        #part 1
        directions = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        for dir in directions:
            dX = dir[0]
            dY = dir[1]

            if not all(in_bounds(x + i * dX, y + i * dY, width, height) for i in range(len(word))):
                continue
            
            t = "".join([puzzleInput[y + i * dY][x + i * dX] for i in range(4)])
            if word in t:
                occuranes += 1

print(occuranes)
print(Xmas)

    