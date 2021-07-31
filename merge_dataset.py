import os
import pandas as pd

data_folder = 'Dataset'
cd = os.getcwd()
directory = '{}/{}'.format(cd, data_folder)


all_csv = os.listdir(directory)

all_df = []
for file in all_csv:
    df = pd.read_csv('{}/{}'.format(directory, file), parse_dates=True)
    all_df.append(df)

phasor_data = pd.concat(all_df)

merged_folder = 'MergedDataset'

if not os.path.exists(merged_folder):
    os.makedirs(merged_folder)

phasor_data.to_csv('{}/full_dataset.csv'.format(merged_folder), index=False)
print("Dataset Merge Complete")
