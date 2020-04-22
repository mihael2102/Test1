import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4UpdateTAConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_TA = "Trading Account"
    LIST_LEVERAGE = "Leverage"
    BOX_READONLY = "Read only"
    BTN_UPDATE = "Update"

    GROUP_LIVE = "live"
    LEVERAGE = "400"
    READ_ONLY = "yes"
