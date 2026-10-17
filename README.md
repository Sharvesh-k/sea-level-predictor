# Sea Level Predictor

A Python data visualization project that analyzes historical global sea-level measurements and predicts future sea-level rise through 2050.

## Project Overview

This project uses data from the US Environmental Protection Agency (EPA) to visualize historical sea-level changes and apply linear regression to estimate future trends.

## Features

- **Historical Data Visualization:** Creates a scatter plot of global average sea-level measurements.
- **Long-Term Prediction:** Fits a line of best fit using all available data and extends it to 2050.
- **Recent Trend Prediction:** Fits a second line using data from the year 2000 onward and extends it to 2050.
- **Data Analysis:** Uses SciPy linear regression to calculate trend lines.

## Technologies Used

- Python
- Pandas
- Matplotlib
- SciPy

## Project Files

- `sea_level_predictor.py` — Data analysis and visualization code.
- `main.py` — Runs the project.
- `epa-sea-level.csv` — Historical sea-level dataset.
- `test_module.py` — Unit tests.

## How to Run

Install the required libraries:

```bash
py -3.13 -m pip install --only-binary=:all: pandas matplotlib scipy
```

Generate the visualization:

```bash
py -3.13 main.py
```

Run the tests:

```bash
py -3.13 -m unittest test_module.py
```

## Generated Output

The project generates `sea_level_plot.png`, containing historical measurements and two regression lines projecting trends through 2050.

## Learning Outcomes

- Reading and analyzing CSV data with Pandas
- Creating scatter plots with Matplotlib
- Applying linear regression with SciPy
- Comparing long-term and recent trends
- Testing Python functions with `unittest`

## Author

Sharvesh K
