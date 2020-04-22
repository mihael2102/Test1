import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ConvertLeadConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    FIELD_FNAME = "First name"
    FIELD_LNAME = "Last name"
    FIELD_EMAIL = "Email"
    FIELD_PHONE = "Phone"
    FIELD_ADDRESS = "Address"
    FIELD_POSTAL_CODE = "Postal code"
    FIELD_CITY = "City"
    FIELD_PASSWORD = "Password"
    FIELD_REFERRAL = "Enter referral"
    FIELD_SOURCE_NAME = "Source name"
    LIST_CITIZENSHIP = "Citizenship"
    LIST_UI_LANGUAGE = "UI Language"
    LIST_COUNTRY = "Country"
    LIST_CURRENCY = "Currency"
    LIST_BRAND = "Brand"
    BTN_FINAL = "Convert lead"

    FNAME = "testqa%s" % random_character
    LNAME = "test"
    EMAIL = "pandaqa+" + now + "@pandats.com"
    PHONE = "7777777"
    DAY = "1"
    MONTH = "JAN"
    YEAR = "1971"
    BIRTHDAY = "1971-01-01"
    CITIZENSHIP = "German"
    UI_LANGUAGE = "English"
    ADDRESS = "test street"
    POSTAL_CODE = "11111"
    CITY = "Zurich"
    COUNTRY = "Germany"
    PASSWORD = "Abcd1234"
    CURRENCY = "EUR"
    GET_CURRENCY = ""
    REFERRAL = "TEST REFERRAL 2"
    BRAND = ""
    SOURCE_NAME = "source test 2"

    EMAIL_EDITABLE = ""
