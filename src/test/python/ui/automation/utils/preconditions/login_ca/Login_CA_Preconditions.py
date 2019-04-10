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
import poplib
from email import parser
from src.main.python.utils.logs.Loging import Logging

class Login_CA_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def check_email_sign_up(self):
        sleep(60)
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user('jonathan.albalak@pandats.com')
        pop_conn.pass_('9U&AU=bm')
        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = ["\n".join(m.decode() for m in mssg[1]) for mssg in messages]
        # Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            if CRMConstants.WELCOME_TO in str(message['Subject']):
                link = self.config.get_value('url').replace('https://', '')
                link1 = link.replace('.ptscrm.com/', '')
                if link1 in str(message['Subject']).lower().replace(' ', ''):
                    Logging().reportDebugStep(self, str(message['Subject']))
                    assert CRMConstants.WELCOME_TO in str(message['Subject'])
                    # return str(message['Subject'])
        pop_conn.quit()




    def sign_up_ca(self):
###REGISTRATION FORM
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))\
                                .click_sign_up()
        if (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "b-finance") \
                or (global_var.current_brand_name == "eafx"):
                CALoginPage(self.driver).click_regulatory_confirmation()
        CALoginPage(self.driver).fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME])\
                                .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_LAST_NAME])\
                                .fill_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.EMAIL])\
                                .fill_phone(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.PHONE])\
                                .fill_password(CAConstants.PASSWORD)
        if global_var.current_brand_name != "q8":
                CALoginPage(self.driver).fill_confirm_password(CAConstants.PASSWORD)\
                                .check_box_accept()
        if global_var.current_brand_name == "goldenmarkets":
                CALoginPage(self.driver).click_customer_policy()
        CALoginPage(self.driver).click_submit() \

###PERSONAL DETAILS FORM
        if global_var.current_brand_name == "q8":

            CALoginPage(self.driver).click_my_account() \
                .logout() \
                .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                 LeadsModuleConstants.EMAIL]) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .click_my_account() \
                .account_details()

        elif global_var.current_brand_name == "firstindex":

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

        # elif global_var.current_brand_name == "ptbanc":
        #
        #     CALoginPage(self.driver).verify() \
        #         .click_hi_guest() \
        #         .click_transactions_history() \
        #         .select_pt_b()\
        #         .fill_city(CAConstants.CITY) \
        #         .fill_zip_code(CAConstants.ZIP_CODE) \
        #         .fill_address(CAConstants.ADDRESS) \
        #         .click_next() \
        #         .verify() \
        #         .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                            LeadsModuleConstants.FIRST_NAME]) \
        #         .sign_out() \
        #         .login() \
        #         .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                          LeadsModuleConstants.EMAIL]) \
        #         .enter_password(CAConstants.PASSWORD) \
        #         .click_login() \
        #         .verify()
        #     assert CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
        #                                                       LeadsModuleConstants.FIRST_NAME]) == \
        #            self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

        elif global_var.current_brand_name == "jonesmutual":

            CALoginPage(self.driver).verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(CAConstants.CURRENCY) \
                .choose_citizenship(CAConstants.CITIZENSHIP2) \
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
            sleep(2)
            existing_client = CALoginPage(self.driver).verify_client(
                self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                    LeadsModuleConstants.FIRST_NAME])
            expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
            print(expected_client, existing_client)
            assert existing_client == expected_client

        elif (global_var.current_brand_name == "xtraderfx")or(global_var.current_brand_name == "solocapitals") \
                or (global_var.current_brand_name == "b-finance"):

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
            sleep(2)
            existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                                 LeadsModuleConstants.FIRST_NAME])
            expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
            expected_client.upper()
            print(expected_client, existing_client)
            assert existing_client == expected_client.upper()

        elif global_var.current_brand_name == "mpcrypto":

            CALoginPage(self.driver).verify() \
                .click_hi_guest() \
                .click_transactions_history() \
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH) \
                .choose_currency(CAConstants.CURRENCY_CRYPTO) \
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
            sleep(2)
            existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                                 LeadsModuleConstants.FIRST_NAME])
            expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

            print(expected_client, existing_client)
            assert existing_client == expected_client

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
            sleep(2)
            existing_client = CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                              LeadsModuleConstants.FIRST_NAME])
            expected_client = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]

            assert existing_client == expected_client

    def client_exist_in_crm(self):
        #Login to CRM
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
        assert ClientsPage(self.driver).get_client_first_name() == self.load_lead_from_config(
                                                                TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
        assert ClientsPage(self.driver).get_client_last_name() == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                                LeadsModuleConstants.FIRST_LAST_NAME]
        if (global_var.current_brand_name != "newrichmarkets") and (global_var.current_brand_name != "brokerz") \
                and (global_var.current_brand_name != "tradospot"):
                assert ClientsPage(self.driver).get_client_phone() == '+49 7777 777'

        if global_var.current_brand_name != "q8":
            assert ClientsPage(self.driver).get_client_address() == CAConstants.ADDRESS
            assert ClientsPage(self.driver).get_client_city() == CAConstants.CITY
            assert ClientsPage(self.driver).get_client_code() == CAConstants.ZIP_CODE
            assert ClientsPage(self.driver).get_client_date_of_birth() == '1995-01-10'
        assert ClientsPage(self.driver).get_client_country() == 'Germany'
        if global_var.current_brand_name == "mpcrypto":
            assert ClientsPage(self.driver).get_client_currency() == CAConstants.CURRENCY_CRYPTO
        else:
            assert ClientsPage(self.driver).get_client_currency() == CAConstants.CURRENCY











