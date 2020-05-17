import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class EditLeadConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S')

    FNAME = "Name"
    LNAME = "Surname"
    MOBILE = "7777777"
    PHONE = "121212"
    EMAIL = "pandaqa+3" + now + "@pandats.com"
    S_EMAIL = "secondarytestqa+edit@pandats.com"
    TITLE = "Edit_Title_%s" % random_numbers
    L_SOURCE = "Web Site"
    L_STATUS = "B - Test"
    STATUS = ""
    ASSIGNED_TO = "Anastasiia V"
    LANGUAGE = "Ukrainian"
    SOURCE_NAME = "edit source name test"
    FAX = "0909"
    REFERRAL = "Edit TEST REFERRAL"
    ADDRESS = "Edit address"
    POSTAL_CODE = "3535"
    CITY = "New York"
    COUNTRY = "United States"
    STATE = "Edit State"
    PO_BOX = "edit po box test"
    DESCRIPTION = "Edit Test Description"
    BTN_FINAL = "Update lead"
