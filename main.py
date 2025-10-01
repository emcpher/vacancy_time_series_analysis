
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

DATA_SOURCE_URL = "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/ap2y/lms/previous"

def main() -> None:
    
    response = requests.get(DATA_SOURCE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # all links will be under <a> tags
    print("Scraping target url.")
    csv_download_tags = soup.find_all('a', {"data-gtm-type": "download-version-csv"})
    for tag in csv_download_tags:
        link = tag.get('href')
        full_url = urljoin(DATA_SOURCE_URL, link)
        download_response = requests.get(full_url)
        data = dict()
        if download_response.status_code == 200:
            # Convert CSV text to a pandas DataFrame
            csv_data = StringIO(download_response.text)
            df = pd.read_csv(csv_data, on_bad_lines='skip')
            date = tag.get('data-gtm-date')
            data[date] = df

    return

if __name__ == "__main__":
    main()
