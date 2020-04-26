import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class HDCreateTicketConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    FIELD_TITLE = "Title"
    FIELD_DESCRIPTION = "Description information"
    LIST_ASSIGNED = "Assigned to"
    LIST_PRIORITY = "Priority"
    LIST_STATUS = "Status"
    LIST_CATEGORY = "Category"
    LIST_SOURCE = "Ticket source"
    BTN_FINAL = "Create ticket"
    BTN_FNL_EDIT = "Edit ticket"

    TITLE = "Test_ticket_%s" % random_numbers
    ASSIGNED_TO = "Panda Auto"
    PRIORITY = "Normal"
    PRIORITY_EDIT = "Low"
    STATUS = "Open"
    STATUS_EDIT = "Closed"
    CATEGORY = "General Question"
    RELATED_TO = "testqa"
    SOURCE = "Email"
    DESCRIPTION = "Test Description"
