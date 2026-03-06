import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # 1
    df = pd.read_csv("epa-sea-level.csv")

    # 2
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", s=10)

    # 3
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    x_pred = pd.Series([i for i in range(1880, 2051)])
    # y = mx + c formülüyle tahmin edilen değerleri hesapla
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, "r", label="Best Fit Line 1")

    # 4
    new_df = df[df["Year"] >= 2000]
    res_new = linregress(new_df["Year"], new_df["CSIRO Adjusted Sea Level"])

    x_pred_new = pd.Series([i for i in range(2000, 2051)])
    y_pred_new = res_new.slope * x_pred_new + res_new.intercept
    plt.plot(x_pred_new, y_pred_new, "green", label="Best Fit Line 2")

    # 5
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    plt.savefig("sea_level_plot.png")
    return plt.gca()
