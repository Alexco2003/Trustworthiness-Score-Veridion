import pandas as pd
import os

def read_images_from_directory():
    count = 1
    directory = "datasets"
    for file in os.listdir(directory):
        if file.endswith(".parquet"):
            file_path = os.path.join(directory, file)
            df = pd.read_parquet(file_path)
            csv_file_path = f'dataset{count}.csv'
            df.to_csv(csv_file_path, index=False)
            count += 1
    return

read_images_from_directory()
