import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class CAConstants(object):
    brand = global_var.current_brand_name

    MARGIN_LVL = "Margin Level"
    TOTAL_P_L = "Total P/L"
    ACCOUNT_VALUE = "Account Value"
    USED_FUNDS = "Used Funds"
    AVALIABLE_FUNDS = "Available funds"
    EMAIL_CA = "pandaqa+" + str(random.randrange(1, 9999999)) + "_ca@pandats.com"
    PASSWORD = "as1as2"
    DAY_BIRTH = "10"
    MONTH_BIRTH = "January"
    YEAR_BIRTH = "1995"
    BIRTHDAY_CRM = "1995-01-10"
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
    CITIZENSHIP3 = "Austrian"
    UPDATE_CITIZENSHIP = "Australian"
    ACCOUNT_TYPE = "Pro"
    ACCOUNT_LIVE = "Live"
    LEVERAGE_LEVEL = "1:100"
    LEVERAGE_LEVEL2 = "1:200"
    LEVERAGE_LEVEL3 = "1:30"
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
    COUNTRY1 = "Albania"
    COUNTRY_DEFAULT = "Germany"
    CREATE_LIVE_ACC_MSG_POSITIVE = "Account created successfully"
    CREATE_LIVE_ACC_MSG_NEGATIVE = "Dear customer, please note you are allowed to have only 1 live accounts"
