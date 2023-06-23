import os
import pandas as pd


class Data:

    def __init__(self):
        """
        Constructor, only init the file path
        """
        self.data_path = '{file}.xlsx'

    def get(self, path, file_name, sheet):
        """
        Function to get users data to replace the templates
        :param sheet: Sheet name
        :param path: Users data path
        :param file_name: Users data
        :return: Dataframe with all the data
        """
        data_header = 0
        data_file = str.format(os.path.join(path, self.data_path), file=file_name)
        return pd.read_excel(data_file, sheet_name=sheet, header=data_header)
