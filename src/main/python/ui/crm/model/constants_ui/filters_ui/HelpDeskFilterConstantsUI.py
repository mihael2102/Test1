import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class HelpDeskFilterConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    HD_FILTER_NAME = "TestFilterHelpDeskModule" + str(date.today())

    COLUMN1 = "Ticket No"
    COLUMN2 = "Priority"
    COLUMN3 = "Status"
    COLUMN4 = "Assigned To"
    COLUMN5 = "CRM Id"
    COLUMN6 = "Category"
    COLUMN7 = "Brand"
    COLUMN8 = "Related to"

    FIELD_VIEW_NAME = "View name"
    LIST_BASED_FILTER = "Based on existing filter"
