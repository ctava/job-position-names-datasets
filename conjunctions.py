import json
import logging
import pathlib
import pandas as pd

class Conjunctions:
    '''Stores conjunctions so you dont have to.'''
    def __init__(self):
        self.name = "conjunctions"
        self.logger = logging.getLogger(f"{self.name}")
        self.logger.setLevel(logging.ERROR)
        self.file_path = pathlib.Path(__file__).parent.resolve()
        self.config_file = pathlib.Path(self.file_path) / f"{self.name}.csv"
        #self.config_file = pathlib.Path(self.file_path) / f"{self.name}.json"

    def get_data(self):
        dtype={'Name': 'string'}
        df = pd.read_csv(self.config_file,dtype=dtype)
        return df['Name']
        #self.data = self.load_json(self.config_file)
        #return self.data['data']

    def load_json(self,filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data