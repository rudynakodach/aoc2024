from PuzzleInput import PuzzleInput

puzzleInput = PuzzleInput.getInput(1)

left = []
right = []

distance = 0
similarityScore = 0

for line in puzzleInput:
    l = int(line.split("   ")[0])
    r = int(line.split("   ")[1])

    left.append(l)
    right.append(r)

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    l = left[i]
    r = right[i]

    distance += abs(l - r)
    similarityScore += l * right.count(l)

print(distance)
print(similarityScore)
