from jproperties import Properties
import pandas as pd


class Files:
    def __init__(self):
        self.properties_file = open("config/config.properties", 'rb')
        self.config_file = pd.read_json("config/config.json").to_dict()
        self.path = "resources/templates"

    def get_properties(self, prop):
        properties = Properties()
        properties.load(self.properties_file)
        return properties.get(prop).data

    def get_environment(self):
        env = self.get_properties("environment")
        return self.config_file["environment"][env]

    def get_email_credentials(self):
        credentials = self.get_properties("user")
        return self.config_file["user"][credentials]
