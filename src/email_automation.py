from src import message, properties, file_factory, user_data, email_manage


class EmailAutomation:

    def __init__(self):
        self.properties = properties.Properties()
        self.file = file_factory.Files()
        self.message = message.Message()
        self.users_data = user_data.Data()
        self.message_template = self.message.get_template_message(self.properties.message)
        self.data_to_replace = self.users_data.get_users_data(self.properties.users_data)
        self.words_to_replace = self.message.get_words_to_replace(self.message_template)
        self.email_service = self.file.get_service(self.properties.service)
        self.admin_email = self.file.get_email_credentials(self.properties.admin)
        self.instance = email_manage.Email(self.email_service['server'], self.email_service['port'])

    def send_emails(self):
        self.instance.login_email(self.admin_email['email'], self.admin_email['password'])
        for index, row in self.data_to_replace.iterrows():
            for word in self.words_to_replace:
                self.message_template = self.message_template.replace(word, row[word])
            self.message_template = self.message.clean_message(self.message_template)
            email_send = self.instance.send_email(self.admin_email['email'], row['EMAIL'], self.message_template)
            if email_send:
                print(str.format("Email not sent to {email_address} ", email_address=row['EMAIL']))
            else:
                print(str.format("Email sent to {email_address}", email_address=row['EMAIL']))
                self.message_template = self.message.get_template_message(self.properties.message)
        self.instance.close_instance()
