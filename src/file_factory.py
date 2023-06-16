import pandas as pd
from src import properties


class Files:
    def __init__(self):
        """
        Constructor
        :param properties: Get all the properties
        :param config_file: All the configurations
        """
        self.properties = properties.Properties()
        self.config_file = pd.read_json("config/config.json").to_dict()

    def get_service(self):
        """
        Function to get service properties
        :return: Dictionary with the properties
        """
        service = self.properties.service
        return self.config_file["service"][service]

    def get_email_credentials(self):
        """
        Function to get email credentials
        :return: Dictionary with the credentials
        """
        credentials = self.properties.admin
        return self.config_file["user"][credentials]


