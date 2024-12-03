import pandas as pd

inputTable = pd.read_csv(
    "./day1/HistorianHysteriaInput.txt",
    sep="   ",
    header=None,
    names=["1", "2"],
    engine="python",
)
sortedTable = pd.concat(
    [
        inputTable["1"].sort_values(ignore_index=True),
        inputTable["2"].sort_values(ignore_index=True),
    ],
    axis=1,
)
difference = abs(sortedTable["1"] - sortedTable["2"]).sum()
print("difference score:", difference)

countTable = pd.merge(
    left=inputTable["2"].value_counts(),
    right=inputTable["1"],
    left_on="2",
    right_on="1",
)
similarity = (countTable["1"] * countTable["count"]).sum()
print("similarity score:", similarity)
