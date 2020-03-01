import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class ClientsFilterConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    CLIENTS_FILTER_NAME = "TestFilterClientsModule" + str(date.today())

    COLUMN1 = "CRM Id"
    COLUMN2 = "Client Status"
    COLUMN3 = "Lead Exist"
    COLUMN4 = "Email"
    COLUMN5 = "Client Name"
    COLUMN6 = "Assigned To"
    COLUMN7 = "Country"
    COLUMN8 = "First Name"
    COLUMN9 = "Last Name"
    COLUMN10 = "City"
    COLUMN11 = "Brand"

    FIELD_VIEW_NAME = "View name"
    LIST_BASED_FILTER = "Based on existing filter"
