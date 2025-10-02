
import os
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

plt.style.use("seaborn-v0_8-dark")

PLOT_DIR = "plots"


def plot_revisions_single_month(combined_frame: pd.DataFrame, month: str) -> None:
    """Create visualisations of the data. I imagine a heavy reliance on matplotlib and seaborn.
    No return value. Plots will be saved into the /plots/ folder.  

    Args:
        combined_frame (pd.DataFrame): A frame with columns (vintage, month, vacancies).
    """
    combined_frame = combined_frame.copy()

    # Starting with a target month, visualise all the vintages for the value.
    one_month = combined_frame.loc[combined_frame["month"]==month, :]

    # Create a Figure and Axes object
    fig, ax = plt.subplots()

    # Plot on the Axes
    ax.plot(one_month["vintage"], one_month["vacancies"], marker="o", linestyle="-")

    # Add labels and title
    ax.set_xlabel("Vintage")
    ax.set_ylabel("Vacancies (thousands)")
    ax.set_title("Vacancies for 2021-01")
    
    # Fix the x-ticks
    ax.set_xticks(one_month["vintage"])
    ax.set_xticklabels(ax.get_xticks(), rotation=90)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%b"))

    # Sort gridlines
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)  # horizontal
    ax.xaxis.grid(False)  

    # Save the figure as a PNG
    fig.savefig(os.path.join(PLOT_DIR, f"revisions_singlemonth_{month}.png"))

    return

def plot_projection(combined_frame: pd.DataFrame, projection: pd.Series) -> None:
    combined_frame = combined_frame.copy()
    projection = projection.copy()

    most_recent_vintage = combined_frame["vintage"].max()
    timeseries = combined_frame.loc[combined_frame["vintage"]== most_recent_vintage,["month", "vacancies"]].set_index("month").squeeze()

    # Create a Figure and Axes object
    fig, ax = plt.subplots()

    # Plot the actuals
    ax.plot(timeseries, marker="o", linestyle="-", color="b", label=f"actuals from {most_recent_vintage}")

    # Plot the projection
    ax.plot(projection, marker="o", linestyle="-", color="r", label=f"projection")

    # Add labels and title
    ax.set_xlabel("Month")
    ax.set_ylabel("Vacancies (thousands)")
    ax.set_title("Vacancies")
    
    # Sort gridlines
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)  # horizontal
    ax.xaxis.grid(False)  

    # Add legend
    ax.legend()

    # Save the figure as a PNG
    fig.savefig(os.path.join(PLOT_DIR, f"projection.png"))

    return