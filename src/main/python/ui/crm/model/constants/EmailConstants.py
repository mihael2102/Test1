import random


class EmailConstants(object):
    CLIENTS_COMMENT = "Comment from clients module"
    TASK_COMMENT = "Comment from task module"
    random_number = str(random.randrange(1, 9999))
    FIRST_SUBJECT = "Email subject " + random_number
    FIRST_SUPPORT_EMAIL = "<support@royalcfd.com>"
    EMAIL_CONFIRM_MESSAGE = "Mail was sent successfully"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
    FIRST_EMAIL_ADDRESS = "first_email_address"
    FIRST_EMAIL_PASSWORD = "first_email_password"
    SECOND_EMAIL_ADDRESS = "second_email_address"
    SECOND_EMAIL_PASSWORD = "second_email_password"
