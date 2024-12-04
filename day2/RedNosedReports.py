import pandas as pd

inputTable = pd.read_csv(
    "./day2/RedNosedReportsInput.txt", sep=" ", header=None, engine="python"
)

diffTable = pd.concat(
    [
        inputTable[n + 1] - inputTable[n]
        for n in range(inputTable.columns.__len__() - 1)
    ],
    axis=1,
)


def assessSafety(row, canRemoveLevel=True):
    increasing = row.map(lambda val: val != val or (val >= 1 and val <= 3))
    decreasing = row.map(lambda val: val != val or (val <= -1 and val >= -3))

    if increasing.all() or decreasing.all():
        return True

    if not canRemoveLevel:
        return False

    for n in range(row.count() + 1):
        newRow = row.copy()
        if n > 0:
            if n != row.count():
                newRow[n] = newRow[n - 1] + newRow[n]
            newRow[n - 1] = float("nan")
        else:
            newRow[n] = float("nan")
        if assessSafety(newRow, False):
            return True

    return False


safeTable = diffTable.aggregate(assessSafety, axis=1).sum()

print(safeTable)
