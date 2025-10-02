
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


def create_projection(combined_frame: pd.DataFrame) -> pd.DataFrame:
    combined_frame = combined_frame.copy()

    # I need to subset onto the most recent vintage
    # The revisions of the different datapoints are not independent, so we cant really use them as training data. 
    # The model would get much too confident.
    most_recent_vintage = combined_frame["vintage"].max()
    timeseries = combined_frame.loc[combined_frame["vintage"]== most_recent_vintage,["month", "vacancies"]].set_index("month").squeeze()

    # Given the lack of time, and the request for a simple model, I'm just going to start with a vanilla SARIMA model.
    # The pandemic is going to be an issue, mind you. 
    model = SARIMAX(
        timeseries, 
        order=(3, 1, 1), 
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    # Fit the model on the observations we have
    results = model.fit()

    # Project out for 12 months
    projection = results.get_forecast(steps=24)

    return projection.predicted_mean