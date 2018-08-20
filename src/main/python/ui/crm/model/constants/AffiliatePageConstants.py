import random

import time


class AffiliatePageConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)

    AFFILIATES_MODULE = "Affiliates"
    AFFILIATE_INFO = "Affiliate_info"
    AFFILIATE_INFO_EDITED = "Affiliate_info_edited"
    BRAND_NEW_FOREX = "first_brand"
    BRAND_NFX = "second_brand"
    PARTNER_NAME = "partner_name " + random_number
    PARTNER_NAME_EDITED = "partner_name " + random_number_edited
    ALLOWED_IP = "allowed_ip"
    IS_ENABLED = "is_enabled"
    FIRST_ALLOWED_METHOD = "allowed_methods_1"
    FIRST_ALLOWED_METHOD_NAME = "allowed_methods_1_name"
    SECOND_ALLOWED_METHOD = "allowed_methods_2"
    SECOND_ALLOWED_METHOD_NAME = "allowed_methods_2_name"
    THIRD_ALLOWED_METHOD = "allowed_methods_3"
    THIRD_ALLOWED_METHOD_NAME = "allowed_methods_3_name"
    FOURTH_ALLOWED_METHOD = "allowed_methods_4"
    FOURTH_ALLOWED_METHOD_NAME = "allowed_methods_4_name"
    FIFTH_ALLOWED_METHOD = "allowed_methods_5"
    FIFTH_ALLOWED_METHOD_NAME = "allowed_methods_5_name"
    EDITED_FIRST_ALLOWED_METHOD = "edited_allowed_methods_1"
    EDITED_FIRST_ALLOWED_METHOD_NAME = "edited_allowed_methods_1_name"
    FIRST_COUNTRY = "blocked_countries_1"
    SECOND_COUNTRY = "blocked_countries_2"
    THIRD_COUNTRY = "blocked_countries_3"
    FOURTH_COUNTRY = "blocked_countries_4"
    FIFTH_COUNTRY = "blocked_countries_5"
    EDITED_COUNTRY_1 = "edited_countries_1"
    DELETED_AFFILIATE_TEXT = "Data not found"


