from datetime import *

from dateutil.relativedelta import relativedelta


class CRMConstants(object):
    EXPIRE_DATE = datetime.now() + relativedelta(days=2)
    FORMAT = "%d-%m-%Y"
    CREDIT_IN_COMMENT = "Credit in "
    AMOUNT_CREDIT_IN = "25.00"
    CREDIT_IN = "9"
    CREDIT_OUT = "10"
    DESCRIPTION_WITHDRAW = "Test"
    STATUS_WITHDRAW = "Approved"
    PAYMENT_METHOD_WITHDRAW = "Credit card"
    DESCRIPTION_DEPOSIT = "Test"
    STATUS_DEPOSIT = "Approved"
    PAYMENT_METHOD_DEPOSIT = "Credit card"
    WITHDRAW = "7"
    DEPOSIT = "6"
    AMOUNT_WITHDRAW = "15"
    AMOUNT_DEPOSIT = "10.00"
    AMOUNT_WITHDRAW_SECOND = "30.00"
