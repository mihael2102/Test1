import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.credit_in.MT4CreditInModule import MT4CreditInModule
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants


class CreditInPrecondition(object):

    def __init__(self, driver, config) -> None:
        self.driver = driver
        self.config = config

    def add_live_account(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        CaManageAccounts().open_new_account_button() \
                          .select_account_currency(
                    Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
                          .create_account_button()

        return CreditInPrecondition(self.driver)

    def add_live_account_in_crm(self):
        CRMHomePage(self.driver)\
            .open_client_module()
        ClientsPage(self.driver)\
            .select_filter(self.config.get_data_client(
                                        TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))\
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                              TestDataConstants.E_MAIL))\
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "newforexstaging"):
            crm_client_profile = MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200))

        elif global_var.current_brand_name == "q8":
            crm_client_profile = MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_PLATFORMS, TestDataConstants.TRADING_PLATFORM_MT4),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200))

        elif global_var.current_brand_name == "axa_markets":
            crm_client_profile = MT4CreateAccountModule(self.driver)\
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_400))

        elif global_var.current_brand_name == "trade99":
            crm_client_profile = MT4CreateAccountModule(self.driver)\
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                MT4ModuleConstants.CURRENCY_BTC,
                MT4ModuleConstants.GROUP_REAL,
                MT4ModuleConstants.LEVERAGE_100)

        elif (global_var.current_brand_name == "gxfx") \
                or (global_var.current_brand_name == "dax-300") \
                or (global_var.current_brand_name == "kontofx") \
                or (global_var.current_brand_name == "uprofx"):
            crm_client_profile = MT4CreateAccountModule(self.driver)\
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_EUR),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_EUR),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE_1_200))

        else:
            crm_client_profile = MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE))

        return crm_client_profile

    def make_credit_in(self):
        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        if global_var.current_brand_name == "trade99":
            crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.CREDIT_IN2)
        else:
            crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.CREDIT_IN)

        MT4CreditInModule().make_credit_in(account_number, CRMConstants.AMOUNT_CREDIT_IN,
                                           CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE),
                                           CRMConstants.CREDIT_IN_COMMENT) \
            .click_ok() \
            .refresh_page()
        return CreditInPrecondition(self.driver)
