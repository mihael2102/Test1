import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class SignUpFirstStepConstants(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    FIELD_FNAME = "First Name"
    FIELD_LNAME = "Last Name"
    FIELD_EMAIL = "Email"
    FIELD_PHONE = "Phone"
    FIELD_PASSWORD = "Password"
    FIELD_C_PASSWORD = "Confirm Password"
    FIELD_PROMOCODE = "Enter Promocode"

    F_NAME = "testqa" + random_character
    L_NAME = "Test"
    EMAIL = "pandaqa+" + str(random.randrange(1, 9999999)) + "_ca@pandats.com"
    PHONE = "7777777"
    PASSWORD = "as1as2"
    PROMO = "11111"
    COUNTRY = "Albania"
