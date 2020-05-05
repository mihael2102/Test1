import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4CreditOutConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_TA = "Trading account"
    FIELD_AMOUNT = "Amount in account currency"
    FIELD_GRANTED_BY = "Granted by"
    FIELD_COMMENT = "Comment"
    BTN_FINAL = "Credit out"

    AMOUNT = "1.00"
    AMOUNT_CRYPTO = "0.00001"
    GRANTED_BY = "Test credit out"
    COMMENT = "Test Credit out"
    EXPECTED_CREDIT = "1.00"
    EXPECTED_CREDIT_CR = "0.00001"
