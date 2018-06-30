import pytest

from src.main.python.ui.crm.model.constants.DocumentClientsModuleConstants import DocumentClientsModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=21)
class CreateDocument(BaseTest):

    def test_create_document(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        document_module = CRMHomePage().open_more_list_modules() \
            .select_document_module_more_list(DocumentClientsModuleConstants.DOCUMENT)

        document_module.open_create_document_module().perform_create_document(
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_STATUS),
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.COMMENTS))

        message = document_module.get_successful_message()

        assert message == DocumentClientsModuleConstants.MESSAGE_SUCCESSFUL

        document_module.click_ok()

        document_view_page = document_module.open_pending_tab().open_document_number()

        document_type = document_view_page.get_document_type()
        document_status = document_view_page.get_document_status()
        document_comment = document_view_page.get_document_comment()

        assert document_type == Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_DOCUMENT_TYPE)
        assert document_status == Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_STATUS)
        assert document_comment == Config.data.get_data_document_crm(DocumentClientsModuleConstants.COMMENTS)

    def test_delete_document(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        document_module = CRMHomePage().open_more_list_modules() \
            .select_document_module_more_list(DocumentClientsModuleConstants.DOCUMENT)

        document_module.open_create_document_module().perform_create_document(
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.FIRST_STATUS),
            Config.data.get_data_document_crm(DocumentClientsModuleConstants.COMMENTS))

        document_module.click_ok()

        message_delete_document = document_module.open_pending_tab() \
            .select_document_by_delete_button() \
            .click_yes_button() \
            .get_successful_message()

        assert message_delete_document == DocumentClientsModuleConstants.MESSAGE_DELETE_DOCUMENT
        document_module.click_ok()
