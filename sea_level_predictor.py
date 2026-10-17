
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years = pd.Series(range(1880, 2051))
    predictions = intercept + slope * years
    plt.plot(years, predictions, "r", label="Best fit line")

    # Create second line of best fit using data from 2000 onward
    recent_df = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )
    recent_years = pd.Series(range(2000, 2051))
    recent_predictions = intercept_recent + slope_recent * recent_years
    plt.plot(recent_years, recent_predictions, "g", label="Best fit line since 2000")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
