import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4WithdrawConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_P_METHOD = "Payment method"
    LIST_STATUS = "Status"
    LIST_TA = "Trading accounts"
    LIST_CLEARED_BY = "Cleared by"
    FIELD_AMOUNT = "Amount in account currency"
    FIELD_COMMENT = "Comment"
    BTN_FINAL = "Withdraw"

    P_METHOD = "Credit card"
    STATUS = "Approved"
    TA = ""
    AMOUNT = "1.00"
    AMOUNT_CRYPTO = "0.00001"
    COMMENT = "Test deposit"
    CLEARED_BY = "PRAXIS"

    BALANCE = "1.00"
    BALANCE_CRYPTO = "0.00001"
