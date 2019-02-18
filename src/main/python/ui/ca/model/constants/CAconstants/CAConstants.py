import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class CAConstants(object):
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
    CITIZENSHIP = "Albanian"
    CITIZENSHIP2 = "Andorran"
    UPDATE_CITIZENSHIP = "Australian"
    ACCOUNT_TYPE = "Pro"
    ACCOUNT_LIVE = "Live"
    LEVERAGE_LEVEL = "1:100"
    LEVERAGE_LEVEL2 = "1:200"
    ACCOUNT_DEMO = "Demo"
    INITIAL_DEPOSIT0 = "0"
    INITIAL_DEPOSIT1 = "1000000"
    INITIAL_DEPOSIT = "10000"
    INITIAL_DEPOSIT_BTC = "10"
    DEMO_ACCOUNT_NUMBER = ""
    LIVE_ACCOUNT_NUMBER = ""
    UPDATE_FIRST_NAME = "pandatest" + (''.join(random.sample(string.ascii_uppercase*6, 6)))
    UPDATE_LAST_NAME = "Test"