from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from scr.main.python.ui.brand.model.client_area_modules.verification_center.CaVerificationCenter import \
    CaVerificationCenter
from scr.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.utils.TestDataConstants import TestDataConstants


class DownloadDocuments(BaseTest):

    def test_make_dowload_documents(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.VERIFICATION_CENTER)

        status_document_ca = CaVerificationCenter().perform_front_upload().get_document_status()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))

        status_document_crm = crm_client_profile \
            .perform_scroll_down() \
            .open_document_tab() \
            .open_document_number() \
            .get_document_status()

        assert status_document_ca == status_document_crm
