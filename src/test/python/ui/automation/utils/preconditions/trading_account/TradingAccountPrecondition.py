import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var
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
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI


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
        """ Log in CA """
        if global_var.current_brand_name == "q8" or \
           global_var.current_brand_name == "strattonmarkets-eu":
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .not_runned_test()
        else:
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .login() \
                .enter_email(CAConstants.EMAIL_CA) \
                .enter_password(CAConstants.PASSWORD) \
                .click_login() \
                .verify() \
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                    LeadsModuleConstants.FIRST_NAME])

            """ Create LIVE account """
            CAPage(self.driver)\
                .open_manage_accounts() \
                .open_new_account_btn() \
                .select_account_type(CAConstants.ACCOUNT_LIVE) \
                .select_currency(var.get_var(self.__class__.__name__)["live_acc_currency"]) \
                .select_leverage_level(var.get_var(self.__class__.__name__)["live_acc_leverage"]) \
                .click_create_account()\
                .get_create_account_message()\
                .additional_account_created()\
                .open_live_section()\
                .get_live_account_number()

    def add_demo_account(self):
        """ Log in CA """
        if global_var.current_brand_name == "q8" or \
           global_var.current_brand_name == "strattonmarkets-eu":
            CALoginPage(self.driver) \
                .open_first_tab_page(self.config.get_value('url_ca')) \
                .not_runned_test()
        else:
            CALoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url_ca'))\
                .login()\
                .enter_email(CAConstants.EMAIL_CA)\
                .enter_password(CAConstants.PASSWORD)\
                .click_login()\
                .verify()\
                .click_hi_user(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                LeadsModuleConstants.FIRST_NAME])

            """ Create Demo account """
            CAPage(self.driver)\
                .open_manage_accounts()\
                .open_demo_section()\
                .open_new_account_btn()\
                .select_account_type(CAConstants.ACCOUNT_DEMO) \
                .select_currency(var.get_var(self.__class__.__name__)["demo_acc_currency"]) \
                .select_leverage_level(var.get_var(self.__class__.__name__)["demo_acc_leverage"]) \
                .set_initial_deposit(CAConstants.INITIAL_DEPOSIT0) \
                .verify_init_deposit_error() \
                .set_initial_deposit(CAConstants.INITIAL_DEPOSIT1) \
                .verify_init_deposit_error() \
                .set_initial_deposit(var.get_var(self.__class__.__name__)["initial_deposit_amount"]) \
                .click_create_account() \
                .verify_demo_account_created() \
                .open_demo_section()

            """ Verify Leverage """
            actual_leverage = CAPage(self.driver).get_leverage()
            expected_leverage = var.get_var(self.__class__.__name__)["demo_acc_leverage"]
            print(expected_leverage, actual_leverage)
            assert actual_leverage == expected_leverage

            """ Verify Currency """
            actual_currency = CAPage(self.driver).get_currency()
            expected_currency = var.get_var(self.__class__.__name__)["demo_acc_currency"]
            if global_var.current_brand_name == "trade99" or \
                    global_var.current_brand_name == "analystq":
                actual_currency = actual_currency.split(':')[0]
            assert actual_currency == expected_currency

            CAPage(self.driver).get_demo_account_number()

    def verify_account_in_crm(self):
        """ Login to CRM """
        if global_var.current_brand_name != "q8":
            CRMLoginPage(self.driver)\
                .open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET)) \
                .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

            sleep(2)
            ClientsPage(self.driver).find_client_by_email(CAConstants.EMAIL_CA)
            sleep(2)
            ClientProfilePage(self.driver).open_trading_accounts_tab()
            ClientsPage(self.driver).trading_account_exist(CAConstants.DEMO_ACCOUNT_NUMBER)
            ClientsPage(self.driver).trading_account_exist(CAConstants.LIVE_ACCOUNT_NUMBER)

        else:
            Logging().reportDebugStep(self, "Test is not running")
            return self

    def verify_account_in_crm_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CAConstants.EMAIL_CA)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        ClientsPage(self.driver)\
            .trading_account_exist_ui(CAConstants.DEMO_ACCOUNT_NUMBER)\
            .trading_account_exist_ui(CAConstants.LIVE_ACCOUNT_NUMBER)

    def add_demo_account_from_crm(self):
        lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        ClientsPage(self.driver)\
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        if ConvertLeadConstantsUI.EMAIL_EDITABLE:
            ClientsPage(self.driver) \
                .find_client_by_email(client1[LeadsModuleConstants.EMAIL])
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(lead1[LeadsModuleConstants.EMAIL])

        ClientProfilePage(self.driver) \
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if global_var.current_brand_name == "q8":
            MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT5),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif global_var.current_brand_name == "mpcrypto":
            MT4CreateAccountModule(self.driver) \
                .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_BCH),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif global_var.current_brand_name == "trade99":
            MT4CreateAccountModule(self.driver) \
                .create_account(
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY_BTC),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
                    self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif (global_var.current_brand_name == "dax-300") \
                or (global_var.current_brand_name == "gxfx") \
                or (global_var.current_brand_name == "kontofx") \
                or (global_var.current_brand_name == "uprofx"):
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
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if global_var.current_brand_name == "q8":
            MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT4),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self

        elif global_var.current_brand_name == "mpcrypto":
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

    def add_live_mt5_from_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        sleep(2)
        if global_var.current_brand_name == "q8":
            MT4CreateAccountModule(self.driver) \
                .create_account_with_platform(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT5),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, CRMConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_LEVERAGE))
            return self
        else:
            return self

    def add_mt5_demo_account_from_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        crm_client_profile\
            .open_mt4_actions(CRMConstants.CREATE_MT4_USER)
        MT4CreateAccountModule(self.driver) \
            .create_account_with_platform(
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_PLATFORM_MT5),
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_SERVER),
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_CURRENCY),
            self.config.get_value(TestDataConstants.TRADING_ACCOUNT1, TestDataConstants.TRADING_GROUP_DEMO),
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

        elif global_var.current_brand_name == "trade99":
            MT4CreateAccountModule(self.driver).update_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO_GROUP),
                MT4ModuleConstants.LEVERAGE_50)

        else:
            MT4CreateAccountModule(self.driver).update_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO_GROUP),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_UPDATED,
                                      TestDataConstants.TRADING_ACCOUNT_DEMO_LEVERAGE))

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
        return TradingAccountPrecondition(self.driver, self.config)
