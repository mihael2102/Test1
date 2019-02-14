import random
from datetime import *
from dateutil.relativedelta import relativedelta


class CAConstants(object):
    STATUS_DOCUMENTS_APPROVED_CA = "Document Verified"
    STATUS_DOCUMENTS_APPROVED = "Approved"
    DOCUMENTS = "Bear.jpg"
    TICKET_CLOSED_CA = "CLOSED"
    TICKET_AA = "Awaiting Agent"
    TICKET_AC = "Awaiting Client"
    TICKET_CLOSED_BY_CLIENT = "Closed by Client"
    TICKET_CLOSED = "Closed"
    TICKET_IN_PROGRESS = "In Progress"
    TICKET_IN_PROGRESS_CA = "IN PROGRESS"
    TICKET_OPEN = "OPEN"
    TICKET_OPEN_CRM = "Open"
    TICKET_SUBJECT = "Tichet Subject" + str(random.randrange(1, 999))
    TICKET_DESCRIPTION = "this is ticket description"
    TICKET_CATEGORY = "Login Problem"
    DEMO = "demo"
    NEW_ADDRESS = "THISISNEWADDRESS"
    NEW_CITY = "THISISNEWCITY"
    NEW_CODE = "999"
    LEVERAGE = "1:100"
    PASSWORD = "as1as2as1as2"
    DAY_BIRTH = "10"
    MONTH_BIRTH = "12"
    YEAR_BIRTH = "1995"
    CURRENCY = "EUR"
    CURRENCY_USD = "USD"
    CITY = "Berlin"
    ZIP_CODE = "123"
    ADDRESS = "Street10"
    CITIZENSHIP = "Germany"
    CITIZENSHIP_AUS = "Mexico"
    CITIZENSHIP_SOUTH_A = "South Africa"
    ACCOUNT_TYPE = "Pro"
    AREA_CODE = "555"
    PHONE = "4562456245"
    DATA_MONTH_YEAR = "1996-12-10"