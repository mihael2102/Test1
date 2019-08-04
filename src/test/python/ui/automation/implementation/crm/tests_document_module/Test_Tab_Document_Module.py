import pytest

from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=23)
class TabDocumentModule(BaseTest):

    def test_check_tabs_document_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        document_module = CRMHomePage()\
            .open_more_list_modules() \
            .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)

        all_tab_name = document_module.open_tab_listview()
        approved_tab_name = document_module.get_approved_tab_name_text()
        not_approved_tab_name = document_module.get_not_approved_text()
        pending_tab_name = document_module.get_pending_tab_text()

        assert all_tab_name == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_TABS,
                                                                    DocumentModuleConstants.FIRST_TAB)
        assert approved_tab_name == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_TABS,
                                                                         DocumentModuleConstants.SECOND_TAB)
        assert not_approved_tab_name == Config.data.get_data_document_module(
            DocumentModuleConstants.DOCUMENTS_MODULE_TABS,
            DocumentModuleConstants.THIRD_TAB)
        assert pending_tab_name == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_MODULE_TABS,
                                                                        DocumentModuleConstants.FOURTH_TAB)

    # def test_searching_tabs_document_module(self):
    #     CRMLoginPage().open_first_tab_page(Config.url_crm) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                        self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                        self.config.get_value(TestDataConstants.OTP_SECRET))
    #
    #     document = CRMHomePage().open_more_list_modules() \
    #         .select_module_more_list(CRMDocumentConstants.DOCUMENT)
    #
    #     document.open_create_document_module().perform_create_document(
    #         Config.data.get_data_document_crm(CRMDocumentConstants.FIRST_DOCUMENT_TYPE),
    #         Config.data.get_data_document_crm(CRMDocumentConstants.FIRST_STATUS),
    #         Config.data.get_data_document_crm(CRMDocumentConstants.COMMENTS))
    #
    #     document.open_create_filter_pop_up() \
    #         .perform_create_filter(Config.data.get_data_first_client(CRMConstants.FILTER_NAME),
    #                                Config.data.get_data_first_client(CRMConstants.FIRST_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.SECOND_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.THIRD_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.FOURTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.FIFTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.SIXTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.SEVENTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.EIGHTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.NINTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.TENTH_COLUMN),
    #                                Config.data.get_data_first_client(CRMConstants.ELEVENTH_COLUMN)) \
    #         .click_save_button()
    #
    #     document.click_ok().open_pending_tab().perform_searching()
