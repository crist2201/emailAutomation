from src import message, properties, file_factory, user_data, email_manage, whatsapp_manage


class MessageAutomation:

    def __init__(self):
        """
        Constructor to init all the properties
        """
        self.properties = properties.Properties()
        self.file = file_factory.Files()
        self.message = message.Message()
        self.users_data = user_data.Data()
        self.message_template = self.message.get(self.properties.path, self.properties.message)
        self.data_to_replace = self.users_data.get(self.properties.path, self.properties.users_data,
                                                   self.properties.sheet)
        self.words_to_replace = self.message.get_words(self.message_template)
        self.service = self.file.get_service(self.properties.service)

        self.admin = self.file.get_admin_credentials(self.properties.admin)
        self.instance = self.select_instance()

    def select_instance(self):
        if self.properties.service != "whatsapp":
            return email_manage.Email(self.service['server'], self.service['port'])
        else:
            return whatsapp_manage.Whatsapp()

    def send_emails(self):
        """
        Function to send email
        :return: None
        """
        self.instance.login_email(self.admin['email'], self.admin['password'])
        for index, row in self.data_to_replace.iterrows():
            for word in self.words_to_replace:
                self.message_template = self.message_template.replace(word, row[word])
            self.message_template = self.message.clean_message(self.message_template)
            email_send = self.instance.send_email(self.admin['email'], row['EMAIL'], self.message_template)
            if email_send:
                print(str.format("Email not sent to {email_address} ", email_address=row['EMAIL']))
            else:
                print(str.format("Email sent to {email_address}", email_address=row['EMAIL']))
                self.message_template = self.message.get(self.properties.path, self.properties.message)
        self.instance.close_instance()

    def send_whatsapp(self):
        for index, row in self.data_to_replace.iterrows():
            for word in self.words_to_replace:
                self.message_template = self.message_template.replace(word, row[word])
            self.message_template = self.message.clean_message(self.message_template)
            self.instance.send_messages(row['CELULAR'], self.message_template)
            self.message_template = self.message.get(self.properties.path, self.properties.message)

