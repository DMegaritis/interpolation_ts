from interpolation_ts.interpolation import Interpolation
import pandas as pd
import os
from utils.ploter import plot_interp
import matplotlib.pyplot as plt
from pathlib import Path

# Path to the parent directory of your script
parent_path = Path(__file__).resolve().parent.parent  # goes from examples/script -> project root

# Path to the data folder
data_path = parent_path / "examples" / "data"

# Load CSVs
df1 = pd.read_csv(data_path / "df1.csv")
df2 = pd.read_csv(data_path / "df2.csv")
df3 = pd.read_csv(data_path / "df3.csv")
df4 = pd.read_csv(data_path / "df4.csv")

# Ploting:
plot_interp([df1, df2, df3, df4], labels=['df1', 'df2', 'df3', 'df4'])


# Call interpolation
dfs = [df1, df2, df3, df4]
interpolated = Interpolation().interpolate(dfs, overlap_windows=True)

df1_interpolated, df2_interpolated, df3_interpolated, df4_interpolated = interpolated

plot_interp([df1_interpolated, df2_interpolated, df3_interpolated, df4_interpolated], labels=['df1', 'df2', 'df3', 'df4'])

