import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')
    
    # First line of best fit (1880-2050)
    slope, intercept, _, _, _ = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051)
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line (1880-2050)')
    
    # Second line of best fit (2000-2050)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = stats.linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'g', label='Best Fit Line (2000-2050)')
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt

if __name__ == "__main__":
    draw_plot().show()
