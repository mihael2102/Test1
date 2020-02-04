import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class TradingDetailsConstantsUI(object):
    brand = global_var.current_brand_name

    TAB_CLOSED_TRANSACTIONS = "Closed Transactions"
    FIELD_BALANCE = "Balance"
    if brand == "newrichmarkets":
        ASSET_1 = "3M"
    else:
        ASSET_1 = "EURUSD"
