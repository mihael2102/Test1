from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from time import sleep
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.mt4.credit_out.MT4CreditOutModule import MT4CreditOutModule
from src.main.python.utils.config import Config



class CreditOutPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def credit_out_crm(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                              TestDataConstants.E_MAIL))
        sleep(2)
        ClientProfilePage(self.driver).open_mt4_actions(CRMConstants.CREDIT_OUT)
        MT4CreditOutModule(self.driver).make_credit_out(CRMConstants.CREDIT_ACCOUNT, CRMConstants.AMOUNT_CREDIT_OUT,
                                                        CRMConstants.CREDIT_OUT_COMMENT,
                                                        CRMConstants.EXPIRE_DATE.strftime(CRMConstants.FORMAT_DATE), CRMConstants.CLEARNED_BY)
        sleep(3)
        ClientProfilePage(self.driver).refresh_page() \
            .click_trading_accounts_tab() \
            .open_trading_accounts_tab() \
            .open_trading_account_page(CRMConstants.CREDIT_ACCOUNT)

        actual_credit = MT4CreditOutModule(self.driver).get_credit_int()
        expected_credit = int(((CRMConstants.AMOUNT_CREDIT_IN).split('.'))[0]) - int(
            ((CRMConstants.AMOUNT_CREDIT_OUT).split('.'))[0])
        count = 0
        while actual_credit != expected_credit:
            sleep(1)
            CRMHomePage(self.driver).refresh_page()
            sleep(3)
            actual_credit = MT4CreditOutModule(self.driver).get_credit_int()
            count += 1
            if count == 10:
                break
        assert actual_credit == expected_credit

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
        return CreditOutPrecondition()

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

        crm_client_profile.click_trading_accounts_tab().get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
        return CreditOutPrecondition()
