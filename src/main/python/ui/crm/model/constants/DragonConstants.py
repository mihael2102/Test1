import random


class DragonConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)

    LEAD_LAST_NAME = "dragon" + random_number
    LEAD_EMAIL = "pandaqa+dragon" + random_number
    LEAD_ASSIGNED_TO = "Dragon Test"
    PHONE_NUMBER_INVALID = "61298765432312"
