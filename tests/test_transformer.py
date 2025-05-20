import json
from pathlib import Path

import pandas as pd
import pytest

from transformer import transform_data  # replace with your actual module name


@pytest.fixture
def sample_csv(tmp_path):
    csv_content = """video_id,category_id,title
1,10,Test Video 1
2,20,Test Video 2
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    return csv_file


@pytest.fixture
def sample_json(tmp_path):
    json_content = {
        "items": [
            {"id": "10", "snippet": {"title": "Music"}},
            {"id": "20", "snippet": {"title": "Sports"}},
        ]
    }
    json_file = tmp_path / "categories.json"
    json_file.write_text(json.dumps(json_content))
    return json_file


def test_transform_data(sample_csv, sample_json):
    df = transform_data(sample_csv, sample_json)

    # Check that new column 'category_name' is created correctly
    expected = ["Music", "Sports"]
    assert df["category_name"].tolist() == expected

    # Check original columns still present
    assert "video_id" in df.columns
    assert "category_id" in df.columns
    assert "title" in df.columns
