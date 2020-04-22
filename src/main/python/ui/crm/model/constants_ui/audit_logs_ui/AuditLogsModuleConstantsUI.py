import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import string


class AuditLogsModuleConstantsUI(object):
    ROW_NUMBER_FOR_DATA_SEARCHING_5 = "5"
    ROW_NUMBER_FOR_DATA_SEARCHING_1 = "1"
    TAB_ALL = "All"
    COLUMN_MODULE = "module"
    COLUMN_ACTION = "action"
    MODULE_USERS = "Users"
    MODULE_TRANSACTIONS = "Financial Transactions"
    MODULE_LEADS = "Leads"
    ACTION_OTP_LOGIN = "OTP: Authenticate, Login Success"
    ACTION_EXPORT = "Export"
    ACTION_SAVE = "Save"
    ACTION_DETAIL_VIEW = "Detail View"
    ACTION_EDIT_VIEW = "Edit View"
    DATA_OTP_LOGIN = "OTP: Authenticate, loginSuccess"
    DATA_TRANSACTIONS = "MTTransactions"
    DATA_DETAIL_VIEW = "DetailView"
    DATA_EDIT_VIEW = "EditView"
