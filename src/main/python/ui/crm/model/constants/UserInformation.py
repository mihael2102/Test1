import random


class UserInformation(object):
    USER_MANAGEMENT = "User Management"
    random_number = str(random.randrange(1, 999999))
    FIRST_USER = "FirstUser"
    FIRST_USER_NAME = "pandatest" + random_number
    FIRST_EMAIL = "pandaqa+%s@pandats.com" % random_number
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    ROLE = "Support Rep"
    ROLE2 = "Vice President"
    ROLE3 = "IT Manager"
    ROLE1 = "Panda Success"
    FIRST_ROLE = "first_role"
    FIRST_PASSWORD = "first_password"
    FIRST_CONFIRM_PASSWORD = "first_confirm_password"
    FIRST_LAST_NAME = "first_last_name"
    PASSWORD = "Test12345"