from PrintQueueInput import rules, lists

beforeRules = dict()
afterRules = dict()
for rule in rules.splitlines():
    [before, after] = rule.split("|", 1)
    if before in beforeRules:
        beforeRules[before].add(after)
    else:
        beforeRules[before] = set([after])
    if after in afterRules:
        afterRules[after].add(before)
    else:
        afterRules[after] = set([before])


def ruleBroken(value, i, values):
    valuesBefore = values[:i]
    valuesAfter = values[i + 1 :]
    if value in beforeRules:
        valuesBreakingBeforeRules = list(
            filter(lambda valueBefore: valueBefore in beforeRules[value], valuesBefore)
        )
        if len(valuesBreakingBeforeRules) > 0:
            return True, values.index(valuesBreakingBeforeRules[0])
    if value in afterRules:
        valuesBreakingAfterRules = list(
            filter(lambda valueAfter: valueAfter in afterRules[value], valuesAfter)
        )
        if len(valuesBreakingAfterRules) > 0:
            return True, values.index(valuesBreakingAfterRules[0])
    return False, 0


def isInOrder(values):
    for i, value in enumerate(values):
        unordered, _ = ruleBroken(value, i, values)
        if unordered:
            return False
    return True


def getMiddleValue(values):
    return int(values[int((len(values) - 1) / 2)])


def getAlreadyOrderedMiddleValue(line):
    values = line.split(",")
    if isInOrder(values):
        return getMiddleValue(values)
    return 0


def swapValues(values, i1, i2):
    if i1 > i2:
        i1, i2 = i2, i1
    return [
        *values[:i1],
        values[i2],
        *values[i1 + 1 : i2],
        values[i1],
        *values[i2 + 1 :],
    ]


def orderValues(values):
    for i, value in enumerate(values):
        unordered, swapIndex = ruleBroken(value, i, values)
        if unordered:
            swappedValues = swapValues(values, i, swapIndex)
            return orderValues(swappedValues)
    return values


def getReOrderedMiddleValue(line):
    values = line.split(",")
    if isInOrder(values):
        return 0
    orderedValues = orderValues(values)
    return getMiddleValue(orderedValues)


orderedMiddles = list(map(getAlreadyOrderedMiddleValue, lists.splitlines()))
print(sum(orderedMiddles))

reorderedMiddles = list(map(getReOrderedMiddleValue, lists.splitlines()))
print(sum(reorderedMiddles))
