from datetime import *
import random

from dateutil.relativedelta import relativedelta


class CampaignsConstants(object):
    SECOND_ASSIGNED_TO = "second_assigned_to"
    FIST_ASSIGNED_TO = "first_assigned_to"
    FIST_DEAL = "first_deal"
    SECOND_DEAL = "second_deal"
    THIRD_DEAL = "third_deal"
    first_random_number = str(random.randrange(1, 9999))
    second_random_number = str(random.randrange(1, 99))
    MODULE = "Campaigns"
    CAMPAIGN_MODULE_INFO = "Campaigns_info_1"
    CAMPAIGN_NAME = "Campaign name " + first_random_number
    FIRST_ACTIVITY = "first_activity"
    SECOND_ACTIVITY = "second_activity"
    FIRST_START_DATE = datetime.now()
    SECOND_START_DATE = datetime.now() + relativedelta(days=1)
    FIRST_END_DATE = datetime.now() + relativedelta(days=2)
    SECOND_END_DATE = datetime.now() + relativedelta(days=2)
    FORMAT_DATE = "%Y-%m-%d"
    SECOND_FORMAT_DATE = "%d"
    RATE = second_random_number
