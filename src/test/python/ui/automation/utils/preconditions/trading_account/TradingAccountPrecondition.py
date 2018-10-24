from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class TradingAccountPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
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
        return TradingAccountPrecondition()

    def add_demo_account_from_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if (global_var.current_brand_name == "royal_cfds"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_1_200))
            return self

        elif (global_var.current_brand_name == "q8"):
            MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT4),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif (global_var.current_brand_name == "mpcrypto"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_BCH),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        else:
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

    def add_live_account_from_crm(self):
        # crm_client_profile = CRMLoginPage(self.driver) \
        #     .open_first_tab_page(self.config.get_value('url')) \
        #     .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
        #                self.config.get_value(TestDataConstants.CRM_PASSWORD),
        #                self.config.get_value(TestDataConstants.OTP_SECRET)) \
        #     .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
        #     .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
        #
        # crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        #
        # MT4CreateAccountModule(self.driver)\
        #     .create_account(
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
        #     self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE))
        # return self

        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if (global_var.current_brand_name == "royal_cfds"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_1_200))
            return self

        elif (global_var.current_brand_name == "q8"):
            MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT4),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif (global_var.current_brand_name == "mpcrypto"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_BCH),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        else:
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

    def update_demo_account_from_crm(self):
        ClientProfilePage(self.driver).open_mt4_actions(CRMConstants.UPDATE_MT4_USER)
        from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
        MT4CreateAccountModule(self.driver).update_account(
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED, TestDataConstants.TRADING_ACCOUNT_DEMO),
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED, TestDataConstants.TRADING_ACCOUNT_DEMO_GROUP),
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED, TestDataConstants.TRADING_ACCOUNT_DEMO_LEVERAGE))
        return self

    def make_deposit(self):
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

        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)

        MT4DepositModule().make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                        CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                        CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT) \
            .click_ok() \
            .refresh_page()

        crm_client_profile.click_trading_accounts_tab() \
            .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
        return TradingAccountPrecondition()
