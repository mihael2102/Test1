import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class CAWithdrawConstants(object):
    random_number = str(random.randrange(1, 9999999))

    PAYMENT_METHOD = "Credit Card"
    CC_LAST_DIGITS = "1111"
    EXPIRY_MONTH = "01"
    EXPIRY_YEAR = "2025"
    REASON = "Limited funds"
    STATUS_REQUEST_CA = "Canceled by customer"
    STATUS_REQUEST_CRM = "Cancelled by customer"
