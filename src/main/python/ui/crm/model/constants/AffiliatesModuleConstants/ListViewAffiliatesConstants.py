import random
import string


class ListViewAffiliatesConstants(object):
    random_number = str(random.randrange(1, 9999))
    random_number_edited = random_number + str(10)
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    COLUMN_PARTNER_NAME = "Partner Name"
