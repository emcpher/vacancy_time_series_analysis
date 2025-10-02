
import time
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
from typing import Dict

# Two second wait
WAIT = 2

def download_all_data(url: str, number_of_files: int = 20) -> Dict[str, pd.DataFrame]:
    """_summary_

    Args:
        url (str): The main URL for the website.
        number_of_files (int, optional): The number of files we want to consider. Defaults to 20.

    Returns:
        Dict[str, pd.DataFrame]: A dictionary of the scraped files. Keys are the dates scraped from the website. 
        No real pre-processing done at this stage. 
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # all links will be under <a> tags
    print("Scraping target url.")
    csv_download_tags = soup.find_all('a', {"data-gtm-type": "download-version-csv"})
    raw_data = dict()
    for tag in csv_download_tags[:number_of_files]:
        link = tag.get('href')
        full_url = urljoin(url, link)
        time.sleep(WAIT)
        date = tag.get('data-gtm-date')
        print(f"Doing: {date}")
        download_response = requests.get(full_url)
        if download_response.status_code == 200:
            # Convert CSV text to a pandas DataFrame
            csv_data = StringIO(download_response.text)
            df = pd.read_csv(csv_data)
            raw_data[date] = df
        else: 
            raise requests.exceptions.RequestException("One of the requests is going wrong.")

    return raw_data 