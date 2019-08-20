import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class CAConstants(object):
    MARGIN_LVL = "Margin Level"
    TOTAL_P_L = "Total P/L"
    ACCOUNT_VALUE = "Account Value"
    USED_FUNDS = "Used Funds"
    AVALIABLE_FUNDS = "Available funds"
    PASSWORD = "as1as2"
    DAY_BIRTH = "10"
    MONTH_BIRTH = "January"
    YEAR_BIRTH = "1995"
    CURRENCY = "EUR"
    CURRENCY_CRYPTO = "BTC"
    CITY = "Berlin"
    UPDATE_CITY = "Toronto"
    ZIP_CODE = "123"
    UPDATE_ZIP_CODE = "567"
    ADDRESS = "Street10"
    UPDATE_ADDRESS = "Lenin25"
    CITIZENSHIP = "English"
    CITIZENSHIP2 = "Andorran"
    CITIZENSHIP3 = "Austrian"
    UPDATE_CITIZENSHIP = "Australian"
    ACCOUNT_TYPE = "Pro"
    ACCOUNT_LIVE = "Live"
    LEVERAGE_LEVEL = "1:100"
    LEVERAGE_LEVEL2 = "1:200"
    ACCOUNT_DEMO = "Demo"
    INITIAL_DEPOSIT0 = "0"
    INITIAL_DEPOSIT1 = "1000000"
    INITIAL_DEPOSIT = "50000"
    INITIAL_DEPOSIT_BTC = "10"
    INITIAL_DEPOSIT_PTBANC = "250"
    DEMO_ACCOUNT_NUMBER = ""
    LIVE_ACCOUNT_NUMBER = ""
    UPDATE_FIRST_NAME = "pandatest" + (''.join(random.sample(string.ascii_uppercase*6, 6)))
    UPDATE_LAST_NAME = "Test"
    TICKET_SUBJECT = "QAtest"
    CATEGORY = "General Question"
    TICKET_DESCRIPTION = "test"
    TICKET_NUMBER_CA = ""
    DOCUMENT_STATUS_CA = "Verified"
    US_REPORTABLE_YES = "Yes"
    US_REPORTABLE_NO = "No"
    ROW = 14
    FNAME_COL = 1
    LNAME_COL = 2
    EMAIL_COL = 8
    PHONE_COL = 9
    BIRTHDAY_COL = 11
    PASSWORD_COL = 12
    ZIP_COL = 6
    CITY_COL = 5
    ADDRESS_COL = 4
    GENDER_COL = 3
    NUMBER = random.randrange(1, 333)
