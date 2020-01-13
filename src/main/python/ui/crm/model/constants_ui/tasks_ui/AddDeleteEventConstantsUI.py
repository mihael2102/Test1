import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class AddDeleteEventConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    EVENT_STATUS = "Not Started"
    EVENT_TYPE = "Call"
    DURATION = "15M"
    ASSIGN_TO = "Panda Auto"
    ATTACHED_TO = "testqa"
    SUBJECT = "Test_Event_%s" % random_numbers
    PRIORITY = "Low"
    COMMENTS = "Test Comment"
    PICK_LIST_EVENT_STATUS = "Event Status"
    PICK_LIST_EVENT_TYPE = "Event Type"
    PICK_LIST_DURATION = "Duration"
    PICK_LIST_ASSIGN_TO = "Assign To"
    PICK_LIST_PRIORITY = "Priority"
    FIELD_SUBJECT = "subject"
    FIELD_COMMENTS = "comments"
