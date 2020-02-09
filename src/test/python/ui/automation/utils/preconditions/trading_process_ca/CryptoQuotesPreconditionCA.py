import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.login.WebTraderPage import WebTraderPage
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants
from src.main.python.ui.ca.model.constants.CAvariables.TradingVariablesCA import TradingVariablesCA


class CryptoQuotesPreconditionCA(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_crypto_quotes_ca(self):

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
            .close_payment_popup()

        if global_var.current_brand_name == "q8":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@class='platform__mobile-platform']"))
        elif global_var.current_brand_name == "24option":
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(
                "//iframe[@id='swPandaIframe']"))

        WebTraderPage(self.driver) \
            .open_trading_page()
        if global_var.current_brand_name == "dualix" or \
           global_var.current_brand_name == "strattonmarkets-eu":
            WebTraderPage(self.driver) \
                .perform_scroll_down()
        if global_var.current_brand_name == "24option":
            asset = "BitcoinEUR"
        else:
            asset = TradingConstants.ASSET_BTCEUR
        WebTraderPage(self.driver) \
            .open_asset_group(TradingConstants.ASSET_GROUP_CRYPTO) \
            .verify_asset_price_change(asset)
