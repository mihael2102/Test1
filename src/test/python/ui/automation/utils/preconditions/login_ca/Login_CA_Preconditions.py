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
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
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
        pop_conn.pass_('xUQ7hrr9VF')
        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = ["\n".join(m.decode() for m in mssg[1]) for mssg in messages]
        # Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            if CRMConstants.WELCOME_TO in str(message['Subject']):
                link = self.config.get_value('url').replace('https://', '')
                link1 = link.replace('.ptscrm.com/','')
                if link1 in str(message['Subject']).lower():
                    Logging().reportDebugStep(self, str(message['Subject']))
                    assert CRMConstants.WELCOME_TO in str(message['Subject'])
                    # return str(message['Subject'])
        pop_conn.quit()

    def client_exist_in_crm(self):
        # Login to CRM:
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.EMAIL])
        sleep(2)
        assert ClientsPage(self.driver).get_client_first_name() == self.load_lead_from_config(
            TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME]
        assert ClientsPage(self.driver).get_client_last_name() == \
               self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                   LeadsModuleConstants.FIRST_LAST_NAME]
        # if global_var.current_brand_name != "stoxmarket":
        #     assert "245" in ClientsPage(self.driver).get_client_phone()
        # assert ClientsPage(self.driver).get_client_address() == CAConstants.ADDRESS
        # assert ClientsPage(self.driver).get_client_city() == CAConstants.CITY
        # assert ClientsPage(self.driver).get_client_code() == CAConstants.ZIP_CODE
        # assert ClientsPage(self.driver).get_client_country() == 'Germany'
        # assert ClientsPage(self.driver).get_client_date_of_birth() == '1995-01-10'
        # assert ClientsPage(self.driver).get_client_currency() == CAConstants.CURRENCY

    def sign_up_ca(self):
        # Registration Form
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca'))\
            .click_sign_up()

        if global_var.current_brand_name == "itrader_global":
            CALoginPage(self.driver).select_country(CAConstants.CITIZENSHIP_AUS)
        elif global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).select_country(CAConstants.CITIZENSHIP_SOUTH_A)
        else:
            CALoginPage(self.driver).select_country(CAConstants.CITIZENSHIP)

        CALoginPage(self.driver)\
            .fill_first_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])\
            .fill_last_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                    LeadsModuleConstants.FIRST_LAST_NAME])\
            .fill_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.EMAIL])\
            .fill_area_code(CAConstants.AREA_CODE)\
            .fill_phone(CAConstants.PHONE)\
            .fill_password(CAConstants.PASSWORD)\
            .fill_confirm_password(CAConstants.PASSWORD)\
            .check_box_accept()

        if global_var.current_brand_name == "triomarkets" or global_var.current_brand_name == "kaya_fx" or \
                global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).check_box_accept_new()

        CALoginPage(self.driver).click_submit()

        if global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).close_welcome_message()

        if global_var.current_brand_name == "finmarket":
            CALoginPage(self.driver).enter_data_birth(CAConstants.DATA_MONTH_YEAR)

        else:
            CALoginPage(self.driver)\
                .select_data_birth_day(CAConstants.DAY_BIRTH) \
                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                .select_data_birth_year(CAConstants.YEAR_BIRTH)

        if global_var.current_brand_name != "itrader_global" and global_var.current_brand_name != "oinvestsa" and \
                global_var.current_brand_name != "finmarket":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY)
        if global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY_USD)

        CALoginPage(self.driver).fill_city(CAConstants.CITY) \
                                .fill_zip_code(CAConstants.ZIP_CODE) \
                                .fill_address(CAConstants.ADDRESS)

        if global_var.current_brand_name == "finmarket":
            CALoginPage(self.driver).click_submit()

        CALoginPage(self.driver).sign_out()

        if global_var.current_brand_name == "oinvestsa":
             CALoginPage(self.driver).open_first_tab_page\
                 ("https://my.oinvest.co.za/Login/tabid/115/language/en-US/Default.aspx?returnurl=%2f")

        if global_var.current_brand_name == "gmo":
            CALoginPage(self.driver).open_first_tab_page("https://my.gmotrading.com/en-us/login.aspx") \


        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                     LeadsModuleConstants.EMAIL]) \
                                .enter_password(CAConstants.PASSWORD) \
                                .click_login()

        assert CALoginPage(self.driver).verify_client(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.FIRST_NAME]).upper() == \
                                                      self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                          LeadsModuleConstants.FIRST_NAME].upper() + " DOE"
