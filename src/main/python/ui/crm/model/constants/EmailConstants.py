import random
from datetime import *


class EmailConstants(object):
    random_number = str(random.randrange(1, 9999999))
    CLIENTS_COMMENT = "Test Comment " + str(date.today())
    TASK_COMMENT = "Comment from task module " + str(date.today())
    FIRST_SUBJECT = "Test subject " + str(date.today())
    FIRST_SUPPORT_EMAIL = "<newforex@pandats.com>"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
    EMAIL_ADDRESS = "jonathan.albalak@pandats.com"
    EMAIL_PASSWORD = "9U&AU=bm"
