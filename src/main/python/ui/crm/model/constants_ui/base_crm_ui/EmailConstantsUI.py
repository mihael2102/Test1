import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class EmailConstantsUI(object):
    FIELD_SUBJECT = ""

    SUBJECT_TASKS = ": SUBJECT_TASK" + str(random.randrange(1, 999))
    MESSAGE = "Test message"
