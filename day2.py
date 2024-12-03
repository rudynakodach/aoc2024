from PuzzleInput import PuzzleInput

puzzleInput = PuzzleInput.getInput(2)

safeReports = 0
dampenedReports = 0

for line in puzzleInput:
    
    report = list(map(int, line.split(" ")))

    def is_safe(report):
        increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
        decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
        return increasing or decreasing

    if is_safe(report):
        safeReports += 1
        dampenedReports += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                dampenedReports += 1
                break

print(safeReports)
print(dampenedReports)
