import json
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants


class DataProviders(object):

    def get_data_client(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_campaign_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/campaigns-information.json')
        conn_string = json.load(connection_file)
        return conn_string[CampaignsConstants.CAMPAIGN_MODULE_INFO][value]

    def get_data_document_module(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/documents-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_tabs_trading_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/trading-account-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_TABS][value]

    def get_data_columns_trading_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/trading-account-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_COLUMNS][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[TaskModuleConstants.TASK_MODULE][value]

    def get_data_lead_info(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/leads-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_financial_transactions_info(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/financial-transactions-information.json')
        conn_string = json.load(connection_file)
        return conn_string[FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE][value]

    def get_data_audit_logs_info(self, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/audit-logs-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AuditLogsConstants.AUDIT_LOGS_MODULE_INFO][value]

    def get_data_user_info(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/user-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_affliate_info(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/affiliate-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_help_desk(self, key, value):
        connection_file = open(
            'D:/automation-newforexqa/src/test/python/resources/test-data/help-desk-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]
