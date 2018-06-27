import json
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.CRMDocumentConstants import CRMDocumentConstants
from src.main.python.ui.crm.model.constants.CRMMassEditConstants import CRMMassEditConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.test.python.utils.TestDataConstants import TestDataConstants

class DataProviders(object):

    def get_data_first_client(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TestDataConstants.CLIENT_ONE][value]

    def get_data_document_crm(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/crm_information.json')
        conn_string = json.load(connection_file)
        return conn_string[CRMDocumentConstants.CRM_ADD_DOCUMENT][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/mass_edit_information.json')
        conn_string = json.load(connection_file)
        return conn_string[CRMMassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/mass_sms_information.json')
        conn_string = json.load(connection_file)
        return conn_string[CRMMassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/crm_information.json')
        conn_string = json.load(connection_file)
        return conn_string[CRMTaskModuleConstants.TASK_MODULE][value]
