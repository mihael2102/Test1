import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class AccountConstants(object):
    brand = global_var.current_brand_name

    if brand == "q8":
        CLIENT = "my account"
    elif brand == "24option":
        CLIENT = "Welcome"
    else:
        CLIENT = "Test"
