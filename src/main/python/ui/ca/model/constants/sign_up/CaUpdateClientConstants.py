import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class CaUpdateClientConstants(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    DAY = "12"
    MONTH = "FEB"
    MONTH_CA = "February"
    YEAR = "1990"
    BIRTHDAY_CRM = "1990-02-12"
    FNAME = "Testing"
    LNAME = "Qa"
    CITY = "Gotham"
    CODE = "001"
    ADDRESS = "Lenin st."

    FNAME2 = "Testing2"
    LNAME2 = "Qa2"
    CITIZENSHIP = "Austrian"
    CITY2 = "Leningrad"
    CODE2 = "002"
    ADDRESS2 = "Washington st."
