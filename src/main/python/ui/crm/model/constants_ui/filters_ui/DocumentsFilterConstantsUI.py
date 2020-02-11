import random
from datetime import *
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class DocumentsFilterConstantsUI(object):
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    brand = global_var.current_brand_name

    DOCUMENTS_FILTER_NAME = "TestFilterDocumentsModule" + str(date.today())

    COLUMN1 = "Document No"
    COLUMN2 = "Status"
    COLUMN3 = "Comments"
    COLUMN4 = "Assigned To"

    FIELD_VIEW_NAME = "View name"
    LIST_BASED_FILTER = "Based on existing filter"
