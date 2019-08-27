import random
from datetime import *
from src.test.python.ui.automation.BaseTest import *


class EmailConstants(object):
    CLIENTS_COMMENT = "Comment from clients module"
    TASK_COMMENT = "Comment from task module"
    random_number = str(random.randrange(1, 9999999))
    FIRST_SUBJECT = "Test subject " + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f'))
    FIRST_SUPPORT_EMAIL = "<newforex@pandats.com>"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
    EMAIL_ADDRESS = Config.email_address
    EMAIL_PASSWORD = Config.email_password
