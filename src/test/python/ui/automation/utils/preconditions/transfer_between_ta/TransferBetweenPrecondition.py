from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


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
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(client1[LeadsModuleConstants.EMAIL])
        sleep(2)
        ClientProfilePage(self.driver).click_trading_accounts_tab() \
                                      .open_trading_accounts_tab()
        trading_account_info = ClientProfilePage(self.driver).get_trading_account_info()
        ta_currency = ""
        ta_number = ""
        if "Live" in trading_account_info:
            ta_currency = ClientProfilePage(self.driver).get_first_account_currency()
        else:
            ta_currency = ClientProfilePage(self.driver).get_second_account_currency()







    # def add_two_usd_currencies(self):
    #     BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
    #         .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
    #                     Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
    #         .click_login_button() \
    #         .open_drop_down_menu() \
    #         .select_module(CaConstants.MANAGE_ACCOUNTS)
    #
    #     CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
    #         .create_account_button()
    #     CaManageAccounts() \
    #         .open_new_account_button() \
    #         .select_account_currency(
    #         Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ACCOUNT_CURRENCY_USD)) \
    #         .create_account_button()
    #
    #     return TransferBetweenPrecondition()
    #
    # def make_deposit(self):
    #     crm_client_profile = CRMLoginPage() \
    #         .open_second_tab_page(Config.url_crm) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET)) \
    #         .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
    #         .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
    #
    #     account_number = crm_client_profile \
    #         .perform_scroll_down() \
    #         .open_trading_accounts_tab() \
    #         .get_client_account()
    #
    #     crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.DEPOSIT)
    #
    #     MT4DepositModule().make_deposit(account_number, CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
    #                                     CRMConstants.PAYMENT_METHOD_DEPOSIT,
    #                                     CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT) \
    #         .click_ok() \
    #         .refresh_page()
    #
    #     crm_client_profile.click_trading_accounts_tab().get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
    #     return TransferBetweenPrecondition()
