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
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
from src.main.python.ui.ca.model.pages.login.CAPage import CAPage
from time import sleep
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage



class TradingAccountPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def add_live_account(self):
        if global_var.current_brand_name != "q8":
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME])
            CAPage(self.driver).open_manage_accounts() \
                               .open_new_account_btn() \
                               .select_account_type(CAConstants.ACCOUNT_LIVE)

            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).select_currency(CAConstants.CURRENCY_CRYPTO)
            else:
                CAPage(self.driver).select_currency(CAConstants.CURRENCY)

            if (global_var.current_brand_name == "swiftcfd") or (global_var.current_brand_name == "jonesmutual")\
                    or (global_var.current_brand_name == "royal_cfds"):
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL2)
            else:
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL)

            CAPage(self.driver).click_create_account() \
                               .additional_account_created() \
                               .open_live_section() \
                               .get_live_account_number()
        else:
            return self

    def add_demo_account(self):
        if global_var.current_brand_name != "q8":
            CALoginPage(self.driver).open_first_tab_page(self.config.get_value('url_ca')) \
                                    .login() \
                                    .enter_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                 LeadsModuleConstants.EMAIL]) \
                                    .enter_password(CAConstants.PASSWORD) \
                                    .click_login() \
                                    .verify() \
                                    .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME])
            CAPage(self.driver).open_manage_accounts() \
                               .open_demo_section() \
                               .open_new_account_btn() \
                               .select_account_type(CAConstants.ACCOUNT_DEMO)

            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).select_currency(CAConstants.CURRENCY_CRYPTO)
            else:
                CAPage(self.driver).select_currency(CAConstants.CURRENCY)

            if (global_var.current_brand_name == "swiftcfd") or (global_var.current_brand_name == "jonesmutual")\
                    or (global_var.current_brand_name == "royal_cfds"):
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL2)
            else:
                CAPage(self.driver).select_leverage_level(CAConstants.LEVERAGE_LEVEL)

            CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT0) \
                               .verify_init_deposit_error() \
                               .set_initial_deposit(CAConstants.INITIAL_DEPOSIT1) \
                               .verify_init_deposit_error()
            if global_var.current_brand_name == "mpcrypto":
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT_BTC)
            else:
                CAPage(self.driver).set_initial_deposit(CAConstants.INITIAL_DEPOSIT)
            CAPage(self.driver).click_create_account() \
                               .verify_demo_account_created() \
                               .open_demo_section()
            if (global_var.current_brand_name == "swiftcfd") or (global_var.current_brand_name == "jonesmutual") \
                    or (global_var.current_brand_name == "royal_cfds"):
                actual_leverage = CAPage(self.driver).get_leverage()
                expected_leverage = CAConstants.LEVERAGE_LEVEL2
                assert actual_leverage == expected_leverage
            else:
                actual_leverage = CAPage(self.driver).get_leverage()
                lev = CAConstants.LEVERAGE_LEVEL
                leverage = lev.split(':')
                expected_leverage = leverage[1]
                print(expected_leverage, actual_leverage)
                assert actual_leverage == expected_leverage

            if global_var.current_brand_name == "mpcrypto":
                actual_currency = CAPage(self.driver).get_currency()
                expected_currency = CAConstants.CURRENCY_CRYPTO
                assert actual_currency == expected_currency
            else:
                actual_currency = CAPage(self.driver).get_currency()
                expected_currency = CAConstants.CURRENCY
                assert actual_currency == expected_currency

            CAPage(self.driver).get_demo_account_number()
        else:
            return self

    def verify_account_in_crm(self):
        # Login to CRM
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                            LeadsModuleConstants.EMAIL])
        sleep(2)
        ClientProfilePage(self.driver).open_trading_accounts_tab()
        ClientsPage(self.driver).trading_account_exist(CAConstants.DEMO_ACCOUNT_NUMBER)
        ClientsPage(self.driver).trading_account_exist(CAConstants.LIVE_ACCOUNT_NUMBER)




            # BrandHomePage().open_first_tab_page(self.config.get_value('url_ca')).login() \
        #     .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
        #                 Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
        #     .click_login_button() \
        #     .open_drop_down_menu() \
        #     .select_module(CaConstants.MANAGE_ACCOUNTS)
        #
        # CaManageAccounts().open_new_account_button() \
        #     .select_account_currency(
        #     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
        #     .create_account_button()
        # return TradingAccountPrecondition()

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

        elif (global_var.current_brand_name == "axa_markets"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE_400))
            return self

        elif (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "safemarkets"):
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_EUR),
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
        if global_var.current_brand_name == "axa_markets":
            MT4CreateAccountModule(self.driver).update_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO_GROUP),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO_LEVERAGE_400))

        else:
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
