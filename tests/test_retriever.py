from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Import your function
from retriever import DATASET, RAW_DATA_PATH, retrieve_dataset


@patch("retriever.KaggleApi")
@patch("retriever.logger")
def test_retrieve_dataset(mock_logger, mock_kaggle_api):
    # Setup mocks
    api_instance = mock_kaggle_api.return_value
    api_instance.authenticate.return_value = None
    api_instance.dataset_download_files.return_value = None

    # Use a temp path for RAW_DATA_PATH
    temp_path = Path("/tmp/test_raw_data")
    # Patch RAW_DATA_PATH in your_module to avoid writing to actual path
    with patch("retriever.RAW_DATA_PATH", temp_path):
        retrieve_dataset()

    # Check that authenticate and download_files were called
    api_instance.authenticate.assert_called_once()
    api_instance.dataset_download_files.assert_called_once_with(
        DATASET, path=temp_path, force=True, unzip=True
    )

    # Check logs
    mock_logger.info.assert_any_call("Check & Download Dataset..")
    mock_logger.info.assert_any_call("Downloaded Dataset!")
