import pandas as pd
import file_factory
import os


class Data(file_factory.Files):

    def __init__(self):
        super().__init__()
        self.data_template = self.get_properties("data_template")
        self.data_path = os.path.join(self.path, "data/{name_file}.xlsx")

    def get_users_data(self):
        data_header = 2
        data_file = str.format(self.data_path, name_file=self.data_template)
        return pd.read_excel(data_file, header=data_header)
