import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ClientDetailsConstants(object):
    TRADING_ACCOUNTS_TAB = "Trading Accounts"
    FINANCIAL_TRANSACTIONS_TAB = "Financial Transactions"
    TAG_BALANCE = "Balance"
    TAG_WITHDRAWALS = "Withdrawals"
    TAG_DEPOSIT = "Deposit"
    TAG_EQUITY = "Equity"
    TAG_FREE_MARGIN = "Free Margin"
    TAG_NET_DEPOSIT = "Net Deposit"
    TAG_CREDIT = "Credit"
