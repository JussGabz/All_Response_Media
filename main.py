from pathlib import Path

from graph import plot_top_categories
from retriever import RAW_DATA_PATH, retrieve_dataset
from transformer import transform_data

csv_file_name = "GBvideos.csv"
json_file_name = "GB_category_id.json"


def main() -> None:
    retrieve_dataset()

    csv_path = Path(RAW_DATA_PATH, csv_file_name)
    json_path = Path(RAW_DATA_PATH, json_file_name)

    df = transform_data(csv_path=csv_path, json_path=json_path)

    plot_top_categories(df, "data/processed/")


main()
