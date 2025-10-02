
import pandas as pd

from vac_ts_analysis import ingest

DATA_SOURCE_URL = "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/ap2y/lms/previous"

def main() -> None:
    
    raw_data = ingest.download_all_data(DATA_SOURCE_URL, number_of_files=20)

    return

if __name__ == "__main__":
    main()
