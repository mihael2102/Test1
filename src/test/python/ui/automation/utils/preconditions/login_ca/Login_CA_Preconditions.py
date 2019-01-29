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
from time import sleep

class Login_CA_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_ca(self):
###REGISTRACTIONS FORM
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))\
                                .click_sign_up()\
                                .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
                                .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
                                .fill_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])\
                                .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.PHONE])\
                                .fill_password(CAConstants.PASSWORD)
        if global_var.current_brand_name != "q8trade_ca":
                CALoginPage(self.driver).fill_confirm_password(CAConstants.PASSWORD)\
                                .check_box_accept()\

        CALoginPage(self.driver).click_submit() \

###PERSONAL DETAILS FORM
        if global_var.current_brand_name == "q8trade_ca":

            CALoginPage(self.driver).click_my_account() \
                .logout() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .click_my_account() \
                .account_details()

        elif global_var.current_brand_name == "firstindex_ca":

            CALoginPage(self.driver).verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(CAConstants.CURRENCY) \
                .choose_citizenship(CAConstants.CITIZENSHIP) \
                .fill_city(CAConstants.CITY) \
                .fill_zip_code(CAConstants.ZIP_CODE) \
                .fill_address(CAConstants.ADDRESS) \
                .account_type(CAConstants.ACCOUNT_TYPE)\
                .click_next() \
                .verify() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                   LeadsModuleConstants.FIRST_NAME]) \
                .sign_out() \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify()
            assert CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.FIRST_NAME]) == \
                   self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

        elif global_var.current_brand_name == "ptbanc_ca":

            CALoginPage(self.driver).verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_pt_b()\
                .fill_city(CAConstants.CITY) \
                .fill_zip_code(CAConstants.ZIP_CODE) \
                .fill_address(CAConstants.ADDRESS) \
                .click_next() \
                .verify() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                   LeadsModuleConstants.FIRST_NAME]) \
                .sign_out() \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify()
            assert CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.FIRST_NAME]) == \
                   self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
        else:

            CALoginPage(self.driver).verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(CAConstants.CURRENCY) \
                .choose_citizenship(CAConstants.CITIZENSHIP) \
                .fill_city(CAConstants.CITY) \
                .fill_zip_code(CAConstants.ZIP_CODE) \
                .fill_address(CAConstants.ADDRESS) \
                .click_next() \
                .verify() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                   LeadsModuleConstants.FIRST_NAME]) \
                .sign_out() \
                .login() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify()
            assert CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.FIRST_NAME]) == \
                   self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

    def client_exist_in_crm(self):
        """ Login to CRM """
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url_crm')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])











