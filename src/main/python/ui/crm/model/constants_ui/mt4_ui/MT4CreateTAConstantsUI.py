import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4CreateTAConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_SERVER = "Server"
    LIST_CURRENCY = "Currency"
    LIST_GROUP = "Group"
    LIST_LEVERAGE = "Leverage"

    SERVER_DEMO = "Demo"
    SERVER_LIVE = "Live"
    GROUP_DEMO = "demo"
    GROUP_LIVE = "live"
    LEVERAGE = "100"
    if brand == "fair-bit":
        CURRENCY = "TTR"
    else:
        CURRENCY = "USD"
