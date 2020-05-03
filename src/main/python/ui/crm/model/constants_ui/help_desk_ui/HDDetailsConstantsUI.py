import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class HDDetailsConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    TAB_DESCRIPTION = "Description Information"
    TAB_ACTIVITIES = "Activities"

    FIELD_TITLE = "Title"
    FIELD_STATUS = "Status"
    FIELD_ASSIGNED_TO = "Assigned To"
    FIELD_PRIORITY = "Priority"
    FIELD_CATEGORY = "Category"
    FIELD_SOURCE = "Ticket Source"
    FIELD_DESCRIPTION = "Description"
