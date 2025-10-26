from pathlib import Path
import pandas as pd
from utils.ploter import plot_interp

# Assuming you saved the AlignOriginalsOnly class as align_ts.py
from align_ts.align import AlignOriginalsOnly

# Path to the parent directory of your script
parent_path = Path(__file__).resolve().parent.parent

# Path to the data folder
data_path = parent_path / "examples" / "data"

# Load CSVs
df1 = pd.read_csv(data_path / "df1.csv")
df2 = pd.read_csv(data_path / "df2.csv")
df3 = pd.read_csv(data_path / "df3.csv")
df4 = pd.read_csv(data_path / "df4.csv")

print(df1, df2, df3, df4)

# Plot original data
plot_interp([df1, df2, df3, df4], labels=['df1', 'df2', 'df3', 'df4'])

# Align data using original timestamps only
dfs = [df1, df2, df3, df4]
aligned = AlignOriginalsOnly().align(dfs)

df1_aligned, df2_aligned, df3_aligned, df4_aligned = aligned

# Plot aligned data
plot_interp([df1_aligned, df2_aligned, df3_aligned, df4_aligned], labels=['df1', 'df2', 'df3', 'df4'])

print(df1_aligned, df2_aligned, df3_aligned, df4_aligned)