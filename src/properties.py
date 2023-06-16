class Properties:
    def __init__(self):
        self.service = self.set_service()
        self.admin = self.set_admin_user()
        self.message = self.set_message_template()
        self.users_data = self.set_users_data()

    @staticmethod
    def set_service():
        """
        Function to set the service to use: Gmail or other
        :return: Service selected
        """
        return input("Service to use (Email): ").lower()

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
