import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    df = pd.read_csv("medical_examination.csv")
    
    # Add overweight column
    df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)
    
    # Normalize cholesterol and glucose: 0 = good, 1 = bad
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)
    
    return df

def draw_cat_plot(df):
    # Convert data into long format
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    # Create the catplot
    g = sns.catplot(
        x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat
    )
    
    fig = g.fig
    return fig

def draw_heat_map(df):
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Compute the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5, cmap="coolwarm", ax=ax)
    
    return fig

if __name__ == "__main__":
    df = load_data()
    cat_plot = draw_cat_plot(df)
    heat_map = draw_heat_map(df)
    
    cat_plot.savefig("catplot.png")
    heat_map.savefig("heatmap.png")
