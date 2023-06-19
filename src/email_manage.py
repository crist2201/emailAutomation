import smtplib
import ssl


class Email:

    def __init__(self, server, port):
        """
        Constructor to init the email service server
        :param server: SMTP server
        :param port: Port to connect
        """
        self.instance = smtplib.SMTP_SSL(server, port, context=ssl.create_default_context())

    def close_instance(self):
        """
        Function to close/finish the instance created
        :return: None
        """
        self.instance.close()

    def login_email(self, email, password):
        """
        Function to log in with email credentials
        :param email: Email address
        :param password: Password
        :return: Instance created or exception
        """
        try:
            self.instance.login(email, password)
            return self.instance
        except smtplib.SMTPException as exception:
            return exception

    def send_email(self, sender, receiver, msg):
        """
        Function to send an email
        :param sender: Sender email address
        :param receiver: Receiver email address
        :param msg: Message to send, it has to be a string
        :return: Empty dictionary if the email was sent
        """
        return self.instance.sendmail(sender, receiver, msg.encode("utf-8"))
