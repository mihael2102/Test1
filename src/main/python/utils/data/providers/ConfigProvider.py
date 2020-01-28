import json
import os
import collections
import yaml
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

import random
import string

from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.FinancialTransactionsModuleConstants import \
    FinancialTransactionsModuleConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.utils.config import Config
from datetime import *
from dateutil.relativedelta import relativedelta


class ConfigProvider:

    eval_prefix = "EVAL_"
    dir_with_xpath = "../../../ui/crm/model/BrandsXpath/"

    config_dir = "../../../../../test/python/resources/config/processes/"
    default_config_file = "default.yml"
    brand = None
    tests = None

    def __init__(self, current_test_suite=None):
        print("init config")
        self.__current_test_suite = current_test_suite
        self.script_dir = os.path.dirname(__file__)
        self.data = {}
        self.brands_config = {}
        self.tests_config = {}
        self.load_config()
        # self.load_brand_config()
        self.brands = None

        self.path_to_data_provider = ""
        # Path to current directory where current file is located
        fileDir = os.path.dirname(__file__)

        # If "jenkins" in filePath, set DataProvider path to jenkins folder on server
        if "Jenkins" in fileDir:
            self.path_to_data_provider = "C:/Program Files (x86)/Jenkins/workspace/%s/src/test/python/resources/test-data/" % Config.test
            # # If tests are run locally, set local DataProvider path

        elif ("C:/Users/Panda102/automation-newforexqa" in fileDir) or (
                "C:\\Users\\Panda102\\automation-newforexqa" in fileDir):
            self.path_to_data_provider = "C:/Users/Panda102/automation-newforexqa/src/test/python/resources/test-data/"

        elif ("D:/automation-newforexqa" in fileDir) or ("D:\\automation-newforexqa" in fileDir):
            self.path_to_data_provider = "D:/automation-newforexqa/src/test/python/resources/test-data/"
            # If tests are run neither on server nor locally, throw an exception and check path
        else:
            raise Exception("Wrong path to Data Provider. Please check it")

    def load_config(self):
        """
        Loads brands and tests configuration
        """
        self.load_brands()
        self.load_tests()

    def load_brands(self, brand='default', use_base=True):
        if self.__current_test_suite is not None:
            brands_file_path = os.path.join(self.script_dir, self.config_dir, self.__current_test_suite)
            with open(os.path.realpath(brands_file_path), 'r') as stream:
                try:
                    self.brands_config = yaml.load(stream)
                    print(self.brands_config)
                    config_dict = {}
                    if use_base:
                        brands_file_path = os.path.join(self.script_dir, self.config_dir, self.default_config_file)
                        with open(os.path.realpath(brands_file_path), 'r') as stream:
                            try:
                                config_dict = yaml.load(stream)
                            except yaml.YAMLError as e:
                                print(e)
                    brand_config_loaded = False
                    # if not brand:
                    #     brand = 'default'
                    for config in self.brands_config['brands']:
                        if config['name'] != brand:
                            continue
                        config_file_path = os.path.join(self.script_dir, self.config_dir, "Brands/",
                                                        config['config_file'])
                        with open(os.path.realpath(config_file_path), 'r') as stream:
                            try:
                                brand_config = yaml.load(stream)
                                if use_base:
                                    config_dict = self.dict_merge(config_dict, brand_config)
                                else:
                                    config_dict = brand_config
                                brand_config_loaded = True
                            except yaml.YAMLError as e:
                                print(e)

                    if not brand_config_loaded:
                        print("Using default brand configuration")
                    config_dict = self.render_configuration(config_dict)
                    self.data = config_dict
                except yaml.YAMLError as e:
                    print(e)

    def load_tests(self):
        tests_file_path = os.path.join(self.script_dir, self.config_dir, Config.test_list)
        with open(os.path.realpath(tests_file_path), 'r') as stream:
            try:
                self.tests_config = yaml.load(stream)
                print(self.tests_config)
            except yaml.YAMLError as e:
                print(e)

    # def load_brand_config(self, brand='default', use_base=True):
    #     """
    #     Load a configuration for a specific brand
    #     :param brand the brand name as specified in the brands_config loaded previously
    #     :param use_base whether to use the default configuration as a base for the brand configuration
    #     """
    #     # load default configuration as a base configuration
    #     config_dict = {}
    #     if use_base:
    #         brands_file_path = os.path.join(self.script_dir, self.config_dir, self.default_config_file)
    #         with open(os.path.realpath(brands_file_path), 'r') as stream:
    #             try:
    #                 config_dict = yaml.load(stream)
    #             except yaml.YAMLError as e:
    #                 print(e)
    #     brand_config_loaded = False
    #     # if not brand:
    #     #     brand = 'default'
    #     for config in self.brands_config['brands']:
    #         if config['name'] != brand:
    #             continue
    #         config_file_path = os.path.join(self.script_dir, self.config_dir, "Brands/", config['config_file'])
    #         with open(os.path.realpath(config_file_path), 'r') as stream:
    #             try:
    #                 brand_config = yaml.load(stream)
    #                 if use_base:
    #                     config_dict = self.dict_merge(config_dict, brand_config)
    #                 else:
    #                     config_dict = brand_config
    #                 brand_config_loaded = True
    #             except yaml.YAMLError as e:
    #                 print(e)
    #
    #     if not brand_config_loaded:
    #         print("Using default brand configuration")
    #     config_dict = self.render_configuration(config_dict)
    #     self.data = config_dict

    def dict_merge(self, dct, merge_dct, add_keys=True):
        """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
        updating only top-level keys, dict_merge recurses down into dicts nested
        to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
        ``dct``.

        This version will return a copy of the dictionary and leave the original
        arguments untouched.

        The optional argument ``add_keys``, determines whether keys which are
        present in ``merge_dict`` but not ``dct`` should be included in the
        new dict.

        Args:
            dct (dict) onto which the merge is executed
            merge_dct (dict): dct merged into dct
            add_keys (bool): whether to add new keys

        Returns:
            dict: updated dict
        """
        dct = dct.copy()
        if not add_keys:
            merge_dct = {
                k: merge_dct[k]
                for k in set(dct).intersection(set(merge_dct))
            }

        for k, v in merge_dct.items():
            if (k in dct and isinstance(dct[k], dict)
                    and isinstance(merge_dct[k], collections.Mapping)):
                dct[k] = self.dict_merge(dct[k], merge_dct[k], add_keys=add_keys)
            else:
                dct[k] = merge_dct[k]

        return dct

    def render_configuration(self, config):
        """
        Render configuration dictionary. Create actual values for keys with the self.eval_prefix prefix
        :param config: the configuration dictionary
        :return: configuration with the values calculated
        """
        res_config = config.copy()
        for key, value in config.items():
            if isinstance(value, collections.Mapping):
                res_config[key] = self.render_configuration(value)
            else:
                if key.startswith(self.eval_prefix):
                    res_config[key[len(self.eval_prefix):]] = eval(value)
        return res_config

    def reload_configuration(self):
        self.data = self.render_configuration(self.data)

    def get_brands(self):
        """
        Get the list of brands configured. Load the list if not loaded before.
        :return:
        """
        if self.brands is None:
            brands_list = []
            for brand in self.brands_config['brands']:
                brands_list.append(brand['name'])
            self.brands = brands_list
        return self.brands

    def get_tests(self):
        """
        Get the list of tests configured. Load the list if not loaded before.
        :return:
        """
        if self.tests is None:
            tests_list = []
            for test_conf in self.tests_config['tests_config']:
                # handle general directives
                reload_config = False
                reload_config_once = False
                if 'directive' in test_conf:
                    if test_conf['directive'] == 'reload_configuration_once':
                        reload_config_once = True
                    if test_conf['directive'] == 'reload_configuration':
                        reload_config = True
                # add tests to list
                for method in test_conf['tests']:
                    test_item = {'module': test_conf['module'], 'class': test_conf['class'], 'method': method}
                    if reload_config_once or reload_config:
                        test_item['reload_config'] = True
                        reload_config_once = False
                    tests_list.append(test_item)
            self.tests = tests_list
        return self.tests

    # def set_xpath_for_tests(self):
    #     current_brand = global_var.current_brand_name
    #     # Read relevant XPaths from file for current brand
    #     with open(os.path.join(self.script_dir, self.dir_with_xpath, current_brand, (current_brand + "_xpath.yml")), 'r') as stream:
    #         try:
    #             global_var.current_brand_xpath_dict = yaml.load(stream)
    #         except yaml.YAMLError as e:
    #             print(e)

    def get_xpath_for_brand_pages(self):
        current_brand = global_var.current_brand_name
        # Read relevant XPaths from file for current brand
        with open(os.path.join(self.script_dir, self.dir_with_xpath, (current_brand + "_xpath.yml")), 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as e:
                print(e)

    def get_default_xpath_dictionary(self):
        current_brand = global_var.current_brand_name
        # Read relevant XPaths from file for current brand
        with open(os.path.join(self.script_dir, self.dir_with_xpath, "default.yml"), 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as e:
                print(e)

    def get_value(self, key, sub_key=None):
        if sub_key:
            return self.data[key][sub_key]
        else:
            return self.data[key]

    def get_data_client(self, key, sub_key=None):
        return self.get_value(key, sub_key)

    def get_data_campaign_module(self, value):
        connection_file = open(
            self.path_to_data_provider + 'campaigns-information.json')
        conn_string = json.load(connection_file)
        return conn_string[CampaignsConstants.CAMPAIGN_MODULE_INFO][value]

    def get_data_document_module(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'documents-module-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]

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
        return self.get_value(key, value)

    def get_data_lead_info_from_json(self, value):
        connection_file = open(
            self.path_to_data_provider + 'leads-information.json')
        conn_string = json.load(connection_file)
        return conn_string[LeadsModuleConstants.LEADS_MODULE_COLUMNS][value]

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
        return conn_string[AffiliateModuleConstants.AFFILIATE_INFO][value]

    def get_data_affliate_info_edited(self, value):
        connection_file = open(
            self.path_to_data_provider + 'affiliate-information.json')
        conn_string = json.load(connection_file)
        return conn_string[AffiliateModuleConstants.AFFILIATE_INFO_EDITED][value]

    def get_data_help_desk(self, key, value):
        connection_file = open(
            self.path_to_data_provider + 'help-desk-information.json')
        conn_string = json.load(connection_file)
        return conn_string[key][value]
