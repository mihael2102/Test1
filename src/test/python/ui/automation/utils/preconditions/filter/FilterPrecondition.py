from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config
import src.main.python.utils.data.globals.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.filter.FilterPage import FilterPage

class FilterPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_filter_clients_module(self):
        CRMHomePage(self.driver).open_client_module() \
            .open_create_filter_pop_up() \

        if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "intelligent_capital"):
            FilterPage(self.driver).perform_create_filter_client_module(
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FILTER_NAME),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIRST_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SECOND_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.THIRD_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FOURTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIFTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SIXTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SEVENTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.EIGHTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.NINTH_COLUMN),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.TENTH_COLUMN_OTHER_TYPE),
                       self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.ELEVENTH_COLUMN))

        else:
            FilterPage(self.driver).perform_create_filter_client_module(
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FILTER_NAME),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIRST_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SECOND_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.THIRD_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FOURTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.FIFTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SIXTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.SEVENTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.EIGHTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.NINTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.TENTH_COLUMN),
                self.config.get_value(TestDataConstants.MODULE_CLIENTS_FILTER, CRMConstants.ELEVENTH_COLUMN))

        FilterPage(self.driver).click_save_button()
        return FilterPrecondition(self.driver, self.config)

    def create_filter_help_desk(self):
        CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .open_help_desk_page() \
            .open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FIRST_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SECOND_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.THIRD_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FOURTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FIFTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SIXTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SEVENTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.EIGHTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.TENTH_COLUMN),
            self.config.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.ELEVENTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition(self.driver, self.config)

    def create_filter_leads_module(self):
        CRMHomePage(self.driver).open_lead_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_lead_module(
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.FILTER_NAME),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.FIRST_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.SECOND_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.THIRD_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.FOURTH_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.FIFTH_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.SIXTH_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.SEVENTH_COLUMN),
            self.config.get_data_lead_info_from_json(LeadsModuleConstants.EIGHT_COLUMN)) \
            .click_save_button()
        return FilterPrecondition(self.driver, self.config)

    def create_filter_documents_module(self):
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_document_module_more_list(DocumentModuleConstants.DOCUMENT) \
            .open_create_filter_pop_up() \
            .perform_create_filter_documents_module(
            self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FILTER_NAME),
            self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FIRST_COLUMN),
            self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.SECOND_COLUMN),
            self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.THIRD_COLUMN),
            self.config.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FOURTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition(self.driver, self.config)

    def create_filter_trading_account_module(self):
        CRMHomePage(self.driver).open_trading_account_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_trading_accounts_module(
            self.config.get_data_columns_trading_module(TradingAccountConstants.FILTER_NAME),
            self.config.get_data_columns_trading_module(TradingAccountConstants.FIRST_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.SECOND_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.THIRD_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.FOURTH_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.FIFTH_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.SIXTH_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.SEVENTH_COLUMN),
            self.config.get_data_columns_trading_module(TradingAccountConstants.EIGHTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition(self.driver, self.config)
