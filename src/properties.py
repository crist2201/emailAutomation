class Properties:
    def __init__(self):
        self.properties = self.set_properties()
        self.service = self.properties[0].lower()
        self.admin = self.properties[1].lower()
        self.template = self.properties[2]
        self.version = self.properties[3]
        self.message = self.properties[4]
        self.users_data = self.properties[5]
        self.sheet = self.properties[6].upper()
        self.path = self.set_path(self.version, self.template)

    @staticmethod
    def set_properties():
        properties = input("Set properties (service, user, template, version, message, data, course):")
        return properties.title().replace(" ", "").split(",")

    @staticmethod
    def set_path(version, template):
        path = 'resources/templates/Version {version}/{template}/'
        return str.format(path, version=version, template=template)

    @staticmethod
    def set_service():
        """
        Function to set the service to use: Gmail or other
        :return: Service selected
        """
        return input("Service to use (Gmail): ").lower()

    @staticmethod
    def set_admin_user():
        """
        Function to set the service to use: Gmail or other
        :return: Service selected
        """
        return input("Admin user to use (qa_testing or qa_academy): ").lower()

    @staticmethod
    def set_message_template():
        """
        Function to set the message template to use
        :return: Message file name
        """
        return input("Set message template: ")

    @staticmethod
    def set_users_data():
        """
        Function to set users data to use
        :return: Users data file name
        """
        return input("Set users data: ")
