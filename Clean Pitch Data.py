import pandas as pd

df = pd.read_csv("2019_pitches.csv")

# write necessary columns to new csv
selectedColumns = [29, 33, 34]
df_selected = df.iloc[:, selectedColumns]

df_selected.to_csv('cleanedPitches.csv', index=False)

