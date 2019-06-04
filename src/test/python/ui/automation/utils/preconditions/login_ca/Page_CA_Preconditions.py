from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from time import sleep
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class Page_CA_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def switch_between_accounts(self):
        if global_var.current_brand_name != "q8":
            try:
                CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                        .login() \
                                        .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                     LeadsModuleConstants.EMAIL]) \
                                        .enter_password(CAConstants.PASSWORD) \
                                        .click_login() \
                                        .verify()
                CAPage(self.driver).open_accounts_list(CAConstants.ACCOUNT_LIVE) \
                                   .switch_to_account(CAConstants.LIVE_ACCOUNT_NUMBER, CAConstants.ACCOUNT_LIVE) \
                                   .open_accounts_list(CAConstants.ACCOUNT_LIVE) \
                                   .verify_active_account_number(CAConstants.LIVE_ACCOUNT_NUMBER)
                if global_var.current_brand_name == "mpcrypto":
                    CAPage(self.driver).verify_active_account_currency(CAConstants.CURRENCY_CRYPTO)
                else:
                    CAPage(self.driver).verify_active_account_currency(CAConstants.CURRENCY)
                if global_var.current_brand_name != "kontofx":
                    CAPage(self.driver).switch_to_account(CAConstants.DEMO_ACCOUNT_NUMBER, CAConstants.ACCOUNT_DEMO) \
                                       .open_accounts_list(CAConstants.ACCOUNT_DEMO) \
                                       .verify_active_account_number(CAConstants.DEMO_ACCOUNT_NUMBER)
                    if global_var.current_brand_name == "mpcrypto":
                        CAPage(self.driver).verify_active_account_currency(CAConstants.CURRENCY_CRYPTO)
                    else:
                        CAPage(self.driver).verify_active_account_currency(CAConstants.CURRENCY)
                else:
                    Logging().reportDebugStep(self, "Test is not running")

            except (ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                Logging().reportDebugStep(self, "Module does not exist")
                return self
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def update_personal_details_in_ca(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "b-finance") \
                and (global_var.current_brand_name != "tradospot"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .open_ca_menu()
            CAPage(self.driver).open_personal_details()
            if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "trade99":
                CAPage(self.driver).edit_first_name(CAConstants.UPDATE_FIRST_NAME) \
                                   .edit_last_name(CAConstants.UPDATE_LAST_NAME)
            CAPage(self.driver).edit_citizenship(CAConstants.UPDATE_CITIZENSHIP) \
                               .edit_city(CAConstants.UPDATE_CITY) \
                               .edit_zip(CAConstants.UPDATE_ZIP_CODE) \
                               .edit_address(CAConstants.UPDATE_ADDRESS) \
                               .click_save_changes_btn()
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def check_personal_details_in_crm(self):
        # Login to CRM
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "b-finance") \
                and (global_var.current_brand_name != "tradospot"):
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                                self.config.get_value(TestDataConstants.OTP_SECRET)) \
                                     .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                                TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
            sleep(2)
            assert ClientsPage(self.driver).get_citizenship() == CAConstants.UPDATE_CITIZENSHIP
            assert ClientsPage(self.driver).get_client_address() == CAConstants.UPDATE_ADDRESS
            assert ClientsPage(self.driver).get_client_city() == CAConstants.UPDATE_CITY
            assert ClientsPage(self.driver).get_client_code() == CAConstants.UPDATE_ZIP_CODE
            if global_var.current_brand_name != "kontofx" and global_var.current_brand_name != "trade99":
                assert ClientsPage(self.driver).get_client_first_name() == CAConstants.UPDATE_FIRST_NAME
                assert ClientsPage(self.driver).get_client_last_name() == CAConstants.UPDATE_LAST_NAME
            # assert ClientsPage(self.driver).get_citizenship() == CAConstants.UPDATE_CITIZENSHIP
            # assert ClientsPage(self.driver).get_client_address() == CAConstants.UPDATE_ADDRESS
            # assert ClientsPage(self.driver).get_client_city() == CAConstants.UPDATE_CITY
            # assert ClientsPage(self.driver).get_client_code() == CAConstants.UPDATE_ZIP_CODE
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def update_personal_details_in_crm(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET)) \
                                 .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                            TestDataConstants.FILTER))
        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        ClientsPage(self.driver).click_edit_btn() \
                                .edit_first_name(CRMConstants.EDIT_FIRST_NAME) \
                                .edit_last_name(CRMConstants.EDIT_LAST_NAME) \
                                .edit_citizenship(CRMConstants.EDIT_CITIZENSHIP) \
                                .edit_city(CRMConstants.EDIT_CITY) \
                                .edit_zip(CRMConstants.EDIT_ZIP_CODE) \
                                .edit_address(CRMConstants.EDIT_ADDRESS) \
                                .fill_birthday(CRMConstants.BIRTHDAY) \
                                .click_save_changes_btn()

    def check_personal_details_in_ca(self):
        if global_var.current_brand_name == "q8":
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .click_my_account() \
                                    .account_details()
            assert CRMConstants.EDIT_FIRST_NAME == CAPage(self.driver).get_first_name()
            assert CRMConstants.EDIT_LAST_NAME == CAPage(self.driver).get_last_name()
            assert CRMConstants.EDIT_CITY == CAPage(self.driver).get_city()
            assert CRMConstants.EDIT_ADDRESS == CAPage(self.driver).get_address()

        else:
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
            CALoginPage(self.driver).login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .click_hi_user(CRMConstants.EDIT_FIRST_NAME)
            CAPage(self.driver).open_personal_details()
            assert CRMConstants.EDIT_FIRST_NAME == CAPage(self.driver).get_first_name()
            assert CRMConstants.EDIT_LAST_NAME == CAPage(self.driver).get_last_name()
            assert CRMConstants.EDIT_CITIZENSHIP == CAPage(self.driver).get_citizenship()
            assert CRMConstants.EDIT_CITY == CAPage(self.driver).get_city()
            assert CRMConstants.EDIT_ZIP_CODE == CAPage(self.driver).get_zipcode()
            assert CRMConstants.EDIT_ADDRESS == CAPage(self.driver).get_address()

    def upload_document_ca(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify() \
                .open_ca_menu()
            CAPage(self.driver).open_verification_center() \
                               .select_document_type(TestDataConstants.DOCUMENT_TYPE1) \
                               .cklick_upload_btn()\
                               .browse_documents()
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def check_and_update_document_in_crm(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                                self.config.get_value(TestDataConstants.OTP_SECRET)) \
                                     .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                                    TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.EMAIL]) \
                                    .scroll_to_documents_section() \
                                    .open_document_tab() \
                                    .verify_document_name() \
                                    .verify_document_type(TestDataConstants.DOCUMENT_TYPE1) \
                                    .verify_document_status(TestDataConstants.DOCUMENT_STATUS1) \
                                    .open_document_preview() \
                                    .update_document_status(TestDataConstants.DOCUMENT_STATUS)\
                                    .click_save_document_btn() \
                                    .verify_doc_saved_message(TestDataConstants.DOCUMENT_SUCCESSFUL_MESSAGE) \
                                    .scroll_to_documents_section() \
                                    .verify_document_status(TestDataConstants.DOCUMENT_STATUS)
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def check_document_status_in_ca(self):
        if (global_var.current_brand_name != "q8") and (global_var.current_brand_name != "kontofx"):
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify() \
                .open_ca_menu()
            CAPage(self.driver).open_verification_center() \
                               .select_document_type(TestDataConstants.DOCUMENT_TYPE1) \
                               .verify_document_status_ca(CAConstants.DOCUMENT_STATUS_CA)
        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self


