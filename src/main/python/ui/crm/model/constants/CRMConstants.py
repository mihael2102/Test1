import random
from datetime import *
from dateutil.relativedelta import relativedelta
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class CRMConstants(object):
    brand = global_var.current_brand_name
    MT4_ACCOUNT_CREATED_SUCCESFULLY_2 = "MT4 Account created successfully"
    MT4_ACCOUNT_UPDATED_SUCCESFULLY_2 = "MT4 Account updated successfully"
    MT4_ACCOUNT_UPDATED_SUCCESFULLY_3 = "Trading Account updated successfully"
    DEPOSIT_SUCCESSFULLY_2 = "Successful MT4 Deposit"
    TESTQA = "testqa"
    STATUS_EVENT = "Planned"
    TYPE_EVENT = "Meeting"
    DURATION_EVENT = "15M"
    SERVER_NOT_CONFIGURATE = "Server Not Configured?"
    CC_EMAIL = "jonathan.albalak@pandats.com"
    SUBJECT_TASK_MAIL = ": SUBJECT_TASK" + str(random.randrange(1, 999))
    TRADING_LEVERAGE_ITRADER = "30"
    SUBJECT_LEAD_MAIL = ": Test MAIL" + str(random.randrange(1, 9999999))
    BODY_LEAD_MAIL = "Test"
    CHANGE_PHONE_LEAD = "0534431234"
    DATE_BIRTH = "1999-02-19"
    STATUS_EDIT_STOX = "R - New"
    STATUS_EDIT_ITRADER = "Test"
    THIRD_STEP_IMPORT_LEADS = "File successfully uploaded."
    STATUS_EDIT = "B - Test"
    SOURCE_EDIT = "Other"
    COUNTRY_EDIT = "Albania"
    STATUS_ASSIGN = "R - New"
    PANDAQA_ASSIGN = "Panda Auto"
    PANDAQA_ASSIGN_CMB = "pandaqatest pandaqa"
    SHORT_EMAIL = "pandaqa"
    SORTING_EXIST = "no"
    SORTING_LEAD_NO = 1
    SORTING_EMAIL = 1
    SECOND_COUNTRY = "country_two"
    PHONE = "Phone"
    SEND_SMS = "Send SMS to "
    SEND_SMS_MESSAGE = "Message was sent successfully"
    MASS_ASSIGN_MESSAGE = "3 accounts assigned to Panda Auto"
    ONE_ASSIGN_MESSAGE = "1 accounts assigned to Panda Auto"
    CONVERT_SUCCESSFUL_MESSAGE = "Account created successfully"
    FIRST_COLUMN = "first_column"
    SECOND_COLUMN = "second_column"
    THIRD_COLUMN = "third_column"
    FOURTH_COLUMN = "fourth_column"
    FOURTH_COLUMN_OTHER_TYPE = "Email"
    FIFTH_COLUMN = "fifth_column"
    SIXTH_COLUMN = "sixth_column"
    SIXTH_COLUMN_OTHER_TYPE = "Assigned To"
    SEVENTH_COLUMN = "seventh_column"
    EIGHTH_COLUMN = "eighth_column"
    NINTH_COLUMN = "ninth_column"
    NINTH_COLUMN_OTHER_TYPE = "Last Name"
    TENTH_COLUMN = "tenth_column"
    TENTH_COLUMN_OTHER_TYPE = "City"
    ELEVENTH_COLUMN = "eleventh_column"
    FILTER_NAME = "test_filter"
    SECOND_FILTER_NAME = "TestFilter" + str(random.randrange(1, 9999))
    CLIENT_STATUS = "client_status_1"
    BRAND = "brand_one"
    TRANSFER_BETWEEN_TA_MESSAGE = "Funds were transferred successfully"
    AMOUNT_TRANSFER_BETWEEN_TA = "1.00"
    TRANSFER_BETWEEN_TA = "8"
    TRANSFER_BETWEEN_TA2 = "5"
    DESCRIPTION_ADD_INTERACTION = "Description Interaction"
    DATE = datetime.now()
    TODAY_DATE = datetime.today().now()
    TIME_ZERO = "07:00:00"
    SECOND_DATE = datetime.now() + relativedelta(days=1, minutes=15)
    THIRD_DATE = datetime.now() + relativedelta(days=2, minutes=30)
    FOURTH_DATE = datetime.now() + relativedelta(days=3, minutes=45)
    MT4_ACCOUNT_CREATED_SUCCESFULLY = "Account created successfully"
    TRADING_ACCOUNT_CREATED_SUCCESFULLY = "Trading Account created successfully"
    MT4_ACCOUNT_UPDATED_SUCCESFULLY = "Account updated successfully"
    TRADING_SERVER_LIVE = "server_live"
    WITHDRAW_SUCCESSFULLY = "MT4 Withdraw successfull"
    DEPOSIT_SUCCESSFULLY = "Successful Deposit"
    TITLE_OF_CLIENT_DEPOSIT_POPUP = "Client Deposit"
    PASSWORD_CHANGE = "Password was change successfully"
    CRM_CLIENT_AREA_PASSWORD_CHANGE = "Client Area Password changed successfully"
    MASS_EDIT = "Successfuly updated"
    CHANGE_PASSWORD = "4"
    MT4_PASSWORD_VALID_MESSAGE = "Entered password valid"
    CUSTOMER_PASSWORD_VALID_MESSAGE = "The password that was entered is correct."
    CHECK_PASSWORD = "3"
    EXPIRE_DATE = datetime.now() + relativedelta(days=2)
    FORMAT_DATE_YEARS = "%d-%m-%Y"
    FORMAT_DATE = "%Y-%m-%d"
    SECOND_FORMAT_DATE = "%Y-%m-%d"
    THIRD_FORMAT_DATE = "%A"
    FIRST_FORMAT_TIME = "%H:%M:%S"
    SECOND_FORMAT_TIME = "%H"
    THIRD_FORMAT = f'{TODAY_DATE:%B} {TODAY_DATE.day}, {TODAY_DATE.year}'
    CREDIT_IN_COMMENT = "Credit in "
    CREDIT_OUT_COMMENT = "Credit out "
    AMOUNT_CREDIT_IN = "2.00"
    AMOUNT_CREDIT_IN_BTC = "0.00002"
    AMOUNT_CREDIT_OUT = "1.00"
    AMOUNT_CREDIT_OUT_BTC = "0.00001"
    CREDIT_IN = "9"
    CREDIT_IN2 = "6"
    CREDIT_OUT = "10"
    CREDIT_OUT2 = "7"
    CREDIT_ACCOUNT = ""
    CREDIT_OUT_GRANTEDBY = "TEST"
    DESCRIPTION_WITHDRAW = "Test"
    CLEAREDBY_WITHDRAW = "PRAXIS"
    CLEAREDBY_WITHDRAW1 = "Wire Transfer"
    STATUS_WITHDRAW = "Approved"
    PAYMENT_METHOD_WITHDRAW = "Credit card"
    DESCRIPTION_DEPOSIT = "Description Deposit"
    DESCRIPTION_TRANSFER_BETWEEN_TA = "test"
    STATUS_DEPOSIT = "Approved"
    PAYMENT_METHOD_DEPOSIT = "Credit card"
    WITHDRAW = "7"
    WITHDRAW2 = "4"
    DEPOSIT = "6"
    DEPOSIT2 = "3"
    CREATE_MT4_USER = "1"
    CREATE_MT4_WITHDRAW = "7"
    UPDATE_MT4_USER = "2"
    AMOUNT_DEPOSIT = "10.00"
    AMOUNT_WITHDRAW = "1"
    AMOUNT_WITHDRAW_BTC = "0.00001"
    AMOUNT_DEPOSIT_FOR_CREDIT_OUT = "2.00"
    AMOUNT_DEPOSIT_BTC = "0.00002"
    AMOUNT_WITHDRAW_SECOND = "30.00"
    ADD_INTERACTION = "6"
    ADD_INTERACTION_TEXT = "Add Interaction"
    CHECK_CLIENT_PASSWORD = "Check Client Password"
    CHANGE_CLIENT_PASSWORD = "Change Client Password"
    INTERACTION_SUCCESSFULLY = "Interaction successfully created"
    SHORT_E_MAIL = "short_email"
    SHORT_SECOND_E_MAIL = "short_second_email"
    SHORT_CLIENT_NAME = "short_client_name"
    SHORT_FIRST_NAME = "short_first_name"
    SHORT_LAST_NAME = "short_last_name"
    FIRST_PHONE_TYPE = "first_phone_type"
    DESCRIPTION_SEND_SMS = "Hello"
    COUNTER_SMS = "1"
    SUBJECT_MASS_SMS = "mass sms test"
    MESSAGE_MASS_SMS = "Sms test " + str(random.randrange(1, 9999999))
    DOCUMENT_TYPE = "Bank statement"
    DOCUMENT_STATUS = "Pending"
    DOCUMENT_SUB_TYPE = "Crypto Transfer"
    DOCUMENT_COMMENTS = "Comments"
    DOCUMENT_SUCCESSFUL_MESSAGE = "Upload Document successfull"
    EASY_SEARCH_CLIENT = "testqa"
    EASY_SEARCH_CLIENT_TEST = "test test"
    ALLOWED_IP = "1.1.1.1"
    ALLOWED_METHOD = "Create lead"
    BLOCKED_COUNTRY = "Albania"
    CREATE_AFFILIATE_SUCCCESS = "Success"
    EASY_SEARCH_CLIENT_TEST = "test"
    CAMPAIGN_NAME = "TestCampaign" + str(random.randrange(1, 9999))
    FIST_ASSIGNED_TO = "Panda Auto"
    START_DATE = "2019-01-09"
    START_DATE2 = "2020-02-03"
    END_DATE = "2021-12-30"
    END_DATE2 = "2022-11-11"
    FIST_DEAL = "CPA"
    SECOND_DEAL = "CPL"
    RATE = "111"
    RATE1 = "222"
    DELETE_INTERACTION_MESSAGE = "Are You Sure You want to Delete?"
    INTERACTION_DELETED_MESSAGE = "Successfully deleted"
    MYDASHBOARD_MODULE = "My Dashboard"
    AUDITLOGS_MODULE = "Audit Logs"
    CRM_CONFIGURATION = "CRM Configuration"
    FIRST_TA_NUMBER_FROM_TA_SECTION = "2"
    SECOND_TA_NUMBER_FROM_TA_SECTION = "3"
