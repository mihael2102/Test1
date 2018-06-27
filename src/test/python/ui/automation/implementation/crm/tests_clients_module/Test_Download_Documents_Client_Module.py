from src.main.python.ui.crm.model.constants.CRMDocumentConstants import CRMDocumentConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class DownloadDocumentsClientModule(BaseTest):

    def test_perform_download_document(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        document_module = crm_clients_module_page.perform_scroll_down() \
            .open_document_tab() \
            .open_download_module()

        document_module.perform_create_document(
            Config.data.get_data_document_crm(CRMDocumentConstants.FIRST_DOCUMENT_TYPE),
            Config.data.get_data_document_crm(CRMDocumentConstants.FIRST_STATUS),
            Config.data.get_data_document_crm(CRMDocumentConstants.COMMENTS))
