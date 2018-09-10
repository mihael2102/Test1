import time

class ApiConstants(object):
    # Request. HEADER. Field names for requests. Key values for JSON
    FIELD_NAME_CONTENT_TYPE = 'content-type'
    FIELD_NAME_AUTHORIZATION = 'Authorization'

    # RESPONSE. Keys of JSON object
    RESPONSE_JSON_KEY_DATA = "data"
    RESPONSE_JSON_VALUE_TOKEN = "token"

    # AFFILIATE
    # Field names for requests. Key values for JSON
    FIELD_NAME_PARTNER_ID = "partnerId"
    FIELD_NAME_TIME = "time"
    FIELD_NAME_ACCESS_KEY = "accessKey"
    # Info about affiliate
    AFFILIATE_INFO_API = "Affiliate_info_api"
    PARTNER_SECRET_KEY = "partner_secret_key"
    MILLIS_TIME = int(round(time.time()))

    # NEW CLIENT
    # Info about new client
    CLIENT_1_INFO_API = "client_1_api"
    # Field names for requests. Key values for JSON
    FIELD_NAME_EMAIL = "email"
    FIELD_NAME_PASSWORD = "password"
    FIELD_NAME_COUNTRY = "country"
    FIELD_NAME_FIRSTNAME = "firstName"
    FIELD_NAME_LASTNAME = "lastName"
    FIELD_NAME_PHONE = "phone"


