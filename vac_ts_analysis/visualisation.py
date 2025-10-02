
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

def plot_all_revisions(combined_frame: pd.DataFrame) -> None:
    """Plot all revisions overlaid. The entire being to shift all the series so that they all share one x-axis value for a "finished" value.
    You could then see their paths to the "finised" value overlaid. It would look a bit like a fan chart. 

    Args:
        combined_frame (pd.DataFrame): A frame with columns (vintage, month, vacancies).
    """
    combined_frame = combined_frame.copy()

    combined_frame["vintage_months_after_observation"] = combined_frame["vintage"] - combined_frame["month"]

    # Create a Figure and Axes object
    fig, ax = plt.subplots()

    months = combined_frame["month"].unique()
    for month in months[:20]:

        # Get the month's data
        month_data = combined_frame.loc[combined_frame["month"]==month, ["vintage_months_after_observation", "vacancies"]].set_index("vintage_months_after_observation").squeeze()

        # Plot the actuals
        ax.plot(month_data, marker="o", linestyle="-", color="b", label=f"revisions for: {month}")


    # Add labels and title
    ax.set_xlabel("Publication delay")
    ax.set_ylabel("Vacancies (thousands)")
    ax.set_title("Vacancies")
    
    # Sort gridlines
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)  # horizontal
    ax.xaxis.grid(False)  

    # Save the figure as a PNG
    fig.savefig(os.path.join(PLOT_DIR, f"revisions_allmonths.png"))

    # TODO - get all the series on a similar scale so that you can compare them! Doesn't quite work as-is.

    return 

def plot_projection(combined_frame: pd.DataFrame, projection: pd.Series) -> None:
    """Plot the actuals and the projection against each other. Save in /plots/ 

    Args:
        combined_frame (pd.DataFrame): A dataframe of the various historic actuals.
        projection (pd.Series): The projection
    """
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