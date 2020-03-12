import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.ca.CADepositPage import CADepositPage


class DepositCAPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def client_deposit_page_loading(self):
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .close_campaign_banner() \
            .close_notifications_banner() \
            .click_sign_in_btn() \
            .enter_email(self.config.get_value('email_live_acc')) \
            .enter_password(self.config.get_value('password_live_acc')) \
            .click_login() \
            .verify() \
            .verify_client(var.get_var(self.__class__.__name__)["client_name"])
        CADepositPage(self.driver) \
            .click_deposit_btn() \
            .select_payment_method() \
            .check_deposit_page_loaded()
