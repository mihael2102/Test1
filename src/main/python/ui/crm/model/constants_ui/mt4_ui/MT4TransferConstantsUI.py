import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class MT4TransferConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    LIST_SOURCE = "Source"
    LIST_DESTINATION = "Destination"
    FIELD_AMOUNT = "Amount"

    AMOUNT = "1.00"
    EXPECTED_BALANCE_1 = "0.00"
    EXPECTED_BALANCE_2 = "1.00"
