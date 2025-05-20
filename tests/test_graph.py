from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pytest
import seaborn as sns

from graph import plot_top_categories  # replace with your module


@pytest.fixture
def sample_df():
    data = {
        "category_name": ["Music", "Sports", "Gaming", "Music", "Sports"],
        "views": ["1000", "2000", "1500", "3000", "1000"],
    }
    return pd.DataFrame(data)


def test_plot_top_categories(tmp_path, sample_df):
    output_path = tmp_path / "plot.png"

    # Run the plotting function
    plot_top_categories(sample_df, output_path)

    # Check that file was created
    assert output_path.exists()
    assert output_path.stat().st_size > 0

    # Optionally, test plot contents by inspecting the figure (more advanced, not usually necessary)
    plt.close("all")  # Close plot to prevent memory leak in tests
