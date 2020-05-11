import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MainPageConstants(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    ITEM_TRANS_HISTORY = "Transaction History"
    ITEM_PER_DETAILS = "Personal Details"
    ITEM_VER_CENTER = "Verification Center"
    ITEM_SERV_DESK = "Service Desk"
    ITEM_WITHDRAW = "Withdraw"
    ITEM_DEPOSIT = "Deposit"
    ITEM_MAN_ACCOUNTS = "Manage Accounts"
    ITEM_SIGN_OUT = "Sign Out"
