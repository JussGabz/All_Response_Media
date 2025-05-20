import json
from pathlib import Path
from typing import Union

import pandas as pd

from logger import get_logger

logger = get_logger(__name__)


def transform_data(
    csv_path: Union[str, Path], json_path: Union[str, Path]
) -> pd.DataFrame:
    """
    Transform raw data and returns DataFrame
    """

    logger.info("Transform Data...")

    df = pd.read_csv(csv_path)

    with open(json_path) as f:
        categories = json.load(f)

    # Creates a category map for each category in json file
    category_map = {
        int(item["id"]): item["snippet"]["title"] for item in categories["items"]
    }

    df["category_name"] = df["category_id"].map(category_map)

    logger.info("Transformed Data!")

    return df
