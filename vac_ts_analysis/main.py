
import pandas as pd

from vac_ts_analysis import ingest, preprocessing, visualisation

DATA_SOURCE_URL = "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/ap2y/lms/previous"

MONTHS_TO_PLOT = [
    "2025-01-01",
    "2024-07-01",
    "2024-01-01",
    "2023-07-01",
    "2023-01-01",
    "2022-07-01",
    "2022-01-01"
]

def main() -> None:
    
    # 1. Data ingest from target website
    raw_data = ingest.download_all_data(DATA_SOURCE_URL, number_of_files=20)

    # 2. Preprocessing and combination of frames
    combined_frame = preprocessing.preprocess_and_combine(raw_data)

    # 3. Visualisation
    #visualisation.visualise_data(combined_frame)
    for month in MONTHS_TO_PLOT:
        visualisation.plot_revisions_single_month(combined_frame, month=month)

    return

if __name__ == "__main__":
    main()
