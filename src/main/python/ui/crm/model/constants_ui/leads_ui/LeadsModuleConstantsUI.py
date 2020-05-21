import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class LeadsModuleConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

    COLUMN_FNAME = "First Name"
    COLUMN_LNAME = "Last Name"
    COLUMN_MOBILE = "Mobile"
    COLUMN_PHONE = "Phone"
    COLUMN_EMAIL = "Email"
    COLUMN_S_EMAIL = "Secondary email"
    COLUMN_TITLE = "Title"
    COLUMN_LANGUAGE = "Language"
    COLUMN_SOURCE_NAME = "Source Name"
    COLUMN_FAX = "Fax"
    COLUMN_REFERRAL = "Referral"
    COLUMN_ADDRESS = "Address"
    COLUMN_POSTAL_CODE = "Postal Code"
    COLUMN_CITY = "City"
    COLUMN_STATE = "State"
    COLUMN_PO_BOX = "PO Box"
    COLUMN_DESCRIPTION = "Description"
    COLUMN_LEAD_SOURCE = "Lead source"
    COLUMN_LEAD_STATUS = "Lead Status"
    COLUMN_ASSIGNED_TO = "Assigned To"
    COLUMN_COUNTRY = "Country"
    COLUMN_LEAD_NO = "Lead No"
    COLUMN_CREATED_TIME = "Created Time"
    ROW_NUMBER_FOR_DATA_SEARCHING_5 = "5"
    ROW_NUMBER_FOR_DATA_SEARCHING_1 = "1"
    TAB_ALL = "All"

    SHORT_EMAIL = "pandaqa"
