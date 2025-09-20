# Flowchart Experiments

This directory contains different experimental approaches for achieving consistent node widths in the PyScript flowchart application.

## Files

### `intermediate_version.py`
- Intermediate version with some fixes
- Contains debugging output and various width calculation attempts
- Shows the evolution of the approach

### `rectangle_patches_approach.py`
- Uses `matplotlib.patches.Rectangle` for drawing consistent-width boxes
- Attempts to measure text width using `get_window_extent()`
- Hit coordinate limits in PyScript environment
- Shows the graphic measurement approach that didn't work in PyScript

## Current Solution

The final solution in `main.py` uses character padding with monospace font, which proved to be the most reliable approach for the PyScript environment.

## Key Learnings

1. **Character padding** works better than graphic measurement in PyScript
2. **Monospace font** is essential for accurate character-based width calculation
3. **PyScript has coordinate limits** that prevent very wide rectangles
4. **Even padding distribution** creates better visual balance
