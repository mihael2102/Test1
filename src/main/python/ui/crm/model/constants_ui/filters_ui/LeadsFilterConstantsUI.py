import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class LeadsFilterConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LEADS_FILTER_NAME = "TestFilterLeadsModule" + str(date.today())

    COLUMN1 = "First Name"
    COLUMN2 = "Last Name"
    COLUMN3 = "Email"
    COLUMN4 = "Assigned To"
    COLUMN5 = "Lead No"
    COLUMN6 = "Lead Source"
    COLUMN7 = "Lead Status"
    COLUMN8 = "Language"

    FIELD_VIEW_NAME = "View name"
    LIST_BASED_FILTER = "Based on existing filter"
