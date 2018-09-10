import json
import os
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.AffiliatePageConstants import AffiliatePageConstants
from src.main.python.ui.crm.model.constants.ApiConstants import ApiConstants
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.ReportConstants import ManagementReportConstants, TradingReportConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.utils.config import Config


class DataProviders(object):

    def __init__(self):
        self.path_to_data_provider = ""
        # Path to current directory where current file is located
        fileDir = os.path.dirname(__file__)

        # If "jenkins" in filePath, set DataProvider path to jenkins folder on server
        if "jenkins" in fileDir:
            self.path_to_data_provider = "C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/" % Config.test
        # If tests are run locally, set local DataProvider path
        elif ("D:/automation-newforexqa" in fileDir) or ("D:\\automation-newforexqa" in fileDir):
            self.path_to_data_provider = "D:/automation-newforexqa/src/test/python/resources/test-data/"
        # If tests are run neither on server nor locally, throw an exception and check path
        else:
            raise Exception("Wrong path to Data Provider. Please check it")

    def get_data_client(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_api_client_information(self, value):
        connection_file = open(
            self.path_to_data_provider + 'client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[ApiConstants.CLIENT_1_INFO_API][value]

    def get_data_api_affiliate_information(self, value):
        connection_file = open(
            self.path_to_data_provider + 'client-information.json')
        conn_string = json.load(connection_file)
        return conn_string[ApiConstants.CLIENT_1_INFO_API][value]

    def get_data_campaign_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'campaigns-information.json')
        conn_string = json.load(connection_file)
        return conn_string[CampaignsConstants.CAMPAIGN_MODULE_INFO][value]

    def get_data_management_report_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'reports-information.json')
        conn_string = json.load(connection_file)
        return conn_string[ManagementReportConstants.MANAGEMENT_REPORT_INFO][value]

    def get_data_trading_report_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'reports-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TradingReportConstants.TRADING_REPORT_INFO][value]

    def get_data_document_module(self, key, value):
        # exclude this method from usages. Instead of it please use more specific methods below
        connection_file = open(
            self.path_to_data_provider + 'documents-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_document_module_information(self, value):
        connection_file = open(
            self.path_to_data_provider + 'documents-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[DocumentModuleConstants.DOCUMENTS_INFO_MODULE][value]

    def get_data_tabs_trading_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'trading-account-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_TABS][value]

    def get_data_columns_trading_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'trading-account-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_COLUMNS][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            self.path_to_data_provider + 'client-information-update_ca.json')
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            self.path_to_data_provider + 'tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            self.path_to_data_provider + 'tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'tasks-module.json')
        conn_string = json.load(connection_file)
        return conn_string[TaskModuleConstants.TASK_MODULE][value]

    def get_data_lead_info(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'leads-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_financial_transactions_info(self, value):
        connection_file = open(
            self.path_to_data_provider + 'financial-transactions-information.json')
        conn_string = json.load(connection_file)
        return conn_string[FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE][value]

    def get_data_audit_logs_info(self, value):
        connection_file = open(
            self.path_to_data_provider + 'audit-logs-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AuditLogsConstants.AUDIT_LOGS_MODULE_INFO][value]

    def get_data_auto_assign_info(self, value):
        connection_file = open(
            self.path_to_data_provider + 'auto-assign-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AutoAssignConstants.AUTO_ASSIGN_INFO][value]

    def get_data_user_info(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'user-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_affliate_info(self, value):
        connection_file = open(
            self.path_to_data_provider + 'affiliate-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AffiliatePageConstants.AFFILIATE_INFO][value]

    def get_data_affliate_info_edited(self, value):
        connection_file = open(
            self.path_to_data_provider + 'affiliate-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AffiliatePageConstants.AFFILIATE_INFO_EDITED][value]

    def get_data_help_desk(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'help-desk-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]
