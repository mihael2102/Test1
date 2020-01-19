import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class HDCreateTicketConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    TITLE = "Test_ticket_%s" % random_numbers
    ASSIGNED_TO = "Panda Auto"
    PRIORITY = "Low"
    STATUS = "Open"
    CATEGORY = "General Question"
    RELATED_TO = "testqa"
    SOURCE = "Email"
    DESCRIPTION = "Test Description"
