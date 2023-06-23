import pandas as pd


class Files:
    def __init__(self):
        """
        Constructor
        :param properties: Get all the properties
        :param config_file: All the configurations
        """
        self.config_file = pd.read_json("config/config.json").to_dict()

    def get_service(self, service):
        """
        Function to get service properties
        :return: Dictionary with the properties
        """
        return self.config_file["service"][service]

    def get_admin_credentials(self, credentials):
        """
        Function to get email credentials
        :return: Dictionary with the credentials
        """
        return self.config_file["user"][credentials]


