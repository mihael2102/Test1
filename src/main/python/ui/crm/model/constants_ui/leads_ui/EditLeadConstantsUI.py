import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class EditLeadConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    FNAME = "testqa2%s" % random_character
    LNAME = "test"
    MOBILE = "1111111"
    PHONE = "333333"
    EMAIL = "pandaqa+2" + now + "@pandats.com"
    S_EMAIL = "secondarytestqa+2@pandats.com"
    TITLE = "Title_%s" % random_numbers
    L_SOURCE = "Other"
    L_STATUS = "R - New"
    ASSIGNED_TO = "Panda Auto"
    LANGUAGE = "English"
    SOURCE_NAME = "source name test"
    FAX = "5555"
    REFERRAL = "TEST REFERRAL"
    ADDRESS = "address"
    POSTAL_CODE = "88888"
    CITY = "Berlin"
    COUNTRY = "Germany"
    STATE = "State"
    PO_BOX = "po box test"
    DESCRIPTION = "Test Description"
