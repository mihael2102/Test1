import random


class DragonConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)

    LEAD_LAST_NAME = "dragon"
    LEAD_EMAIL = "pandaqa+dragon" + random_number + "@pandats.com"
    LEAD_EMAIL1 = "pandaqa+dragon1" + random_number + "@pandats.com"
    LEAD_EMAIL2 = "pandaqa+dragon2" + random_number + "@pandats.com"
    LEAD_EMAIL3 = "pandaqa+dragon3" + random_number + "@pandats.com"
    API_EMAIL = "pandaqa+dragon_api" + random_number + "@pandats.com"
    LEAD_ASSIGNED_TO = "Dragon Test"
    PHONE_NUMBER_INVALID = "61298765432312"
    PHONE_NUMBER_INVALID2 = "44791112345623"
    PHONE_NUMBER_INVALID3 = "190539196203213"
    PHONE_NUMBER_VALID = "49619053919620"
    PHONE_NUMBER_VALID_CA = "619053919620"
    PHONE_NUMBER_INVALID_CA = "111111111111111"
    PHONE_NUMBER_HIDDEN4 = "****"
    PHONE_NUMBER_HIDDEN3 = "***"
    FIRST_NAME_CONVERT = "Test"
    DRAGON_LAST_NAME = "Dragon"
    BIRTHDAY_CONVERT = "1970-01-01"
    ADDRESS_CONVERT = "Test address"
    POST_CODE_CONVERT = "333"
    CITY_CONVERT = "Test City"
    COUNTRY_CONVERT = "Germany"
    EMAIL_VALID_LIST_VIEW = "Send mail"
    EMAIL_VALID_DETAIL_VIEW3 = "***"
    EMAIL_VALID_DETAIL_VIEW4 = "****"
    EMAIL_VALID_SEND_MAIL_POPUP = "****,"
