from src.main.python.ui.ca.model.pages.ca.QuestionnairePage import QuestionnairePage
from src.main.python.ui.ca.model.constants.questionnaire.QuesStrattonConstants import QuesStrattonConstants
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
from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.ca.model.constants.questionnaire.QuesDualixConstants import QuesDualixConstants
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.ca.model.pages.sign_up.SignUpFirstStepPage import SignUpFirstStepPage
from src.main.python.ui.ca.model.constants.sign_up.SignUpFirstStepConstants import SignUpFirstStepConstants


class LoginCAPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sign_up_ca(self):
        """ Registration form """
        SignUpFirstStepPage(self.driver) \
            .first_step_sign_up(
                url=self.config.get_value('url_ca'),
                field1=SignUpFirstStepConstants.FIELD_FNAME,
                first_name=self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME],
                field2=SignUpFirstStepConstants.FIELD_LNAME,
                last_name=self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_LAST_NAME])

        """ Check graphs """
        WebTraderPage(self.driver) \
            .open_trading_page() \
            .check_chart_loaded()

        """ Personal details form """
        if global_var.current_brand_name == "trade99" or \
                global_var.current_brand_name == "libramarkets" or \
                global_var.current_brand_name == "uprofx" or \
                global_var.current_brand_name == "kontofx" or \
                global_var.current_brand_name == "olympiamarkets" or \
                global_var.current_brand_name == "grandefex" or \
                global_var.current_brand_name == "analystq":

            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca'))
            CALoginPage(self.driver) \
                .verify() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                   LeadsModuleConstants.FIRST_NAME]) \
                .click_transactions_history() \
                .open_account_details_tab() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_citizenship(CAConstants.CITIZENSHIP) \
                .fill_city(CAConstants.CITY) \
                .fill_zip_code(CAConstants.ZIP_CODE) \
                .fill_address(CAConstants.ADDRESS) \
                .click_save_changes() \
                .verify() \
                .close_client_area() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                   LeadsModuleConstants.FIRST_NAME]) \
                .sign_out() \
                .login() \
                .enter_email(CAConstants.EMAIL_CA) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify()
        else:
            CALoginPage(self.driver) \
                .verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(var.get_var(self.__class__.__name__)["signup_currency"]) \
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
                .enter_email(CAConstants.EMAIL_CA) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify()
            sleep(2)
            existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                                         LeadsModuleConstants.FIRST_NAME])
            expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
            expected_client.upper()
            print(expected_client, existing_client)
            assert existing_client.lower() == expected_client.lower()

    def client_exist_in_crm(self):
        """ Login to CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver) \
            .find_client_by_email(CAConstants.EMAIL_CA)
        sleep(2)
        assert ClientsPage(self.driver).get_client_first_name() == self.load_lead_from_config(
            TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
        assert ClientsPage(self.driver).get_client_last_name() == self.load_lead_from_config(
            TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_LAST_NAME]
        actual_phone = ClientsPage(self.driver).get_client_phone()
        actual_phone = actual_phone.replace(' ', '')
        expected_phone = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE]
        if (global_var.current_brand_name != "newrichmarkets") \
                and (global_var.current_brand_name != "brokerz") \
                and (global_var.current_brand_name != "kontofx") \
                and (global_var.current_brand_name != "q8") \
                and (global_var.current_brand_name != "gigafx") \
                and (global_var.current_brand_name != "trade99") \
                and (global_var.current_brand_name != "tradenero"):
            if '*' not in actual_phone:
                assert expected_phone in actual_phone

        if global_var.current_brand_name != "q8":
            assert ClientsPage(self.driver).get_client_address() == CAConstants.ADDRESS
            assert ClientsPage(self.driver).get_client_city() == CAConstants.CITY
            assert ClientsPage(self.driver).get_client_code() == CAConstants.ZIP_CODE
            assert ClientsPage(self.driver).get_client_date_of_birth() == '1995-01-10'
        if global_var.current_brand_name == "q8":
            ClientsPage(self.driver).open_address_information_tab()
        assert ClientsPage(self.driver).get_client_country() == 'Germany'
        if global_var.current_brand_name == "mpcrypto" or global_var.current_brand_name == "trade99":
            assert ClientsPage(self.driver).get_client_currency() == CAConstants.CURRENCY_CRYPTO
        else:
            assert ClientsPage(self.driver).get_client_currency() == CAConstants.CURRENCY

    def login_ca(self):
        try:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .close_campaign_banner() \
                .close_notifications_banner() \
                .select_english() \
                .click_sign_in_btn() \
                .enter_email(self.config.get_value('email_live_acc')) \
                .enter_password(self.config.get_value('password_live_acc')) \
                .click_login() \
                .verify() \
                .verify_client(var.get_var(self.__class__.__name__)["client_name"])
        except:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .close_campaign_banner() \
                .close_notifications_banner() \
                .select_english() \
                .click_sign_in_btn() \
                .enter_email(self.config.get_value('email_live_acc')) \
                .enter_password(self.config.get_value('password_live_acc')) \
                .click_login() \
                .verify() \
                .verify_client(var.get_var(self.__class__.__name__)["client_name"])
