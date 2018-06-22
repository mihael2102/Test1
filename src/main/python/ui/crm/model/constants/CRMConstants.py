from datetime import *
from dateutil.relativedelta import relativedelta


class CRMConstants(object):
    SEND_SMS_MESSAGE = "Message was sent successfully"
    MASS_ASSIGN_MESSAGE = "3 accounts assigned to Panda Support"
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
    FILTER_NAME = "test_filter2"
    CLIENT_STATUS = "client_status_1"
    BRAND_NEW_FOREX = "brand_one"
    TRANSFER_BETWEEN_TA_MESSAGE = "Funds were transferred successfully"
    AMOUNT_TRANSFER_BETWEEN_TA = "15.00"
    TRANSFER_BETWEEN_TA = "8"
    DESCRIPTION_ADD_INTERACTION = "Description Interaction"
    PRIORITY = "Medium"
    ASSIGN_TO = "Default User"
    DATE = datetime.now()
    DURATION = "30M"
    EVENT_TYPE = "Meeting"
    EVENT_STATUS = "In Progress"
    WITHDRAW_SUCCESSFULLY = "MT4 Withdraw successfull"
    DEPOSIT_SUCCESSFULLY = "MT4 Deposit successfull"
    PASSWORD_CHANGE = "Password was change successfully"
    MASS_EDIT = "Successfuly updated"
    CHANGE_PASSWORD = "4"
    PASSWORD_MESSAGE = "Entered password valid"
    CHECK_PASSWORD = "3"
    EXPIRE_DATE = datetime.now() + relativedelta(days=2)
    FORMAT_DATE = "%d-%m-%Y"
    FORMAT_TIME = "%H:%M:%S"
    CREDIT_IN_COMMENT = "Credit in "
    CREDIT_OUT_COMMENT = "Credit out "
    AMOUNT_CREDIT_IN = "25.00"
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
    AMOUNT_DEPOSIT = "10.00"
    AMOUNT_WITHDRAW = "15"
    AMOUNT_DEPOSIT_FOR_CREDIT_OUT = "35.00"
    AMOUNT_WITHDRAW_SECOND = "30.00"
    ADD_INTERACTION = "6"
    INTERACTION_SUCCESSFULLY = "Interraction successfully created"
    SHORT_E_MAIL = "short_email"
    SHORT_SECOND_E_MAIL = "short_second_email"
    SHORT_CLIENT_NAME = "short_client_name"
    SHORT_FIRST_NAME = "short_first_name"
    SHORT_LAST_NAME = "short_last_name"
    FIRST_PHONE_TYPE = "first_phone_type"
    DESCRIPTION_SEND_SMS = "Hello"
    COUNTER_SMS = "1"
