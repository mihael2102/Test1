import random
import string
from datetime import *
from dateutil.relativedelta import relativedelta


class QuestionnaireConstants(object):
    random_number = str(random.randrange(1, 9999999))
    CUSTOMER_CLASSIFICATION_EMPTY = ""
    CUSTOMER_CLASSIFICATION_BLOCKED = "Blocked"
    CUSTOMER_CLASSIFICATION_NEGATIVE = "Negative"
    SSN_TIN = "123123"
    NAT_ID = "123123"
    COUNTRY_TAX = "Germany"
    COMPANY_NAME = "Test"
    EMPLOYMENT_STATUS_STUDENT = "Student"
    EDUCATION_LEVEL_NO_EDUCATION = "No Education"
    POLITICALLY_EXPOSED_PERSON_NO = "No"
    TOTAL_ANNUAL_INCOME_UNDER_15 = "Under €15,000"
    APPROXIMATE_NET_WEALTH_UNDER_15 = "Under €15,000"
    EXPECTED_DEPOSIT_UNDER_10 = "Under €10,000"
    SOURCE_TRADING_FUNDS_EMPLOYMENT = "Employment / Business Income or Savings"
    WHY_WANT_TRADE_SPECULATIVE = "Speculative"
    REACT_ON_LOSSES_EXPECT_TO_LOSE = \
       "I expect to lose sometimes. It’s part of trading. If I make a loss, I’ll review and revise my trading strategy."
    INSTRUMENTS_TRADED_BEFORE_NO_EXPERIENCE = "No trading Experience"
    IF_APPLICABLE_NONE = "None of the above."
    REGARDING_CFD = "are non-risky"
    REGARDING_CFD_RETAIL = "are speculative, complex and risky"
    FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS = "Employee layoffs"
    FACTOR_AFFECT_PRICES_EMPLOYEE_LAYOFFS_RETAIL = "Interest Rates and Economic Releases/Announcements"
    WHERE_CLOSE_BMW_POSITION_LONDON = "At the London Stock Exchange"
    WHERE_CLOSE_BMW_POSITION_RETAIL = "Only through our platform"
    REQUIRED_MARGIN_100 = "€100,000"
    REQUIRED_MARGIN_1000 = "€1,000"
    LOSS_AMOUNT_800 = "€800"
    MESSAGE_NEGATIVE = "Dear customer, Based on the information you have submitted, please note that you do not appear to posses the appropriate knowledge and experience to deal in the financial instruments and services our company offers, since these are considered as complex products. We are concerned you do not understand the risks involved. Therefore, we do not recommend you proceed with the opening of a live trading account and opened a demo account for you to review and gain some experience in our platform."
    MAIL_CLIENT_EMPTY = "pandaqa" + random_number + "empty@pandats.com"
    MAIL_CLIENT_BLOCKED = "pandaqa" + random_number + "blocked@pandats.com"
    MAIL_CLIENT_NEGATIVE = "pandaqa" + random_number + "negative@pandats.com"
