import random
import string


class LeadsModuleConstants(object):
    CONFIRM_MESSAGE = "File successfully uploaded."
    LAST_IMPORT_NAME_LEAD = "qatesting1"
    FIRST_IMPORT_LEAD = "FirstImportLead"
    random_numbers = str(random.randrange(1, 9999))
    random_character = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    FIRST_ADDRESS_LEAD = "first_address"
    FIRST_CITIZENSHIP = "first_citizenship"
    FIRST_BRAND_LEAD = "first_brand"
    FIRST_REFERRAL_LEAD = "first_referral"
    FIRST_CURRENCY_LEAD = "first_currency"
    FIRST_CURRENCY_LEAD_EUR = "first_currency_eur"
    FIRST_CURRENCY_LEAD_BCH = "first_currency_BCH"
    FIRST_PASSWORD_LEAD = "first_password"
    FIRST_COUNTRY_NAME = "first_country"
    FIRST_CITY_LEAD = "first_city_lead"
    FIRST_POSTAL_CODE_LEAD = "first_postal_code"
    FIRST_BIRTHDAY_LEAD = "first_birthday_lead"
    FIRST_PHONE_LEAD = "first_phone_lead"
    FIRST_EMAIL_LEAD = "test+%s@gmail.com" % random_numbers
    FIRST_LAST_NAME_LEAD = "first_last_name"
    FIRST_NAME_LEAD = "first_name_lead"
    FIRST_LEAD_INFO = "FirstLeadInfo"
    SECOND_LEAD_INFO = "SecondLeadInfo"
    THIRD_LEAD_INFO = "ThirdLeadInfo"
    FIRST_NAME = "first_name"
    SECOND_NAME = "second_name"
    FIRST_NAME_RAND = "first_name%s" % random_character
    SECOND_NAME_RAND = "second_name%s" % random_character
    USER_NAME_RAND = "second_name%s" % random_character
    THIRD_NAME = "third_name"
    FIRST_LAST_NAME = "last_name"
    SECOND_LAST_NAME = "second_name"
    FIRST_MOBILE = "mobile"
    FAX = "fax"
    EMAIL = "email"
    SECONDARY_EMAIL = "secondary_email"
    FIRST_LANGUAGE = "first_language"
    PANDA_PARTNER = "panda_partner_id"
    FIRST_REFERRAL = "first_referral"
    STREET = "street"
    POSTAL_CODE = "postal_code"
    FIRST_COUNTRY = "first_country"
    FIRST_COUNTRY_GERMANY = "first_country_g"
    FIRST_COUNTRY_SA = "first_country_sa"
    FIRST_COUNTRY_ME = "first_country_me"
    FIRST_DESCRIPTION = "first_descriptions"
    PHONE = "phone"
    PHONE_AREA_CODE = "phone_area_code"
    FIRST_TITTLE = "first_tittle"
    FIRST_LEAD_SOURCE = "first_lead_source"
    FIRST_LEAD_STATUS_NO_INTRS = "first_lead_status_no_interest"
    FIRST_LEAD_STATUS = "first_lead_status"
    FIRST_LEAD_STATUS_TEST = "first_lead_status_test"
    FIRST_LEAD_STATUS_NEW = "first_lead_status_new"
    FIRST_LEAD_STATUS1 = "first_lead_status1"
    FIRST_LEAD_STATUS_NEW_LEAD = "first_lead_status_new_lead"
    FIRST_LEAD_STATUS_C_NEW = "first_lead_status_c_new"
    FIRST_LEAD_STATUS_TEST_GMO = "gmo_status"
    FIRST_ASSIGNED_TO = "first_assigned_to"
    FIRST_SOURCE_NAME = "first_source_name"
    THIRD_LEAD_STATUS = "third_lead_status"
    THIRD_SOURCE_NAME = "third_source_name"
    THIRD_LEAD_SOURCE = "third_lead_source"
    THIRD_ASSIGNED_TO = "third_assigned_to"
    BRAND = "brand"
    PO_BOX = "po_box"
    CITY = "city"
    FIRST_STATE = "first_state"
    FIRST_COLUMN = "first_column"
    SECOND_COLUMN = "second_column"
    LAST_NAME_COLUMN_TEXT = "Last Name"
    THIRD_COLUMN = "third_column"
    FOURTH_COLUMN = "fourth_column"
    ASSIGNED_TO_COLUMN_TEXT = "Assigned To"
    FIFTH_COLUMN = "fifth_column"
    SIXTH_COLUMN = "sixth_column"
    SEVENTH_COLUMN = "seventh_column"
    EIGHT_COLUMN = "eight_column"
    EIGHT_COLUMN_STREET = "eight_column_street"
    LEADS_MODULE_COLUMNS = "LeadModuleColumns"
    FILTER_NAME = "filter_name"
    FIRST_UPDATE_LEAD = "FirstUpdateLead"
    SECOND_TITTLE = "second_tittle"
    SECOND_LEAD_SOURCE = "second_lead_source"
    SECOND_LEAD_STATUS = "second_lead_status"
    SECOND_ASSIGNED_TO = "second_assigned_to"
    SECOND_LANGUAGE = "second_language"
    SECOND_SOURCE_NAME = "second_source_name"
    SECOND_REFERRAL = "second_referral"
    SECOND_COUNTRY = "second_country"
    SECOND_DESCRIPTION = "second_descriptions"
    MESSAGE_MASS_EDIT_SUCCESSFULY = "Successfuly updated"
    FIRST_CONVERT_LEAD = "FirstConvertLead"
    BIRTHDAY = "birthday"
    CITIZENSHIP = "citizenship"
