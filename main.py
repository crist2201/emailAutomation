from src import email_qa, message_template, properties, file_factory

if __name__ == '__main__':
    f = file_factory.Files()
    m = message_template.Message()
    r = m.open_template_message(f.properties.message)
    print(r)

    #x = properties.Properties()
    #print(x.message)
    #s=message_template.Message().replace_data()
    #print(s)
    #x= email_qa.Email().send_emails()
    #email_qa.Email().send_emails()
    #email_qa.Email().close_instance()

