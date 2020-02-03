from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.pages.ca.CAMainMenuPage import CAMainMenuPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
from src.main.python.ui.ca.model.constants.CAconstants.AccountConstants import AccountConstants


class GraphPreconditionCA(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_graph_ca(self):

        if global_var.current_brand_name == "q8":
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca_2'))
        else:
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca'))
        CALoginPage(self.driver) \
            .close_campaign_banner() \
            .click_sign_in_btn() \
            .enter_email(self.config.get_value('email_live_acc')) \
            .enter_password(self.config.get_value('password_live_acc')) \
            .click_login() \
            .verify() \
            .verify_client(AccountConstants.CLIENT)

        WebTraderPage(self.driver) \
            .open_trading_page() \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_5MIN) \
            .check_chart_loaded()\
            .open_graph_tab(TradingConstants.GRAPH_TAB_15MIN) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_30MIN) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_HOURLY) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_4HOURS) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_DAILY) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_WEEKLY) \
            .check_chart_loaded() \
            .open_graph_tab(TradingConstants.GRAPH_TAB_MONTHLY) \
            .check_chart_loaded()
