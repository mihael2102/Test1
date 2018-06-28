import json
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.DocumentClientsModuleConstants import DocumentClientsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
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
        return conn_string[DocumentClientsModuleConstants.CRM_ADD_DOCUMENT][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/mass_edit_information.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/mass_sms_information.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/crm_information.json')
        conn_string = json.load(connection_file)
        return conn_string[TaskModuleConstants.TASK_MODULE][value]
