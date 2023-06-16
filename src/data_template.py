import pandas as pd
from src import file_factory
import os


class Data:

    def __init__(self):
        pass
        #super().__init__()
        #self.data_template = self.get_properties("data_template")
        #self.data_path = os.path.join(self.path, "data/{name_file}.xlsx")

    @staticmethod
    def get_users_data(file_name, path):
        data_header = 2
        data_file = str.format(path, name_file=file_name)
        return pd.read_excel(data_file, header=data_header)
