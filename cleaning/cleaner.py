import pandas as pd
from ingestion.IngestorServices import load_csv


def perform_quick_eda(file_path:str)->None:
    df = load_csv(file_path)

    print("=" * 40)
    print(f"Quick EDA Report for: {file_path}")
    print("=" * 40)
    print(f"\nShape of Dataset: {df.shape[0]:,} rows × {df.shape[1]} columns\n")

    print("🔹 Dataset Info:")
    print("-" * 30)
    df.info()

    print("\n🔹 Summary Statistics:")
    print("-" * 30)
    print(df.describe(include='all'))

    print("\n🔹 Missing Values:")
    print("-" * 30)
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.any() else "No missing values found.")

    print("\n🔹 Sample Rows:")
    print("-" * 30)
    print(df.head())

    print("\nEDA complete.\n")



if __name__=="__main__":
    fp = "../data/cricketData/ipl_2022_deliveries.csv"
    perform_quick_eda(fp)

