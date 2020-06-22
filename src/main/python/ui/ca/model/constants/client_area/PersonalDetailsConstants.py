import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class PersonalDetailsConstants(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    LIST_DAY = "day"
    LIST_MONTH = "month"
    LIST_YEAR = "year"
    LIST_COUNTRY = "country"
    LIST_CITIZENSHIP = "citizenship"
    FIELD_CITY = "City"
    FIELD_ZIP = "Zip Code / Postcode"
    FIELD_ADDRESS = "Address"
    FIELD_FNAME = "First Name"
    FIELD_LNAME = "Last Name"

    DAY_BIRTH = "10"
    MONTH_BIRTH = "January"
    YEAR_BIRTH = "1995"
    BIRTHDAY_CRM = "1995-01-10"
    COUNTRY = "Albania"
    CITIZENSHIP = "Albanian"
    CITY = "Berlin"
    ZIP_CODE = "123"
    ADDRESS = "Street10"
