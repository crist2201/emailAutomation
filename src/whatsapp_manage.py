import pywhatkit


class Whatsapp:

    def __init__(self):
        self.instance = pywhatkit

    def send_messages(self, number, message):
        self.instance.sendwhatmsg_instantly(phone_no=str.format(f"+591{number}"),
                                            message=message)

    def send_programmed_messages(self, number, message, hour, minute):
        self.instance.sendwhatmsg(phone_no=str.format(f"+591{number}"),
                                  message=message,
                                  time_hour=hour,
                                  time_min=minute)

    def send_messages_to_group(self, group_id, message, hour, minute):
        self.instance.sendwhatmsg_to_group(group_id=group_id,
                                           message=message,
                                           time_hour=hour,
                                           time_min=minute)
