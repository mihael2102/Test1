import random
import string


class CreateAffiliateConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    PARTNER_NAME = "testqa%s" % random_character
    ALLOWED_IP = "1.1.1.1"
    ALLOWED_METHOD = "Create lead"
    BLOCKED_COUNTRY = "Albania"
