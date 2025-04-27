"""-------------------------------------------------------
PROJECT-NAME: Testing Ingestion Services
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    time
Version:  1.0.9
__updated__ = Sat Apr 26 2025
-------------------------------------------------------
"""

import pytest
from ingestion.IngestorServices import load_csv
import pandas as pd

csv_file = "data/test_csv.csv"
csv_file_non_existent = "data/test_csv_file.csv"


def test_loading_csv():
    assert isinstance(load_csv(csv_file), pd.DataFrame)


def test_loading_non_existent_csv():
    with pytest.raises(FileNotFoundError):
        load_csv(csv_file_non_existent)
