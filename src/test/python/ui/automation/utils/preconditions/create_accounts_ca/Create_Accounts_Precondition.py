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
from src.main.python.ui.ca.model.pages.ca.CAPage import CAPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from time import sleep

class Create_Accounts_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def create_live_account(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()
        CAPage(self.driver).open_live_account()
        if global_var.current_brand_name == "finmarket":
            CALoginPage(self.driver).enter_data_birth(CAConstants.DATA_MONTH_YEAR)

        else:
            CALoginPage(self.driver).select_data_birth_day(CAConstants.DAY_BIRTH) \
                                .select_data_birth_month(CAConstants.MONTH_BIRTH) \
                                .select_data_birth_year(CAConstants.YEAR_BIRTH)

        if global_var.current_brand_name != "itrader_global" and global_var.current_brand_name != "oinvestsa" and global_var.current_brand_name != "finmarket":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY)
        if global_var.current_brand_name == "oinvestsa":
            CALoginPage(self.driver).choose_currency(CAConstants.CURRENCY_USD)


        CALoginPage(self.driver).fill_city(CAConstants.CITY) \
                            .fill_zip_code(CAConstants.ZIP_CODE) \
                            .fill_address(CAConstants.ADDRESS)

        CALoginPage(self.driver).click_next_open_live_account()
        CALoginPage(self.driver).my_account_link()
        CAPage(self.driver).click_check_box_confirm()
        CAPage(self.driver).click_confirm()
        currency = CAPage(self.driver).verify_relevant_currency()
        assert currency == CAConstants.CURRENCY
        data = CAPage(self.driver).verify_correct_data()

        assert data == CAConstants.LEVERAGE


    def create_demo_account(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()

        CAPage(self.driver).open_demo_account()
        CAPage(self.driver).select_currency()
        CAPage(self.driver).select_leverage()
        CAPage(self.driver).select_deposit()
        CAPage(self.driver).click_submit()
        CAPage(self.driver).finish_button()

