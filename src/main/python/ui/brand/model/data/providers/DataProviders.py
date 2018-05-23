import json

from src.main.python.ui.brand.model.client_area_modules.ca_constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.pages.client_profile.CRMClientUpdate import CRMClientUpdate
from src.test.python.utils.TestDataConstants import TestDataConstants
from src.test.python.utils.XpathDataConstants import XpathDataConstants


class DataProviders(object):

    def get_data_first_client(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TestDataConstants.CLIENT_ONE][value]

    def get_xpath_data(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/client_area.json')
        conn_string = json.load(connection_file)
        return conn_string[XpathDataConstants.CRM_HOME_PAGE][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_client_information_update_crm(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information-update_crm.json')
        conn_string = json.load(connection_file)
        return conn_string[CRMClientUpdate.CLIENT_UPDATE_CRM][value]
