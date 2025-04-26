import pytest
import pandas as pd
from ingestion.IngestorServices import load_csv
import os

# Test data paths
TEST_CSV_PATH = "./data/test_csv.csv"
INVALID_CSV_PATH = "./data/nonexistent_file.csv"


class TestCSVLoading:
    """Test suite for CSV loading functionality"""

    def test_load_csv_returns_dataframe(self):
        """Test that load_csv returns a pandas DataFrame for valid CSV"""
        result = load_csv(TEST_CSV_PATH)
        assert isinstance(result, pd.DataFrame), "Returned object should be a pandas DataFrame"
        assert not result.empty, "DataFrame should not be empty for valid CSV"

    def test_load_csv_nonexistent_file(self):
        """Test that load_csv handles non-existent files appropriately"""
        with pytest.raises(FileNotFoundError):
            load_csv(INVALID_CSV_PATH)

    def test_load_csv_invalid_file(self, tmp_path):
        """Test that load_csv handles invalid CSV files appropriately"""
        # Create a temporary non-CSV file
        invalid_file = tmp_path / "invalid.txt"
        invalid_file.write_text("This is not a CSV file")

        with pytest.raises(pd.errors.EmptyDataError):
            load_csv(str(invalid_file))

    def test_load_csv_empty_file(self, tmp_path):
        """Test that load_csv handles empty CSV files appropriately"""
        # Create a temporary empty CSV file
        empty_file = tmp_path / "empty.csv"
        empty_file.write_text("")

        with pytest.raises(pd.errors.EmptyDataError):
            load_csv(str(empty_file))


if __name__ == '__main__':
    pytest.main()