import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class LeadsDetailsConstantsUI(object):
    random_numbers = str(random.randrange(1, 999999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

    FIELD_FNAME = "First Name"
    FIELD_LNAME = "Last Name"
    FIELD_MOBILE = "Mobile"
    FIELD_PHONE = "Phone"
    FIELD_EMAIL = "Email"
    FIELD_S_EMAIL = "Secondary Email"
    FIELD_TITLE = "Title"
    FIELD_LANGUAGE = "Language"
    FIELD_SOURCE_NAME = "Source Name"
    FIELD_FAX = "Fax"
    FIELD_REFERRAL = "Referral"
    FIELD_STREET = "Street"
    FIELD_POSTAL_CODE = "Postal Code"
    FIELD_CITY = "City"
    FIELD_STATE = "State"
    FIELD_PO_BOX = "PO Box"
    FIELD_DESCRIPTION = "Description"
    FIELD_LEAD_SOURCE = "Lead Source"
    FIELD_LEAD_STATUS = "Lead Status"
    FIELD_ASSIGNED_TO = "Assigned To"
    FIELD_COUNTRY = "Country"
    TAB_CUSTOM_INFORMATION = "Custom Information"
    TAB_ADDRESS_INFORMATION = "Address Information"
    TAB_DESCRIPTION_INFORMATION = "Description Information"

    MOBILE_EDIT = random_numbers
