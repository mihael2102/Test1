import random
from datetime import *
from dateutil.relativedelta import relativedelta


class WorkflowsConstants(object):
    random_number = str(random.randrange(1, 9999))
    CONDITION_OR = "OR"
    COUNTRY_AUSTRIA = "Austria"
    COUNTRY_GUAM = "Guam"
    STATUS_B_TEST = "B - Test"
    NAME_WORKFLOW = "Test_workflow " + random_number
    PRIORITY_WORKFLOW = ""
    CLIENTS_MODULE = "Clients"
    CLIENT_STATUS = "Client Status"
    CONDITION_IS = "is"
    STATUS_TEST = "Test"
    STATUS_TEST_STARS = "Test***"
    STATUS_R_NO_ANSWER = "R - No Answer"
    EMAIl = "Email"
    CONDITION_CONTAINS = "contains"
    PANDATS_EMAIL = "pandaqa+"
    CONDITION_AND = "AND"
    UPDATE_FIELD = "Update Field"
    TASK_TITLE = "Test_title"
    ADDRESS = "Address"
    TEST_ADDRESS = "Test_address"
    COUNTRY = "Country"
    COUNTRY_ALBANIA = "Albania"
    WORKFLOW_EXIST = ""
    DAY = "1"
    MONTH = "JAN"
    YEAR = "1971"
    CITIZENSHIP = "Albanian"
    CITY = "City"
    P_CODE = "123123"
