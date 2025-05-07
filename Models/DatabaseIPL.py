"""-------------------------------------------------------
PROJECT-NAME: IPL Cricket Data Analysis Module
-------------------------------------------------------
Author: JD
ID: 91786
Uses: pandas, os
Version: 1.0.9
__updated__ = Mon Apr 28 2025
-------------------------------------------------------
"""

import os
import pandas as pd


class Database:
    """Base database class providing common database operations."""

    def __init__(self) -> None:
        """Initialize an empty DataFrame."""
        self._df = pd.DataFrame()  # Changed from __df to _df (protected instead of private)

    def get_number_of_records(self) -> int:
        """Return the number of records in the database.
        Returns:
            int: Number of records
        """
        return self._df.shape[0]

    @property
    def shape(self) -> tuple[int, int]:
        """Return the shape of the database (rows, columns).
        Returns:
            tuple: (number of rows, number of columns)
        """
        return self._df.shape

    @property
    def info(self):
        return self._df.info()


class DatabaseIPL(Database):
    """Database class specialized for IPL cricket data."""
    def __init__(self, csv_files: list[str]) -> None:  # Changed list[int] to list[str]
        """Initialize the database by loading IPL data from CSV files.
        Args:
            csv_files: List of paths to CSV files containing IPL data
        """
        super().__init__()  # Initialize parent class
        for file in csv_files:
            if not os.path.exists(file):
                raise FileNotFoundError(f"CSV file not found: {file}")
            df = pd.read_csv(file)
            self._df = pd.concat([self._df, df], ignore_index=True)

    def get_all_players(self) -> list[str]:
        players = list(self._df.striker.unique())+list(self._df.bowler.unique())+list(self._df.fielder.unique())
        return players
    def get_player_count(self)->int:
        return len(self.get_all_players())

    def get_players_per_season(self):
        df = self._df.groupby(by="season",as_index=False)

if __name__ == "__main__":

    file_paths = [
        f"../data/cricketData/ipl_{year}_deliveries.csv"
        for year in range(2022, 2026)
    ]

    try:
        db = DatabaseIPL(file_paths)
        print(f"Number of records: {db.get_number_of_records():,d}")
        print(f"Database shape: {db.shape}")
        print(f"\Database Info: {db.info}")
        print(f"Database All Players: {db.get_all_players()}")
        print(f"Number Of total Players: {db.get_player_count()}")
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
