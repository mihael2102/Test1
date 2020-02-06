import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class TAFilterConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    TA_FILTER_NAME = "TestFilterTradingAccountModule" + str(date.today())

    COLUMN1 = "Trading Account Login"
    COLUMN2 = "Server"
    COLUMN3 = "Brand"
    COLUMN4 = "Assigned To"
    COLUMN5 = "Currency"
    COLUMN6 = "Balance"
    COLUMN7 = "Credit"
    COLUMN8 = "Equity"

    FIELD_VIEW_NAME = "View name"
    LIST_BASED_FILTER = "Based on existing filter"
