from datetime import datetime
import pandas as pd
import time
import os

def pre_processed_data():

    actual_date = datetime.today().strftime("%d-%m-%y")
    path = os.getcwd().split('\\scripts')[0]
    origin_filename = f"\\raw_data\\IBOVDia_{actual_date}.csv"
    target_filename = f"\\pre_processed\\data_{actual_date}.parquet"

    df = pd.read_csv(path + origin_filename, skiprows=1, encoding='latin-1')

    df.to_parquet(path + target_filename, engine='pyarrow')

    return None