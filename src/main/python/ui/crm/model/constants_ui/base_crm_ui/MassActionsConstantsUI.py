import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
import string


class MassActionsConstantsUI(object):

    MASS_ASSIGN = "Mass Assign"
    MASS_EDIT = "Mass Edit"
    DEPARTMENT_ALL = "All Departments"

    FIELD_LEAD_STATUS = "Lead Status"
    FIELD_LEAD_SOURCE = "Lead Source"
    FIELD_CLIENT_STATUS = "Client Status"
    FIELD_COUNTRY = "Country"
    FIELD_LANGUAGE = "Language"
    FIELD_ASSIGNED_TO = "Assigned To"
    LIST_LEAD_STATUS = "Lead Status"
    LIST_EVENT_TYPE = "Event Type"
    LIST_EVENT_DURATION = "Event Duration"
    LIST_PRIORITY = "Priority"

    SOURCE_OTHER = "Other"
    COUNTRY_ALBANIA = "Albania"
    LANGUAGE_GERMAN = "German"
    USER_NAME = "Panda Auto"
    USER_NAME_1 = "Michael O"
    STATUS_R_NEW = "R - New"
    STATUS_B_TEST = "B - Test"
    EVENT_TYPE = "Meeting"
    EVENT_DURATION = "15M"
    PRIORITY = "Low"
