"""Module for csv_ingestor functionality."""


import pandas as pd
import logging
import requests

logger = logging.getLogger(__name__)




def load_csv(file_path:str)->pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def fetch_api_data(endpoint:str)->pd.DataFrame:
    response = requests.get(endpoint)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    logger.info(f"Successfully fetched data from API: {endpoint}")
    return df