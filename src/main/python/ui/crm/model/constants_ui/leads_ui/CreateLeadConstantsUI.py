import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class CreateLeadConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')

    FIELD_FNAME = "First Name"
    FIELD_LNAME = "Last Name"
    FIELD_MOBILE = "Mobile"
    FIELD_PHONE = "Phone"
    FIELD_EMAIL = "Email"
    FIELD_S_EMAIL = "Secondary email"
    FIELD_TITLE = "Title"
    FIELD_LANGUAGE = "Language"
    FIELD_SOURCE_NAME = "Source Name"
    FIELD_FAX = "Fax"
    FIELD_REFERRAL = "Referral"
    FIELD_ADDRESS = "Address"
    FIELD_POSTAL_CODE = "Postal Code"
    FIELD_CITY = "City"
    FIELD_STATE = "State"
    FIELD_PO_BOX = "PO Box"
    FIELD_DESCRIPTION = "Description"
    LIST_LEAD_SOURCE = "Lead source"
    LIST_LEAD_STATUS = "Lead status"
    LIST_ASSIGNED_TO = "Assigned to"
    LIST_COUNTRY = "Country"
    BTN_FINAL = "Create lead"

    FNAME = "testqa%s" % random_character
    FNAME2 = "testqa2%s" % random_character
    LNAME = "test"
    MOBILE = "8888888"
    MOBILE2 = "1111111"
    PHONE = "222222"
    PHONE2 = "333333"
    EMAIL = "pandaqa+" + now + "@pandats.com"
    EMAIL2 = "pandaqa+2" + now + "@pandats.com"
    S_EMAIL = "secondarytestqa+1@pandats.com"
    S_EMAIL2 = "secondarytestqa+2@pandats.com"
    TITLE = "Title_%s" % random_numbers
    L_SOURCE = "Other"
    L_STATUS = "R - New"
    STATUS = ""
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
