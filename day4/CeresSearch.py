from CeresSearchInput import input
import pandas as pd

crossword = pd.DataFrame(map(lambda line: [char for char in line], input.splitlines()))
XMASkernels = [
    pd.DataFrame(
        [
            ["X", "M", "A", "S"],
        ]
    ),
    pd.DataFrame(
        [
            ["X", " ", " ", " "],
            [" ", "M", " ", " "],
            [" ", " ", "A", " "],
            [" ", " ", " ", "S"],
        ]
    ),
    pd.DataFrame(
        [
            ["X"],
            ["M"],
            ["A"],
            ["S"],
        ]
    ),
    pd.DataFrame(
        [
            [" ", " ", " ", "X"],
            [" ", " ", "M", " "],
            [" ", "A", " ", " "],
            ["S", " ", " ", " "],
        ]
    ),
    pd.DataFrame(
        [
            ["S", "A", "M", "X"],
        ]
    ),
    pd.DataFrame(
        [
            ["S", " ", " ", " "],
            [" ", "A", " ", " "],
            [" ", " ", "M", " "],
            [" ", " ", " ", "X"],
        ]
    ),
    pd.DataFrame(
        [
            ["S"],
            ["A"],
            ["M"],
            ["X"],
        ]
    ),
    pd.DataFrame(
        [
            [" ", " ", " ", "S"],
            [" ", " ", "A", " "],
            [" ", "M", " ", " "],
            ["X", " ", " ", " "],
        ]
    ),
]
X_MASkernels = [
    pd.DataFrame(
        [
            ["M", " ", "M"],
            [" ", "A", " "],
            ["S", " ", "S"],
        ]
    ),
    pd.DataFrame(
        [
            ["M", " ", "S"],
            [" ", "A", " "],
            ["M", " ", "S"],
        ]
    ),
    pd.DataFrame(
        [
            ["S", " ", "S"],
            [" ", "A", " "],
            ["M", " ", "M"],
        ]
    ),
    pd.DataFrame(
        [
            ["S", " ", "M"],
            [" ", "A", " "],
            ["S", " ", "M"],
        ]
    ),
]
XMAScounter = 0
X_MAScounter = 0


def isMatch(crossword, ccol, crow, kernel):
    [krows, kcols] = kernel.shape
    overlapCrossword = crossword.iloc[
        crow : min(crows, krows + crow),
        ccol : min(ccols, kcols + ccol),
    ]
    if overlapCrossword.shape != kernel.shape:
        return False
    matches = pd.DataFrame(overlapCrossword.values == kernel.values)
    matchesRequired = kernel.map(lambda val: val != " ").sum().sum()
    if matches.sum().sum() == matchesRequired:
        return True
    return False


[crows, ccols] = crossword.shape
for ccol in range(ccols):
    for crow in range(crows):
        for kernel in XMASkernels:
            if isMatch(crossword, ccol, crow, kernel):
                XMAScounter += 1
        for kernel in X_MASkernels:
            if isMatch(crossword, ccol, crow, kernel):
                X_MAScounter += 1


print(XMAScounter)
print(X_MAScounter)
