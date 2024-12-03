
class PuzzleInput:
    @staticmethod
    def getInput(day: int | str) -> list[str]:
        with open("./inputs/" + str(day) + ".txt", "r") as f:
            return [x for x in f.readlines() if x != ""]
