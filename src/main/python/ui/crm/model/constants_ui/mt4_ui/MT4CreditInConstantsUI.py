import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4CreditInConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_TA = "Trading account"
    FIELD_AMOUNT = "Amount in account currency"
    FIELD_GRANTED_BY = "Granted by"
    FIELD_COMMENT = "Comment"

    TA_CREDIT = ""
    AMOUNT = "2.00"
    DAY = "1"
    MONTH = "JAN"
    YEAR = "2025"
    GRANTED_BY = "Test"
    COMMENT = "Test Credit in"
