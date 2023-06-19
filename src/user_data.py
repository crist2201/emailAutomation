import pandas as pd


class Data:

    def __init__(self):
        """
        Constructor, only init the file path
        """
        self.data_path = "resources/templates/data/{name_file}.xlsx"

    def get_users_data(self, file_name):
        """
        Function to get users data to replace the templates
        :param file_name: Users data
        :return: Dataframe with all the data
        """
        data_header = 0
        data_file = str.format(self.data_path, name_file=file_name)
        return pd.read_excel(data_file, header=data_header)
