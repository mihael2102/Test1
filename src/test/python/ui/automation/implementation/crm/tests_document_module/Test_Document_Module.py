import pytest

from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.documents_module.DocumentPrecondition import DocumentPrecondition


@pytest.mark.run(order=22)
class DocumentModuleTest(BaseTest):

    def test_searching_by_columns(self):

        DocumentPrecondition(self.driver, self.config).searching_by_columns()

    def test_create_document(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        document_module = CRMHomePage().open_more_list_modules() \
            .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)

        document_module.open_create_document_module().perform_create_document(
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.FIRST_STATUS),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.COMMENTS))

        message = document_module.get_successful_message()

        assert message == DocumentModuleConstants.MESSAGE_SUCCESSFUL

        document_module.click_ok()

        document_view_page = document_module.open_pending_tab().open_document_number()

        document_type = document_view_page.get_document_type()
        document_status = document_view_page.get_document_status()
        document_comment = document_view_page.get_document_comment()

        assert document_type == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                                     DocumentModuleConstants.FIRST_DOCUMENT_TYPE)
        assert document_status == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                                       DocumentModuleConstants.FIRST_STATUS)
        assert document_comment == Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                                        DocumentModuleConstants.COMMENTS)

    def test_delete_document(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        document_module = CRMHomePage().open_more_list_modules() \
            .select_documents_module_more_list(DocumentModuleConstants.DOCUMENT)

        document_module.open_create_document_module() \
            .perform_create_document(
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.FIRST_STATUS),
            Config.data.get_data_document_module(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                                 DocumentModuleConstants.COMMENTS))

        document_module.click_ok()

        message_delete_document = document_module.open_pending_tab() \
            .select_document_by_delete_button() \
            .click_yes_button() \
            .get_successful_message()

        assert message_delete_document == DocumentModuleConstants.MESSAGE_DELETE_DOCUMENT
        document_module.click_ok()
