import json
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.utils.config import Config
import yaml


class ConfigProvider:

    home_config_dir = "src/main/python/utils/config/"
    default_config_file = "default.yml"
    brand = None
    tests = None

    def __init__(self):
        self.data = {}
        self.brands_config = {}
        self.tests_config = {}
        self.load_config()
        self.brands = None

    def load_config(self):
        """
        Loads brands and tests configuration
        """
        with open(self.home_config_dir + "brands.yml", 'r') as stream:
            try:
                self.brands_config = yaml.load(stream)
                print(self.brands_config)
            except yaml.YAMLError as e:
                print(e)
        with open(self.home_config_dir + "tests.yml", 'r') as stream:
            try:
                self.tests_config = yaml.load(stream)
                print(self.tests_config)
            except yaml.YAMLError as e:
                print(e)


    def load_brand_config(self, brand, use_base=True):
        """
        Load a configuration for a specific brand
        :param brand the brand name as specified in the brands_config loaded previously
        :param use_base whether to use the default configuration as a base for the brand configuration
        """
        # load default configuration as a base configuration
        if use_base:
            with open(self.home_config_dir + "brands/" + self.default_config_file, 'r') as stream:
                try:
                    self.data = yaml.load(stream)
                except yaml.YAMLError as e:
                    print(e)
        for config in self.brands_config['brands']:
            if config['name'] != brand:
                continue
            with open(self.home_config_dir + "brands/" + config['config_file'], 'r') as stream:
                try:
                    brand_config = yaml.load(stream)
                    if use_base:
                        self.data = {**self.data, **brand_config}
                    else:
                        self.data = brand_config
                except yaml.YAMLError as e:
                    print(e)

    def get_brands(self):
        if self.brands is None:
            brands_list = []
            for brand in self.brands_config['brands']:
                brands_list.append(brand['name'])
            self.brands = brands_list
        return self.brands

    def get_tests(self):
        if self.tests is None:
            tests_list = []
            for test in self.tests_config['tests']:
                for method in test['tests']:
                    tests_list.append({'module': test['module'], 'class': test['class'], 'method': method})
            self.tests = tests_list
        return self.tests

    def get_data_client(self, key, sub_key=None):
        if sub_key:
            return self.data[key][sub_key]
        else:
            return self.data[key]

    def get_data_campaign_module(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/campaigns-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[CampaignsConstants.CAMPAIGN_MODULE_INFO][value]

    def get_data_document_module(self, key, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/documents-module-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_tabs_trading_module(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/trading-account-module-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_TABS][value]

    def get_data_columns_trading_module(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/trading-account-module-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[TradingAccountConstants.TRADING_ACCOUNT_MODULE_COLUMNS][value]

    def get_data_client_information_update_ca(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/client-information-update_ca.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[CAClientUpdate.CLIENT_UPDATE_CA][value]

    def get_data_mass_edit(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/tasks-module.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_EDIT_CLIENT_MODULE][value]

    def get_data_mass_sms(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/tasks-module.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[MassEditConstants.MASS_SMS_CLIENT_MODULE][value]

    def get_data_task_module(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/tasks-module.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[TaskModuleConstants.TASK_MODULE][value]

    def get_data_lead_info(self, key, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/leads-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_financial_transactions_info(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/financial-transactions-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[FinancialTransactionsModuleConstants.FINANCIAL_TRANSACTIONS_MODULE][value]

    def get_data_audit_logs_info(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/audit-logs-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[AuditLogsConstants.AUDIT_LOGS_MODULE_INFO][value]

    def get_data_auto_assign_info(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/auto-assign-module-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[AutoAssignConstants.AUTO_ASSIGN_INFO][value]

    def get_data_user_info(self, key, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/user-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[key][value]

    def get_data_affliate_info(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/affiliate-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[AffiliateModuleConstants.AFFILIATE_INFO][value]

    def get_data_affliate_info_edited(self, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/affiliate-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[AffiliateModuleConstants.AFFILIATE_INFO_EDITED][value]

    def get_data_help_desk(self, key, value):
        connection_file = open(
            'C:/Users/Administrator/.jenkins/workspace/%s/src/test/python/resources/test-data/help-desk-information.json' % Config.test)
        conn_string = json.load(connection_file)
        return conn_string[key][value]
