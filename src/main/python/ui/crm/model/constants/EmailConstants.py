import random


class EmailConstants(object):
    CLIENTS_COMMENT = "Comment from clients module"
    TASK_COMMENT = "Comment from task module"
    random_number = str(random.randrange(1, 9999))
    FIRST_SUBJECT = "Email subject " + random_number
    FIRST_SUPPORT_EMAIL = "<newforex@pandats.com>"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
