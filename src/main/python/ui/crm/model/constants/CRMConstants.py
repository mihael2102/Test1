import random
from datetime import *
from dateutil.relativedelta import relativedelta


class CRMConstants(object):
    SECOND_COUNTRY = "country_two"
    PHONE = "Phone"
    SEND_SMS_MESSAGE = "Message was sent successfully"
    MASS_ASSIGN_MESSAGE = "3 accounts assigned to Panda Support"
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
    AMOUNT_TRANSFER_BETWEEN_TA = "15.00"
    TRANSFER_BETWEEN_TA = "8"
    DESCRIPTION_ADD_INTERACTION = "Description Interaction"
    DATE = datetime.now()
    TODAY_DATE = datetime.today().now()
    TIME_ZERO = "07:00:00"
    SECOND_DATE = datetime.now() + relativedelta(days=1, minutes=15)
    THIRD_DATE = datetime.now() + relativedelta(days=2, minutes=30)
    FOURTH_DATE = datetime.now() + relativedelta(days=3, minutes=45)
    MT4_ACCOUNT_CREATED_SUCCESFULLY = "MT4 Account created successfully"
    MT4_ACCOUNT_UPDATED_SUCCESFULLY = "MT4 Account updated successfully"
    TRADING_SERVER_LIVE = "server_live"
    WITHDRAW_SUCCESSFULLY = "MT4 Withdraw successfull"
    DEPOSIT_SUCCESSFULLY = "Successful MT4 Deposit"
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
    AMOUNT_CREDIT_IN = "1.00"
    AMOUNT_CREDIT_OUT = "10.00"
    CREDIT_IN = "9"
    CREDIT_OUT = "10"
    DESCRIPTION_WITHDRAW = "Test"
    STATUS_WITHDRAW = "Approved"
    PAYMENT_METHOD_WITHDRAW = "Credit card"
    DESCRIPTION_DEPOSIT = "Description Deposit"
    DESCRIPTION_TRANSFER_BETWEEN_TA = "Description Transfer Between Ta"
    STATUS_DEPOSIT = "Approved"
    PAYMENT_METHOD_DEPOSIT = "Credit card"
    WITHDRAW = "7"
    DEPOSIT = "6"
    CREATE_MT4_USER = "1"
    UPDATE_MT4_USER = "2"
    AMOUNT_DEPOSIT = "10.00"
    AMOUNT_WITHDRAW = "15"
    AMOUNT_DEPOSIT_FOR_CREDIT_OUT = "1.00"
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


