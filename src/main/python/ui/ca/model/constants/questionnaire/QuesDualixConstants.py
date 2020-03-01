import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class QuesDualixConstants(object):
    random_number = str(random.randrange(1, 9999999))

    LIST_1 = "Are you a Politically Exposed Person (PEP)?"
    LIST_2 = "What is the purpose and reason for requesting the establishment of a business relationship with the Company?"
    LIST_3 = "What is your estimated amount of investment with our Company (EUR)?"
    LIST_4 = "Expected nature of transaction"
    LIST_5 = "Expected origin of Incoming Funds"
    LIST_6 = "Source of Funds"
    LIST_7 = "Types of services are you familiar with:"
    LIST_8 = "Please select the financial instruments with which you are familiar with:"
    LIST_9 = "Select the nature of your transactions in financial instruments"
    LIST_10 = "The period over which your last transactions in financial instruments have been carried out."
    LIST_11 = "What is your average trade size (volume) of during the last 4 quarters?"
    LIST_12 = "When was the aforementioned annual investment volume has been carried out:"
    LIST_13 = "What is your approximate Size of Portfolio (financial instruments + cash):"
    LIST_14 = "Select the frequency of your transactions in financial instruments"
    LIST_15 = "What is your Employment Status?"
    LIST_16 = "Level of Education:"
    LIST_17 = "Does your education relate to financial industry?"
    LIST_18 = "Does your current or past proffession relate to?"
    LIST_19 = "What is your size of wealth? (Estimated in EUR)"
    LIST_20 = "What is your annual income? (Estimated in EUR)"
    LIST_21 = "How do you think you will react if you incur trading losses?"
    LIST_22 = "Which of the following is correct regarding Contracts for Difference (CFDs)?"
    LIST_23 = "What is the main factor that can affect the prices of the underlying currency exchange (forex) markets?"
    LIST_24 = "Country of Tax"
    LIST_25 = "Are you a US reportable person?"

    FIELD_1 = "SSN/TIN"
    FIELD_2 = "National ID"
    FIELD_3 = "Company Name"

    ITEM_1 = "No"
    ITEM_2 = "Additional Income"
    ITEM_3 = "More than €350,000"
    ITEM_4 = "Crypto"
    ITEM_5 = "Bank Wire"
    ITEM_6 = "Investments"
    ITEM_7 = "Execution"
    ITEM_8 = "Crypto"
    ITEM_9 = "Savings"
    ITEM_10 = "Between 0-6 months ago"
    ITEM_11 = "More than €50,000"
    ITEM_12 = "Between 0-6 months ago"
    ITEM_13 = "€500,001 – €700,000"
    ITEM_14 = "Weekly"
    ITEM_15 = "Employed"
    ITEM_16 = "High School"
    ITEM_17 = "No"
    ITEM_18 = "Banking, Business, Economics"
    ITEM_19 = "More than €250,000"
    ITEM_20 = "More than €250,000"
    ITEM_21 = "I expect to lose sometimes. It is part of trading. If I make a loss, I will review and revise my trading strategy."
    ITEM_22 = "They are speculative, complex and risky."
    ITEM_23 = "Interest Rates and Economic Releases/Announcements"
    ITEM_23_CRM = "Interest Rates and Economic Releases/Announcements."
    ITEM_24 = "Germany"
    ITEM_25 = "No"

    SSN = "123123"
    ID = "11111"
    COMPANY_NAME = "TEST COMPANY"

    SECTION_KNOWLEDGE = "Knowledge"
    SECTION_PERS_PROFILE = "Personal Profile"
