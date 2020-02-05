import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class TradingDetailsConstantsUI(object):
    brand = ""

    TAB_CLOSED_TRANSACTIONS = "Closed Transactions"
    FIELD_BALANCE = "Balance"
    if brand == "fairbit":
        ASSET_1 = "ETCEUR"
    else:
        ASSET_1 = "EURUSD"
