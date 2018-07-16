import json
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.DocumentClientsModuleConstants import DocumentClientsModuleConstants
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.test.python.utils.TestDataConstants import TestDataConstants


class DataProviders(object):

    def get_data_client(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TestDataConstants.CLIENT_ONE][value]

    def get_data_filter_crm(self, key, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/filter-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_document_crm(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/crm-information.json')
        conn_string = json.load(connection_file)
        return conn_string[DocumentClientsModuleConstants.CRM_ADD_DOCUMENT][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[TaskModuleConstants.TASK_MODULE][value]

    def get_data_lead_info(self, key, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/leads-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_financial_transactions_info(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/financial_transactions.json')
        conn_string = json.load(connection_file)
        return conn_string[FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE][value]

    def get_data_audit_logs_info(self, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/audit_logs_module.json')
        conn_string = json.load(connection_file)
        return conn_string[AuditLogsConstants.AUDIT_LOGS_MODULE_INFO][value]

    def get_data_user_info(self, key, value):
        connection_file = open(
            'D:/automation-royalcfd-brand/src/test/python/resources/test-data/user-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]
