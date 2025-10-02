
from typing import Dict
import pandas as pd
import copy
from datetime import datetime

MONTH_PATTERN = r"^\d{4}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)$"

def preprocess_and_combine(raw_data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Takes a dictionary of raw tables, with dates as keys. Clean, combine and return. 
    Gets the vintage from the "Release date" row in the table. 

    Args:
        raw_data (Dict[str, pd.DataFrame]): A dictionary mapping from vintage to the relevant dataframe. 

    Returns:
        pd.DataFrame: A dataframe with columns (vintage, month, vacancies). 
    """
    raw_data = copy.deepcopy(raw_data)

    combined_frame = pd.DataFrame()
    for df in raw_data.values():

        # I am going to use the file release date for the vintage and not the dates from the website.
        # Largely because the most recent just has date "Latest" on the website. 
        release_date = df.loc[df["Title"]=="Release date", "UK Vacancies (thousands) - Total"].iloc[0]
        release_date = datetime.strptime(release_date, "%d-%m-%Y")
        
        # Use a regex to identify the rows corresponding to months.
        month_pattern = MONTH_PATTERN
        df = df.loc[df["Title"].str.match(month_pattern, case=False, na=False), :]

        # Rename the columns
        df = df.rename(columns={
            "Title": "month",
            "UK Vacancies (thousands) - Total": "vacancies"
        })

        # Convert the month to a datetime object
        df["month"] = pd.to_datetime(df["month"], format="%Y %b")

        # Create a column for the vintage
        df["vintage"] = release_date

        # Add to the combined frame
        combined_frame = pd.concat([combined_frame, df], axis=0)

    return combined_frame[["vintage", "month", "vacancies"]]