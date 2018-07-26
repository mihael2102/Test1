import random


class UserInformation(object):
    USER_MANAGEMENT = "User Management"
    random_number = str(random.randrange(1, 9999))
    FIRST_USER = "FirstUser"
    FIRST_USER_NAME = "User_testing+ " + random_number
    FIRST_EMAIL = "testing+%s@pandats.com" % random_number
    FIRST_NAME = "first_name"
    FIRST_ROLE = "first_role"
    FIRST_PASSWORD = "first_password"
    FIRST_CONFIRM_PASSWORD = "first_confirm_password"
    FIRST_LAST_NAME = "first_last_name"
