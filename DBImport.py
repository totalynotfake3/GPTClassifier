# Import File
import os
from pymongo import MongoClient
import pandas as pd


def load_csv_data_to_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['New']
    collection = db['New']

    # Just load through all documents here
    skip_first = True

    for root, dirs, files in os.walk("data"):
        # Iterate through the files
        for name in files:
            # Get the file path
            file_path = os.path.join(root, name)
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
                temp = df.to_dict(orient='records')
                for i in temp:
                    collection.insert_one(i)



