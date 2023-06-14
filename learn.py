# Import pandas package
import pandas as pd

# create a dictionary with five fields each
data = {
	'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
	'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
	'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
	'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
	'E': ['E1', 'E2', 'E3', 'E4', 'E5']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Remove two columns name is 'C' and 'D'
del df["C"]

# df.drop(columns =['C', 'D'])
print(df)