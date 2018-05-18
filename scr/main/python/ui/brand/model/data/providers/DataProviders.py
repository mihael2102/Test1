import json

from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CAClientUpdate import CAClientUpdate
from scr.test.python.utils.TestDataConstants import TestDataConstants
from scr.test.python.utils.XpathDataConstants import XpathDataConstants


class DataProviders(object):

    def get_data_first_client(self, value):
        connection_file = open(
            'scr/test/python/resources/test-data/client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TestDataConstants.CLIENT_ONE][value]

    def get_xpath_data(self, value):
        connection_file = open(
            'scr/test/python/resources/client_area.json')
        conn_string = json.load(connection_file)
        return conn_string[XpathDataConstants.CRM_HOME_PAGE][value]

    def get_data_client_information_update(self, value):
        connection_file = open(
            'scr/test/python/resources/test-data/client-information-update.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE][value]
