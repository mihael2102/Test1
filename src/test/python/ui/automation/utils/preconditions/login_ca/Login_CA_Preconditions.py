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


class LoginCAPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def check_email_sign_up(self):
        sleep(10)
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user(Config.email_address)
        pop_conn.pass_(Config.email_password)
        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = ["\n".join(m.decode() for m in mssg[1]) for mssg in messages]
        # Parse message into an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        # Settings for brand name in subjects:
        if global_var.current_brand_name == "tradenero":
            brand = EmailConstants.SUBJECT_WELCOME_TRADE_NERO
        else:
            brand = global_var.current_brand_name
        subjects = []
        for message in messages:
            if CRMConstants.WELCOME_TO in str(message['Subject']):
                subjects.append(str(message['Subject']).lower())
                Logging().reportDebugStep(self, str(message['Subject']).lower())
        found_subject = ""
        for x in subjects:
            if brand in x:
                found_subject = x

        assert brand in found_subject
        Logging().reportDebugStep(self, 'Mail is found: ' + found_subject)
        pop_conn.quit()

    def sign_up_ca(self):
        """ Registration form """
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .close_campaign_banner()\
            .click_sign_up()\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                                         [LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)
                                        [LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(CAConstants.EMAIL_CA)\
            .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE])\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()\
            .risk_check_box_accept()\
            .select_country_first_step(CAConstants.COUNTRY1)\
            .click_submit()\
            .close_payment_popup()

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
            CALoginPage(self.driver)\
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
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver)\
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

    def client_exist_in_crm_new_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CAConstants.EMAIL_CA)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Get client's data """
        details = ClientDetailsPageUI(self.driver)

        first_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_LNAME)
        phone = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_PHONE)
        birthday = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BIRTHDAY)
        address = details \
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)
        postal_code = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CODE)
        city = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CITY)
        country = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
        currency = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BASE_CURRENCY)

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
                first_name,
                self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]) \
            .comparator_string(
                last_name,
                self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_LAST_NAME]) \
            .comparator_string(birthday, CAConstants.BIRTHDAY_CRM) \
            .comparator_string(currency, CAConstants.CURRENCY) \
            .comparator_string(address, CAConstants.ADDRESS) \
            .comparator_string(postal_code, CAConstants.ZIP_CODE) \
            .comparator_string(city, CAConstants.CITY) \
            .comparator_string(country, CAConstants.COUNTRY_DEFAULT)

        if "*" not in phone:
            assert self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.PHONE] in phone

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
