import random


class DragonConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)

    LEAD_LAST_NAME = "dragon" + random_number
    LEAD_EMAIL = "pandaqa+dragon" + random_number + "@pandats.com"
    LEAD_ASSIGNED_TO = "Dragon Test"
    PHONE_NUMBER_INVALID = "61298765432312"
    PHONE_NUMBER_INVALID2 = "44791112345623"
    PHONE_NUMBER_INVALID3 = "190539196203213"
    PHONE_NUMBER_VALID = "49619053919620"
    PHONE_NUMBER_HIDDEN = "***"
