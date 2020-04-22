import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class AddDeleteEventConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    LIST_EVENT_STATUS = "Event Status"
    LIST_EVENT_TYPE = "Event Type"
    LIST_DURATION = "Duration"
    LIST_ASSIGN_TO = "Assign To"
    LIST_PRIORITY = "Priority"
    FIELD_SUBJECT = "Subject"
    FIELD_COMMENTS = "Comments"
    BTN_ADD_INT = "Add Interaction"
    BTN_SAVE_NEW = "Save & New"
    BTN_SAVE = "Save"

    EVENT_STATUS = "Not Started"
    EVENT_TYPE = "Call"
    DURATION = "15M"
    ASSIGN_TO = "Panda Auto"
    ATTACHED_TO = "testqa"
    SUBJECT = "Test_Event_%s" % random_numbers
    INT_SUBJ_1 = "test1"
    INT_SUBJ_2 = "test2"
    PRIORITY = "Low"
    COMMENTS = "Test Comment"
    SHORT_EMAIL = "pandaqa"
