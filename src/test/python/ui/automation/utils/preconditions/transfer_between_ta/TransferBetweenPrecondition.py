from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.transfer_between_ta.MT4TransferBetweenTa import MT4TransferBetweenTa
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage


class TransferBetweenPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def transfer_between_accounts(self):
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        CRMHomePage(self.driver).open_client_module() \
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(client1[LeadsModuleConstants.EMAIL])

        # Create LIVE account for client using MT4 Actions
        crm_client_profile = ClientProfilePage(self.driver)
        crm_client_profile.open_mt4_actions(CRMConstants.CREATE_MT4_USER)

        if global_var.current_brand_name == "finmarket":
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                      TestDataConstants.TRADING_SERVER_LIVE_OLD_FOREX),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                      TestDataConstants.TRADING_GROUP_LIVE_FINMARKET),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE)) \
                .click_close()

        else:
            MT4CreateAccountModule(self.driver) \
                .create_account(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE,
                                      TestDataConstants.TRADING_SERVER_LIVE_OLD_FOREX),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE)) \
                .click_close()
        sleep(2)
        ClientProfilePage(self.driver).click_trading_accounts_tab() \
                                      .open_trading_accounts_tab()
        sleep(2)
        first_account_number = ClientProfilePage(self.driver).get_trading_account_number_from_ta(
            CRMConstants.FIRST_TA_NUMBER_FROM_TA_SECTION)
        second_account_number = ClientProfilePage(self.driver).get_trading_account_number_from_ta(
            CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)
        first_account_balance = ClientProfilePage(self.driver).get_balance_of_trading_account \
            (CRMConstants.FIRST_TA_NUMBER_FROM_TA_SECTION)
        second_account_balance = ClientProfilePage(self.driver).get_balance_of_trading_account \
            (CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)

        # amount_initial = crm_client_profile.get_initial_amount()

        expected_balance = crm_client_profile \
            .get_difference_amount_text(second_account_balance, CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA)

        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.TRANSFER_BETWEEN_TA)

        MT4TransferBetweenTa(self.driver).make_transfer_between_ta(second_account_number, first_account_number,
                                                                   CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA,
                                                                   CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)

        confirmation_message = crm_client_profile.get_confirm_message()

        assert confirmation_message == CRMConstants.TRANSFER_BETWEEN_TA_MESSAGE

        amount_transfer = crm_client_profile.click_ok() \
            .click_trading_accounts_tab().get_balance_of_trading_account(CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)

        while amount_transfer != expected_balance:
            ClientProfilePage(self.driver).refresh_page()
            sleep(2)
            amount_transfer = ClientProfilePage(self.driver).get_balance_of_trading_account \
                (CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)
        assert amount_transfer == expected_balance


    def add_two_usd_currencies(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
            .create_account_button()
        CaManageAccounts() \
            .open_new_account_button() \
            .select_account_currency(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
            .create_account_button()

        return TransferBetweenPrecondition()

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
                                        CRMConstants.STATUS_DEPOSIT) \
                          .click_ok() \
                          .refresh_page()

        crm_client_profile.click_trading_accounts_tab().get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
        return TransferBetweenPrecondition()
