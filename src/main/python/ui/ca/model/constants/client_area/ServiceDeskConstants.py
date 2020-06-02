import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ServiceDeskConstants(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    BTN_START = "Create New Ticket"
    BTN_FINAL = " Open new ticket "
    TAB_CLOSED = "Closed Tickets"
    FIELD_SUBJECT = "Subject"
    FIELD_DESCRIPTION = "Description:"
    LIST_CATEGORY = "category"

    SUBJECT = "Test_subject_%s" % now
    TITLE = "Test_title_%s" % now
    CATEGORY = "Login Problem"
    DESCRIPTION = "test"
    STATUS = "In Progress"
    STATUS_CL = "Closed"
