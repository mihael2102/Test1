import requests
import time
import hashlib
import json

from src.main.python.ui.crm.model.constants.AffiliatePageConstants import AffiliatePageConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage


class ApiPage():
    def __init__(self, partner_id, partner_secret_key, millis_time, auth_url):
        super().__init__()
        self.partner_id = partner_id
        self.partner_secret_key = partner_secret_key
        self.millis_time = millis_time
        self.auth_url = auth_url

    def api_create_client(self, generated_token, url_create_client):
        header = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Authorization': 'Bearer %s' % generated_token}

        new_client = {"email": "dmytro.k+api011@pandats.com", "password": "as1as2", "country": "de", "firstName": "Dima Api", "lastName": "QA", "phone": "10235145789569"}


        result = requests.post(url_create_client, headers=header, data=new_client)

    def get_generated_token_api(self):
        # POST REQUEST
        # Generate Access key
        concatenated_string = self.partner_id + str(self.millis_time) + self.partner_secret_key
        accessKey = hashlib.sha1(concatenated_string.encode()).hexdigest()

        # Send params in first request to get token.
        parameters = {"partnerId": self.partner_id, "time": self.millis_time, "accessKey": accessKey}
        response_with_auth_token = requests.post(self.auth_url, data=parameters)

        # Read the JSON responce
        response_as_dict_object = {}
        response_as_dict_object = json.loads(response_with_auth_token.text)
        print(response_as_dict_object)

        # Read token value from JSON object
        token = response_as_dict_object["data"]["token"]
        return token



