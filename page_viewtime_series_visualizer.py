import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    lower_bound = df["value"].quantile(0.025)
    upper_bound = df["value"].quantile(0.975)
    df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]
    return df

def draw_line_plot():
    df = load_and_clean_data()
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["value"], color='red', linewidth=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.grid(True)
    plt.savefig("line_plot.png")
    return plt

def draw_bar_plot():
    df = load_and_clean_data()
    df["year"] = df.index.year
    df["month"] = df.index.month
    df_bar = df.groupby(["year", "month"]).mean().unstack()
    df_bar.plot(kind="bar", figsize=(12, 6))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Average Daily Page Views per Month")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.savefig("bar_plot.png")
    return plt

def draw_box_plot():
    df = load_and_clean_data()
    df["year"] = df.index.year
    df["month"] = df.index.strftime('%b')
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x="year", y="value", data=df, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    sns.boxplot(x="month", y="value", data=df, order=months_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    plt.savefig("box_plot.png")
    return plt

if __name__ == "__main__":
    draw_line_plot().show()
    draw_bar_plot().show()
    draw_box_plot().show()
