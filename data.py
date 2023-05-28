import pandas as pd
import template_factory
import os


class Data(template_factory.Template):

    def __init__(self):
        super().__init__()
        self.template = self.set_data()
        self.path = os.path.join(self.set_path(), "data/{name_file}.xlsx")

    def get_users_data(self):
        data_header = 2
        return pd.read_excel(self.get_file(), header=data_header)
