import pandas as pd
import warnings
from typing import Iterable

class AlignData:
    """
    Align multiple time-series datasets by cropping to their overlapping time interval,
    while preserving each dataset's original timestamps and values.

    Important:
    - This class does **not** interpolate, resample, or add artificial timestamps.
    - Only a cropping function is implemented, so all original timestamp-value pairs
      within the overlapping interval are kept exactly as in the input.

    Features:
    - Crops all datasets to the interval where all datasets overlap in time.
    - Original timestamps and values are preserved.
    - Non-increasing timestamps are automatically removed.
    - Outputs share the same column names as the inputs.
    - If there is no temporal overlap, datasets are returned un-cropped with a warning.
    """

    def __init__(self):
        pass

    def align(self, dfs: Iterable[pd.DataFrame]) -> tuple[pd.DataFrame, ...]:
        if not isinstance(dfs, (list, tuple)) or len(dfs) < 1:
            raise ValueError("Provide at least one DataFrame")

        clean_dfs = []
        starts, ends = [], []

        # Clean datasets and record start/end times
        for df in dfs:
            df = df.copy()
            if 'time' not in df.columns:
                raise ValueError("Each DataFrame must have a 'time' column")
            df['time'] = pd.to_datetime(df['time'])
            # Remove non-increasing timestamps
            df = df[df['time'].diff().fillna(pd.Timedelta(seconds=1)) > pd.Timedelta(0)]
            df = df.reset_index(drop=True)
            if df.shape[0] == 0:
                warnings.warn(
                    "One of the input DataFrames became empty after removing non-increasing timestamps.",
                    UserWarning
                )
            clean_dfs.append(df)
            if df.shape[0] > 0:
                starts.append(df['time'].iloc[0])
                ends.append(df['time'].iloc[-1])
            else:
                starts.append(pd.Timestamp.max)
                ends.append(pd.Timestamp.min)

        # Determine overlapping window
        latest_start_overlap = max(starts)
        earliest_end_overlap = min(ends)

        aligned_dfs = []
        for df in clean_dfs:
            if latest_start_overlap > earliest_end_overlap:
                warnings.warn("No temporal overlap between datasets. Returning un-cropped data.", UserWarning)
                df_aligned = df.copy()
            else:
                # Crop to overlapping window
                df_aligned = df[
                    (df['time'] >= latest_start_overlap) &
                    (df['time'] <= earliest_end_overlap)
                ].reset_index(drop=True)

            aligned_dfs.append(df_aligned)

        return tuple(aligned_dfs)
