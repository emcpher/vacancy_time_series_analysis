
import pandas as pd

from vac_ts_analysis import ingest, preprocessing

DATA_SOURCE_URL = "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/ap2y/lms/previous"

def main() -> None:
    
    # 1. Data ingest from target website
    raw_data = ingest.download_all_data(DATA_SOURCE_URL, number_of_files=20)

    # 2. Preprocessing and combination of frames
    combined_frame = preprocessing.preprocess_and_combine(raw_data)

    return

if __name__ == "__main__":
    main()
