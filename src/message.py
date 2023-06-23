import re
import os


class Message:

    def __init__(self):
        """
        Constructor, only init the file path
        """
        self.message_path = '{file}.txt'

    def get(self, path, file_name):
        """
        Function to get the message template
        :param path: Path files
        :param file_name: File name
        :return: Message txt
        """
        message_file = str.format(os.path.join(path, self.message_path), file=file_name)
        return open(message_file, encoding="utf-8").read()

    @staticmethod
    def clean_message(message):
        """
        Function to remove curly braces from message template
        :param message: Txt file to remove curly braces
        :return: Txt file without curly braces
        """
        remove_braces = r'[{}]'
        empty = ""
        return re.sub(remove_braces, empty, message)

    @staticmethod
    def get_words(message):
        """
        Function to get the words to replace from the message template
        :param message: Txt file
        :return: List with all the words to replace
        """
        words_between_braces = r'{(.*?)}'
        return re.findall(words_between_braces, message)
