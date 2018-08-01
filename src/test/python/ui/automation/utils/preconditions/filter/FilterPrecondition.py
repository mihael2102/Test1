from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TradingAccountConstants import TradingAccountConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config


class FilterPrecondition(object):

    def create_filter_clients_module(self):
        CRMHomePage().open_client_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_client_module(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.FILTER_NAME),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.FIRST_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SECOND_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.THIRD_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.FOURTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.FIFTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SIXTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SEVENTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.EIGHTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.NINTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.TENTH_COLUMN),
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.ELEVENTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition()

    def create_filter_help_desk(self):
        CRMHomePage().open_help_desk_page() \
            .open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FILTER_NAME),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FIRST_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SECOND_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.THIRD_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FOURTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.FIFTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SIXTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.SEVENTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.EIGHTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.TENTH_COLUMN),
            Config.data.get_data_help_desk(HelpDeskConstants.HELP_DESK_COLUMNS, HelpDeskConstants.ELEVENTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition()

    def create_filter_leads_module(self):
        CRMHomePage().open_lead_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_lead_module(
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.FILTER_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.FIRST_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.SECOND_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.THIRD_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.FOURTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.FIFTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.SIXTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.SEVENTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                           LeadsModuleConstants.EIGHT_COLUMN)) \
            .click_save_button()
        return FilterPrecondition()

    def create_filter_documents_module(self):
        CRMHomePage().open_more_list_modules() \
            .select_document_module_more_list(DocumentModuleConstants.DOCUMENT) \
            .open_create_filter_pop_up() \
            .perform_create_filter_documents_module(
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FILTER_NAME),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FIRST_COLUMN),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.SECOND_COLUMN),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.THIRD_COLUMN),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_COLUMNS,
                                                 DocumentModuleConstants.FOURTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition()

    def create_filter_trading_account_module(self):
        CRMHomePage().open_trading_account_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_trading_accounts_module(
            Config.data.get_data_columns_trading_module(TradingAccountConstants.FILTER_NAME),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.FIRST_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.SECOND_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.THIRD_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.FOURTH_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.FIFTH_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.SIXTH_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.SEVENTH_COLUMN),
            Config.data.get_data_columns_trading_module(TradingAccountConstants.EIGHTH_COLUMN)) \
            .click_save_button()
        return FilterPrecondition()
