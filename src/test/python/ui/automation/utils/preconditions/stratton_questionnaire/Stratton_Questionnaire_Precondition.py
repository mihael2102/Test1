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
from time import sleep
import poplib
from email import parser
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


class StrattonQuestionnairePrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def customer_classification_empty(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .click_sign_up()\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.EMAIL])\
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.PHONE])\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()\
            .click_submit()\
            .verify()

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))\
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET)) \
                                 .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                            TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()
        assert customer_classification.strip() == CRMConstants.CUSTOMER_CLASSIFICATION_EMPTY

    def customer_classification_blocked(self):
        assert global_var.current_brand_name == "strattonmarkets-eu"
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .click_sign_up()\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.EMAIL])\
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.PHONE])\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()\
            .click_submit()\
            .verify()\
            .click_hi_guest() \
            .click_transactions_history() \
            .select_data_birth_day(CAConstants.DAY_BIRTH) \
            .select_data_birth_month(CAConstants.MONTH_BIRTH) \
            .select_data_birth_year(CAConstants.YEAR_BIRTH) \
            .choose_currency(CAConstants.CURRENCY) \
            .choose_citizenship(CAConstants.CITIZENSHIP3) \
            .fill_city(CAConstants.CITY) \
            .fill_zip_code(CAConstants.ZIP_CODE) \
            .fill_address(CAConstants.ADDRESS) \
            .click_next()\
            .select_us_reportable(CAConstants.US_REPORTABLE_YES)\
            .confirm_us_reportable() \
            .came_back_on_previous_page() \
            .login() \
            .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()\
            .verify_registration_blocked()

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        customer_classification = ClientProfilePage(self.driver).get_customer_classification()

        assert customer_classification.strip() == CRMConstants.CUSTOMER_CLASSIFICATION_BLOCKED

        # Check MT Actions contain only 9 items (there is no Create MT User)
        ClientProfilePage(self.driver).wait_element_to_be_disappear("//div[@id='mt4_act_box']/a[10]")
