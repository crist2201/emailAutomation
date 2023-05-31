from src import file_factory
import pandas as pd
import os


class Words(file_factory.Files):

    def __init__(self):
        super().__init__()
        self.words_template = self.get_properties("words_template")
        self.words_path = os.path.join(self.path, "replaceWords/{name_file}.json")

    def get_words_to_replace(self):
        words_file = pd.read_json(str.format(self.words_path, name_file=self.words_template))
        return words_file.to_dict()[self.words_template]




