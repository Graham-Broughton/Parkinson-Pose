from src.data_scripts.get_dataset import get_data
import os
import shutil

# get_data()
# os.rename('data/UDysRS_UPDRS_Export', 'tmp/')
# shutil.rmtree('data/')
# os.rename('tmp/', 'data/')
for file in os.listdir('data/'):
    if not file.endswith(('LICENSE.txt', '.ipynb')):
        os.rename(f'data/{file}', f'data/{file[:-3]}json')