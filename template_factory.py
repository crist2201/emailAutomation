import pandas as pd


class Template:

    def __init__(self):
        self.template_file = pd.read_json("config/templates.json")
        self.template = self.set_template()
        self.data = self.set_data()

    def set_template(self):
        return self.template_file["config"]["template"]

    def set_path(self):
        return self.template_file["config"]["path"]

    def set_data(self):
        return self.template_file["config"]["data"]

    def get_file(self):
        return str.format(self.path, name_file=self.template)





