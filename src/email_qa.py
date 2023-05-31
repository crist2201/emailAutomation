import smtplib
import ssl

import file_factory
import words_template
import message_template
import data_template


class Email():

    def __init__(self):
        super().__init__()
        self.environment = file_factory.Files().get_environment()
        self.email_credentials = file_factory.Files().get_email_credentials()
        self.message = message_template.Message().get_clean_message()
        self.data = data_template.Data().get_users_data()
        self.words = words_template.Words().get_words_to_replace()

    def instance_server(self):
        return smtplib.SMTP_SSL(self.environment["server"], self.environment["port"],
                                context=ssl.create_default_context())

    def close_instance(self):
        return self.instance_server().quit()

    def login_email(self):
        server = self.instance_server()
        try:
            server.login(self.email_credentials["email"], self.email_credentials["password"])
            return server
        except smtplib.SMTPException as exception:
            return exception

    def send_emails(self):
        server = self.login_email()
        for index, row in self.data.iterrows():
            for key, value in self.words.items():
                self.message = self.message.replace(key, row[key])
            email_send = server.sendmail(self.email_credentials["email"], row['EMAIL'], self.message.encode("utf-8"))
            if email_send:
                print(str.format("Email not sent to {email_address} ", email_address=row['EMAIL']))
            else:
                print(str.format("Email sent to {email_address}", email_address=row['EMAIL']))
                self.message = message_template.Message().get_clean_message()



