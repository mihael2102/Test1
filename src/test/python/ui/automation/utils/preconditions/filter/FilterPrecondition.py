from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.constants.HelpDeskConstants import HelpDeskConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
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

    def create_filter_service_desk(self):
        CRMHomePage().open_help_desk_page() \
            .open_create_filter_pop_up() \
            .perform_create_filter_help_desk_module(
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.FILTER_INFO),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.FIRST_COLUMN),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.SECOND_COLUMN),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.THIRD_COLUMN),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.FOURTH_COLUMN),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.FIFTH_COLUMN),
            Config.data.get_data_filter_crm(HelpDeskConstants.FILTER_INFO, HelpDeskConstants.SIXTH_COLUMN)) \
            .click_save_button()

    def create_filter_leads_module(self):
        CRMHomePage().open_lead_module() \
            .open_create_filter_pop_up() \
            .perform_create_filter_lead_module(
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.FILTER_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.FIRST_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.SECOND_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.THIRD_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.FOURTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.FIFTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.SIXTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.SEVENTH_COLUMN),
            Config.data.get_data_lead_info(LeadsModuleConstants.FILTER_INFO, LeadsModuleConstants.EIGHT_COLUMN)) \
            .click_save_button()

    def create_filter_documents_module(self):
        CRMHomePage().open_more_list_modules() \
            .select_document_module_more_list(DocumentModuleConstants.DOCUMENT) \
            .open_create_filter_pop_up() \
            .perform_create_documents_module(
            Config.data.get_data_document_crm(DocumentModuleConstants.COLUMNS_INFO,
                                              DocumentModuleConstants.FILTER_NAME),
            Config.data.get_data_document_crm(DocumentModuleConstants.COLUMNS_INFO,
                                              DocumentModuleConstants.FIRST_COLUMN),
            Config.data.get_data_document_crm(DocumentModuleConstants.COLUMNS_INFO,
                                              DocumentModuleConstants.SECOND_COLUMN),
            Config.data.get_data_document_crm(DocumentModuleConstants.COLUMNS_INFO,
                                              DocumentModuleConstants.THIRD_COLUMN),
            Config.data.get_data_document_crm(DocumentModuleConstants.COLUMNS_INFO,
                                              DocumentModuleConstants.FOURTH_COLUMN)) \
            .click_save_button()
