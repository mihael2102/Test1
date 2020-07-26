import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ClientDetailsConstantsUI(object):
    brand = global_var.current_brand_name

    ROW_1 = "1"
    ROW_2 = "2"
    ROW_3 = "3"

    TAB_TRADING_ACCOUNTS = "Trading Accounts"
    TAB_FINANCIAL_TRANSACTIONS = "Financial Transactions"
    TAB_CUSTOM_INFORMATION = "Custom Information"
    TAB_MARKETING_INFORMATION = "Marketing Information"
    TAB_ADDRESS_INFORMATION = "Address Information"
    TAB_ACTIVITIES = "Activities"
    TAB_HELP_DESK = "Help Desk"

    TAG_BALANCE = "Balance"
    TAG_WITHDRAWALS = "Withdrawals"
    TAG_DEPOSIT = "Deposit"
    TAG_EQUITY = "Equity"
    TAG_FREE_MARGIN = "Free Margin"
    TAG_NET_DEPOSIT = "Net Deposit"
    TAG_CREDIT = "Credit"

    FIELD_FNAME = "First Name"
    FIELD_LNAME = "Last Name"
    FIELD_EMAIL = "Email"
    FIELD_PHONE = "Phone"
    FIELD_CITIZENSHIP = "Citizenship"
    FIELD_UI_LANGUAGE = "UI Language"
    FIELD_ADDRESS = "Address"
    FIELD_CODE = "Code"
    FIELD_CITY = "City"
    FIELD_COUNTRY = "Country"
    FIELD_BASE_CURRENCY = "Base Currency"
    FIELD_REFERRAL = "Referral"
    FIELD_CLIENT_SOURCE = "Client Source"
    FIELD_BIRTHDAY = "Date Of Birth"
    FIELD_CLIENT_STATUS = "Client Status"

    COLUMN_LOGIN = "Login"
    COLUMN_BALANCE = "Balance"
    COLUMN_CREDIT = "Credit"
    COLUMN_LEVERAGE = "Leverage"
    COLUMN_READ_ONLY = "Read Only"
