import hashlib
import json
import requests

from src.main.python.ui.crm.model.constants.ApiConstants import ApiConstants


class ApiPage():
    def __init__(self, partner_id, partner_secret_key, millis_time, auth_url):
        super().__init__()
        self.partner_id = str(partner_id)
        self.partner_secret_key = str(partner_secret_key)
        self.millis_time = str(millis_time)
        self.auth_url = auth_url

    def get_generated_token_api(self):
        # POST REQUEST
        # Generate Access key
        concatenated_string = self.partner_id + str(self.millis_time) + self.partner_secret_key
        accessKey = hashlib.sha1(concatenated_string.encode()).hexdigest()

        # Send params in first request to get token.
        parameters = {ApiConstants.FIELD_NAME_PARTNER_ID: self.partner_id, ApiConstants.FIELD_NAME_TIME: self.millis_time, ApiConstants.FIELD_NAME_ACCESS_KEY: accessKey}
        response_with_auth_token = requests.post(self.auth_url, data=parameters)

        # Read the JSON responce
        response_as_dict_object = json.loads(response_with_auth_token.text)

        # Read token value from JSON object
        token = response_as_dict_object[ApiConstants.RESPONSE_JSON_KEY_DATA][ApiConstants.RESPONSE_JSON_VALUE_TOKEN]
        return "Bearer " + token

    def api_create_client(self, generated_token, url_create_client, content_type, client_email, client_password, client_country, client_first_name, client_last_name, client_phone):
        header = {ApiConstants.FIELD_NAME_CONTENT_TYPE: content_type, ApiConstants.FIELD_NAME_AUTHORIZATION: generated_token}

        new_client = {ApiConstants.FIELD_NAME_EMAIL: client_email, ApiConstants.FIELD_NAME_PASSWORD: client_password, ApiConstants.FIELD_NAME_COUNTRY: client_country, ApiConstants.FIELD_NAME_FIRSTNAME: client_first_name, ApiConstants.FIELD_NAME_LASTNAME: client_last_name, ApiConstants.FIELD_NAME_PHONE: client_phone}


        result = requests.post(url_create_client, headers=header, data=new_client)
        return ""


