import os
from csv import DictReader
import pandas as pd


PATH = os.getenv("FILEPATH")

def read_archive():
    data = []
    file = pd.read_excel(PATH)

    for i, row in file.iterrows():
        data.append(str(row))
    return data
