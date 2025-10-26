# interpolation_ts

This repository provides tools for **aligning and interpolating time-series data from wearable sensors**. It is designed for datasets where timestamps may not perfectly match across devices or recordings.  

## Features

### 1. Interpolation (`Interpolation` class)
- Aligns multiple datasets to a **uniform time grid** using **PCHIP interpolation**.
- Preserves original sample values at their nearest grid points to avoid distorting the signal.
- Handles datasets with arbitrary column names, as long as a `time` column exists.
- Optional cropping to overlapping windows across datasets.
- Automatically removes non-increasing timestamps.
- Useful when a consistent sampling rate is needed for signal processing or modeling.
- Interpolation smooths the signal, but original values are injected to preserve peaks as much as possible.

---

### 2. Cropping / Original Alignment (`AlignData` class)
- Aligns datasets **by cropping to their overlapping time interval**.
- Preserves all original timestamps and values **without interpolation or resampling**.
- Automatically removes non-increasing timestamps.
- Useful for comparing multiple datasets while keeping all original data points intact.
- Only cropping is implemented; no new timestamps are created (original timestamps are kept).

---
