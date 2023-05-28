import template_factory
import os
import re


class Message(template_factory.Template):

    def __init__(self):
        super().__init__()
        self.path = os.path.join(self.set_path(), "messages/{name_file}.txt")
        self.remove_braces = r'[{}]'
        self.find_braces = r'{.*}'
        self.empty = ""

    def get_template_message(self):
        return open(self.get_file(), encoding="utf-8").read()

    def get_clean_message(self):
        return re.sub(self.remove_braces, self.empty, self.get_template_message())


