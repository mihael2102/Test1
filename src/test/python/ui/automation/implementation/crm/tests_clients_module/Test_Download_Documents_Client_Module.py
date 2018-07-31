from src.main.python.ui.crm.model.constants.DocumentModuleConstants import DocumentModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class DownloadDocumentsClientModule(BaseTest):

    def test_perform_download_document(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        document_module = crm_clients_module_page.perform_scroll_down() \
            .open_document_tab() \
            .open_download_module()

        document_module.perform_create_document_client_profile(
            Config.data.get_data_document_crm(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                              DocumentModuleConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_crm(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                              DocumentModuleConstants.FIRST_STATUS),
            Config.data.get_data_document_crm(DocumentModuleConstants.DOCUMENTS_INFO_MODULE,
                                              DocumentModuleConstants.COMMENTS))

        message = crm_clients_module_page.refresh_page() \
            .get_name_document()

        assert message == DocumentModuleConstants.NAME_DOCUMENT
