import random


class EmailConstants(object):
    random_number = str(random.randrange(1, 9999999))
    CLIENTS_COMMENT = "Test Comment"
    TASK_COMMENT = "Comment from task module " + random_number
    FIRST_SUBJECT = "Test subject " + random_number
    FIRST_SUPPORT_EMAIL = "<newforex@pandats.com>"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
