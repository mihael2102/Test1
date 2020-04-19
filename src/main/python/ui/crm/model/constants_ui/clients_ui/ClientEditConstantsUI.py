import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ClientEditConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    FIELD_FNAME = "First name"
    FIELD_LNAME = "Last name"
    FIELD_CITY = "City"
    LIST_COUNTRY = "Country"
    BTN_SAVE = "Save"

    ROW_1 = "1"
    SHORT_EMAIL = "pandaqa"
    PHONE = "1010101"
    FNAME = "testqa_%s" % random_character
    E_FNAME = "testqa_edit%s" % random_character
    LNAME = "test_edit"
    EMAIL = "pandaqa+" + now + "ed@pandats.com"
    CITY = "Edit city"
    COUNTRY = "Afghanistan"
