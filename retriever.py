from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

from logger import get_logger

logger = get_logger(__name__)


# base_url = "https://www.kaggle.com/api/v1"
# dataset_version = "115"
# url = f"{base_url}/datasets/download/{owner_slug}/{dataset_slug}?datasetVersionNumber={dataset_version}"

owner_slug = "datasnaek"
dataset_slug = "youtube-new"

RAW_DATA_PATH = Path("data/raw")
DATASET = f"{owner_slug}/{dataset_slug}"


def retrieve_dataset() -> None:
    """
    Retrieve Dataset from Kaggle
    """

    api = KaggleApi()
    api.authenticate()

    logger.info("Check & Download Dataset..")
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    api.dataset_download_files(DATASET, path=RAW_DATA_PATH, force=True, unzip=True)

    logger.info("Downloaded Dataset!")
