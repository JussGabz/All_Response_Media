from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from logger import get_logger

logger = get_logger(__name__)


def plot_top_categories(df: pd.DataFrame, path: Union[str, Path]) -> None:
    logger.info("Plotting Graph")

    df["views"] = pd.to_numeric(df["views"], errors="coerce")
    df_top = (
        df.groupby("category_name")["views"].sum().sort_values(ascending=False).head(10)
    )

    sns.barplot(x=df_top.values, y=df_top.index)
    plt.xlabel("Total Views")
    plt.title("Top 10 Categories by Views")
    plt.tight_layout()
    plt.savefig(path)

    logger.info(f"Graph exported to {path}")
