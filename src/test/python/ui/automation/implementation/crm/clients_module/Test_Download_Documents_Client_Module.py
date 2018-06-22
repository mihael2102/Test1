from src.main.python.ui.crm.model.constants.CRMDocumentConstants import CRMDocumentConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class TestDownloadDocumentsClientModule(BaseTest):

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

        document_module.perform_download_document() \
            .set_document_type(Config.data.get_crm_data(CRMDocumentConstants.FIRST_DOCUMENT_TYPE)) \
            .set_status(Config.data.get_crm_data(CRMDocumentConstants.FIRST_STATUS)) \
            .set_expire_date(Config.data.get_crm_data(CRMDocumentConstants.EXPIRE_DATE_DOCUMENT)) \
            .set_description_date(Config.data.get_crm_data(CRMDocumentConstants.COMMENTS))
