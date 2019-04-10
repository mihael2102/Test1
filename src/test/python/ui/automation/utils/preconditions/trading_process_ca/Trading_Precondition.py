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
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.help_desk.HelpDeskEditPage import HelpDeskEditPage
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage


class Trading_Precondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config


    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead


    def trade_with_insufficient_funds(self):
        CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver).enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
            .enter_password(CAConstants.PASSWORD) \
            .click_login()
        ca_balance = CAPage(self.driver).get_balance()
        CAPage(self.driver).click_actions_launch()
        avaliable_funds_int = WebTraderPage(self.driver).get_avaliable_funds()
        avaliable_funds_int1 = avaliable_funds_int.replace('.','')
        assert ca_balance.replace('.','') in avaliable_funds_int1.replace(',', '')
        avaliable_funds = WebTraderPage(self.driver).check_avaliable_funds()
        used_funds = WebTraderPage(self.driver).check_used_funds()
        account_value = WebTraderPage(self.driver).check_account_value()
        total_p_l = WebTraderPage(self.driver).check_total_p_l()
        margin_level = WebTraderPage(self.driver).check_margin_level()
        assert avaliable_funds == CAConstants.AVALIABLE_FUNDS
        assert used_funds == CAConstants.USED_FUNDS
        assert account_value == CAConstants.ACCOUNT_VALUE
        assert total_p_l == CAConstants.TOTAL_P_L
        assert margin_level == CAConstants.MARGIN_LVL



