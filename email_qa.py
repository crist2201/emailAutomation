import pandas as pd
import smtplib
import ssl
import words_factory
import message_factory
import data


class Email(message_factory.Message):

    def __init__(self):
        super().__init__()
        self.email_file = pd.read_json("config/email.json").to_dict()
        self.server = self.login_email()
        self.message = self.get_clean_message()
        self.words = words_factory.Words().get_words_to_replace()
        self.data = data.Data().get_users_data()

    def get_email_address(self):
        return self.email_file["qa_academy"]["email"]

    def get_email_password(self):
        return self.email_file["qa_academy"]["password"]

    def get_server_address(self):
        return self.email_file["qa_academy"]["server"]

    def get_server_port(self):
        return self.email_file["qa_academy"]["port"]

    def instance_server(self):
        return smtplib.SMTP_SSL(self.get_server_address(), self.get_server_port(), context=ssl.create_default_context())

    def close_instance(self):
        return self.instance_server().quit()

    def login_email(self):
        server = self.instance_server()
        try:
            server.login(self.get_email_address(), self.get_email_password())
            return server
        except smtplib.SMTPException as exception:
            return exception

    def send_emails(self):
        for index, row in self.data.iterrows():
            for key, value in self.words.items():
                self.message = self.message.replace(key, row[key])
            email_send = self.server.sendmail(self.get_email_address(), row['EMAIL'], self.message.encode("utf-8"))
            if email_send:
                print(str.format("Email not sent to {email_address} ", email_address=row['EMAIL']))
            else:
                print(str.format("Email sent to {email_address}", email_address=row['EMAIL']))
                self.message = self.get_clean_message()



