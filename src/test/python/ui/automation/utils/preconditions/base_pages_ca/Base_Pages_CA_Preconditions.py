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
from src.main.python.ui.ca.model.pages.ca.CAMainMenuPage import CAMainMenuPage


class BasePagesCAPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def main_menu_pages_loading(self):
        CALoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .login() \
            .enter_email(CAConstants.EMAIL_CA) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login() \
            .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                               LeadsModuleConstants.FIRST_NAME]) \
            .click_transactions_history()
        CAMainMenuPage(self.driver)\
            .check_transaction_history_loaded()\
            .open_account_details_tab()\
            .check_account_details_loaded()\
            .open_verification_center_tab()\
            .check_verification_center_loaded()\
            .open_service_desk_tab()\
            .check_service_desk_loaded()\
            .open_withdraw_tab()\
            .check_withdraw_loaded()\
            .open_manage_accounts_tab()\
            .check_manage_accounts_loaded()
