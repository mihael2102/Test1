from src.main.python.ui.ca.model.pages.ca.QuestionnairePage import QuestionnairePage
from src.main.python.ui.ca.model.constants.CAconstants.QuestionnaireConstants import QuestionnaireConstants
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
        if global_var.current_brand_name == "q8":
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca_2'))\
                .close_campaign_banner()\
                .click_sign_in_btn()\
                .enter_email(self.config.get_value('email_live_acc'))\
                .enter_password(self.config.get_value('password_live_acc'))\
                .click_login()\
                .verify()\
                .verify_client("my account")
            CADepositPage(self.driver)\
                .click_deposit_btn()\
                .check_deposit_page_loaded()
        elif global_var.current_brand_name == "24option":
            try:
                CALoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url_ca')) \
                    .close_campaign_banner() \
                    .close_notifications_banner()\
                    .click_sign_in_btn() \
                    .enter_email(self.config.get_value('email_live_acc')) \
                    .enter_password(self.config.get_value('password_live_acc')) \
                    .click_login() \
                    .verify() \
                    .verify_client("Welcome")
                CADepositPage(self.driver) \
                    .click_deposit_btn() \
                    .check_deposit_page_loaded()
            except:
                CALoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url_ca')) \
                    .close_campaign_banner() \
                    .close_notifications_banner() \
                    .click_sign_in_btn() \
                    .enter_email(self.config.get_value('email_live_acc')) \
                    .enter_password(self.config.get_value('password_live_acc')) \
                    .click_login() \
                    .verify() \
                    .verify_client("Welcome")
                CADepositPage(self.driver) \
                    .click_deposit_btn() \
                    .check_deposit_page_loaded()
        else:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .close_campaign_banner() \
                .click_sign_in_btn() \
                .enter_email(self.config.get_value('email_live_acc')) \
                .enter_password(self.config.get_value('password_live_acc')) \
                .click_login() \
                .verify() \
                .verify_client("Test")
            CADepositPage(self.driver)\
                .click_deposit_btn() \
                .select_payment_method() \
                .check_deposit_page_loaded()
