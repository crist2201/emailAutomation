import template_factory
import pandas as pd
import os


class Words(template_factory.Template):

    def __init__(self):
        super().__init__()
        self.path = os.path.join(self.set_path(), "replaceWords/{name_file}.json")

    def get_words_to_replace(self):
        return pd.read_json(self.get_file())[self.template].to_dict()




