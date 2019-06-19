import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class EmailConstants(object):
    brand = global_var.current_brand_name
    random_number = str(random.randrange(1, 9999999))
    CLIENTS_COMMENT = "Test Comment " + str(date.today())
    TASK_COMMENT = "Comment from task module " + str(date.today())
    FIRST_SUBJECT = brand + ": Test subject " + str(date.today())
    FIRST_SUPPORT_EMAIL = "<newforex@pandats.com>"
    SECOND_EMAIL_CONFIRM_MESSAGE = "Email sent"
    EMAIL_ADDRESS = "jonathan.albalak@pandats.com"
    EMAIL_PASSWORD = "xUQ7hrr9VF"
