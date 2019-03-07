from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from time import sleep
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.mt4.withdraw.MT4WithdrawModule import MT4WithdrawModule


class WithdrawPreconditionCRM(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_withdraw(self):
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
        ClientProfilePage(self.driver).scroll_to_financial_transactions_section() \
                                      .open_financial_transactions_tab()
        account_number = ClientProfilePage(self.driver).get_trading_account_number()
        ClientProfilePage(self.driver).open_mt4_actions(CRMConstants.WITHDRAW)
        MT4WithdrawModule(self.driver).select_payment_method(CRMConstants.PAYMENT_METHOD_WITHDRAW) \
                                      .select_account(account_number) \
                                      .set_amount(CRMConstants.AMOUNT_WITHDRAW) \
                                      .set_description(CRMConstants.DESCRIPTION_WITHDRAW) \
                                      .select_status(CRMConstants.STATUS_WITHDRAW)
        if global_var.current_brand_name == "q8":
            MT4WithdrawModule(self.driver).select_cleared_by(CRMConstants.CLEAREDBY_WITHDRAW1)
        else:
            MT4WithdrawModule(self.driver).select_cleared_by(CRMConstants.CLEAREDBY_WITHDRAW)
        MT4WithdrawModule(self.driver).create_withdraw_button()
        CRMLoginPage(self.driver).perform_scroll_up()
        ClientProfilePage(self.driver).click_trading_accounts_tab() \
                                      .open_trading_accounts_tab() \
                                      .open_trading_account_page(account_number)
        balance = ClientProfilePage(self.driver).get_balance_in_trading_account()
        actual_balance = int((balance.split('.'))[0])
        expected_balance = int(((CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT).split('.'))[0]) - int(CRMConstants.AMOUNT_WITHDRAW)
        assert actual_balance == expected_balance

