from PuzzleInput import PuzzleInput

puzzleInput = PuzzleInput.getInput(11)

stones = list(map(int, puzzleInput[0].split(" ")))

def process(stone: int):
    if stone == 0:
        return [1]
    
    s = str(stone)
    l = len(s)
    if l % 2 == 0:
        mid = l // 2
        return [int(s[:mid]), int(s[mid:])]    
    return [stone * 2024]

for i in range(75):
    stones = [process(stone) for stone in stones]
    if i == 25:
        print(len(stones))
    print(i)

    # for stone in stones:
    #     if stone == 0:
    #         s.append(1)
    #     elif len(str(stone)) % 2 == 0:
    #         n = str(stone)
    #         mid = len(n) // 2

    #         left = int(n[:mid])
    #         right = int(n[mid:])

    #         s.append(left)
    #         s.append(right)
    #     else:
    #         s.append(stone * 2024)

    # stones = s
    # print(i)


print(len(stones))