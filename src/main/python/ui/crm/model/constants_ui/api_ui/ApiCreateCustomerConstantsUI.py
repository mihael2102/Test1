import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ApiCreateCustomerConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    EMAIL = "pandaqa+" + now + "c@pandats.com"
    PASSWORD = "as1as2"
    COUNTRY = "de"
    COUNTRY_CRM = "Germany"
    FNAME = "testqa" + random_character
    LNAME = "testAPI"
    PHONE = "3453453"
    REFFERAL = "langref=hebrew"
    STATUS_OK = "ok"
