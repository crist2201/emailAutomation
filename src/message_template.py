from src import file_factory
import os
import re


class Message(file_factory.Files):

    def __init__(self):
        super().__init__()
        self.message_template = self.get_properties("message_template")
        self.message_path = os.path.join(self.path, "messages/{name_file}.txt")

    def get_template_message(self):
        message_file = str.format(self.message_path, name_file=self.message_template)
        return open(message_file, encoding="utf-8").read()

    def get_clean_message(self):
        remove_braces = r'[{}]'
        empty = ""
        return re.sub(remove_braces, empty, self.get_template_message())


