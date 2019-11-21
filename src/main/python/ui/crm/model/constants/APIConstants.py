import random
from datetime import *
from dateutil.relativedelta import relativedelta


class APIConstants(object):
    PARTNER_ID_UFT = "54654"
    PARTNER_ID_EAFX = "10551"
    PARTNER_ID_ANY1PROFIT = "50291"
    API_SECRET_KEY = "5fb7b2998ef7c9223cf14b4db93f7a4cbf79c58749def28ebf1032165888c5f5"
    PARTNER_ID = "3898"
    PASSWORD = "as1as2"
    COUNTRY = "bg"
    COUNTRY1 = "fi"
    COUNTRY2 = "de"
    COUNTRY_LEAD = "li"
    LASTNAME = "testAPI"
    PHONE = "3453453"
    STATUS_OK = "ok"
    STATUS_DUPLICATE_CUSTOMER = "Error 400: Bad Request"
    STATUS_DUPLICATE_CUSTOMER1 = "BL002"
    STATUS_DUPLICATE_CUSTOMER2 = "Customer already exists"
    COUNTRY_CRM = "Germany"
    PHONE_CRM = "+34 53453"
    REFFERAL = "langref=hebrew"
    PAGE = "1"
    LIMIT = "5"
    CHANGE_FIRST_NAME = "test"
    CHANGE_PHONE = "3523233"
    CHANGE_PHONE_CRM = "+352 3233"
    CHANGE_POSTAL_CODE = "777"
    CHANGE_ADDRESS = "Change address"
    CHANGE_CITY = "Change city"
    LEAD_FNAME = "LeadFName"
    LEAD_LNAME = "LeadLName"
    LEAD_PHONE = str(random.randrange(1, 9999999))
    CLIENT_PHONE = str(random.randrange(1, 9999999))
    LEAD_PHONE_CRM = "+352 3233"
    API_filter = "API"
    PAYMENT_DETAILS = "Payment Details"
    PANDATS_EMAIL = "pandats.com"
    FOREX_DEPOSIT = "forexDeposit"
    EMAIL = "pandaqa" + str(random.randrange(1, 9999999)) + "@pandats.com"
