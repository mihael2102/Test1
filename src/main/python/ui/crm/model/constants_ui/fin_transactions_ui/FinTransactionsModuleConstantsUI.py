import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class FinTransactionsModuleConstantsUI(object):
    ROW_NUMBER_FOR_DATA_SEARCHING_5 = "5"
    ROW_NUMBER_FOR_DATA_SEARCHING_1 = "1"
    TAB_ALL = "All"
    COLUMN_TRANSACTION_NO = "Transaction No"
    COLUMN_LOGIN = "Login"
    COLUMN_CLIENT = "Client"
    COLUMN_T_TYPE = "Transaction Type"
    COLUMN_P_TYPE = "Payment Type"
