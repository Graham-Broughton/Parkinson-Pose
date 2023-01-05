from dotenv import load_dotenv
load_dotenv('././kaggle.env')

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import src.data_scripts.get_dataset as get_data
def get_data():
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('LIMI44/parkinsons-visionbased-pose-estimation-dataset', path='./data_files', unzip=True)