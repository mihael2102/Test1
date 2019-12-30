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
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.constants.ClientDetailsConstants import ClientDetailsConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.mt4.transfer_between_ta.MT4TransferBetweenTa import MT4TransferBetweenTa
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown


class TransferBetweenPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def transfer_between_accounts(self):
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(client1[LeadsModuleConstants.EMAIL])
        sleep(2)

        # Get ta accounts info
        crm_client_profile = ClientProfilePage(self.driver)

        ClientProfilePage(self.driver)\
            .click_trading_accounts_tab() \
            .open_trading_accounts_tab()
        sleep(2)
        first_account_number = ClientProfilePage(self.driver).get_trading_account_number_from_ta(
                                                        CRMConstants.FIRST_TA_NUMBER_FROM_TA_SECTION)
        second_account_number = ClientProfilePage(self.driver).get_trading_account_number_from_ta(
                                                        CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)
        first_account_balance = ClientProfilePage(self.driver).get_balance_of_trading_account\
                                                        (CRMConstants.FIRST_TA_NUMBER_FROM_TA_SECTION)
        second_account_balance = ClientProfilePage(self.driver).get_balance_of_trading_account\
                                                        (CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)

        if global_var.current_brand_name == "trade99":
            expected_balance = crm_client_profile \
                .get_difference_amount_text(second_account_balance, CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_BTC)
            crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.TRANSFER_BETWEEN_TA2)
            MT4TransferBetweenTa(self.driver).make_transfer_between_ta(second_account_number,
                                                                       first_account_number,
                                                                       CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_BTC,
                                                                       CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)
        else:
            expected_balance = crm_client_profile \
                .get_difference_amount_text(second_account_balance,
                                            CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA)
            crm_client_profile\
                .perform_scroll_up()\
                .open_mt4_actions(CRMConstants.TRANSFER_BETWEEN_TA)

            MT4TransferBetweenTa(self.driver)\
                .make_transfer_between_ta(second_account_number,
                                          first_account_number,
                                          CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA,
                                          CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)

        confirmation_message = crm_client_profile.get_confirm_message()

        try:
            assert confirmation_message == CRMConstants.TRANSFER_BETWEEN_TA_MESSAGE
        except (NoSuchElementException, TimeoutException, AssertionError):
            pass

        amount_transfer = crm_client_profile.click_ok() \
            .click_trading_accounts_tab().get_balance_of_trading_account(CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)

        count = 0
        while amount_transfer != expected_balance:
            ClientProfilePage(self.driver).refresh_page()
            sleep(2)
            amount_transfer = ClientProfilePage(self.driver).get_balance_of_trading_account\
                (CRMConstants.SECOND_TA_NUMBER_FROM_TA_SECTION)
            count += 1
            if count == 7:
                break
        assert amount_transfer == expected_balance

    def transfer_between_accounts_new_ui(self):
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        # Open clients module. Find created client by email and open his profile
        CRMHomePage(self.driver) \
            .open_client_module_new_ui() \
            .select_filter_new_ui(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email_new_ui(client1[LeadsModuleConstants.EMAIL])

        # Get balance of accounts and calculate of expected total:
        crm_client_profile = ClientProfilePage(self.driver)
        ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT)
        balance1 = TradingAccountsInformationPage(self.driver)\
            .get_balance_text()

        ClientsPage(self.driver)\
            .came_back_on_previous_page()
        sleep(0.5)
        ClientProfilePage(self.driver) \
            .refresh_page()\
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(MT4ModuleConstants.ACCOUNT_NUMBER_CREDIT)
        balance2 = TradingAccountsInformationPage(self.driver) \
            .get_balance_text()

        ClientsPage(self.driver) \
            .came_back_on_previous_page()

        if global_var.current_brand_name == "trade99":
            expected_balance1 = crm_client_profile \
                .get_difference_amount_text(balance1, CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_BTC)
        else:
            expected_balance1 = crm_client_profile \
                .get_difference_amount_text(balance1[0], CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA[0])

        if global_var.current_brand_name == "trade99":
            expected_balance2 = crm_client_profile \
                .get_sum_amount_text(balance2, CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_BTC)
        else:
            expected_balance2 = crm_client_profile \
                .get_sum_amount_text(balance2[0], CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA[0])

        # Make Transfer between TA:
        MT4DropDown(self.driver) \
            .open_mt4_module_newui(CRMConstants.CREATE_MT_TRANSFER)

        if global_var.current_brand_name == "trade99":
            MT4TransferBetweenTa(self.driver)\
                .make_transfer_between_ta_new_ui(MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT,
                                                 MT4ModuleConstants.ACCOUNT_NUMBER_CREDIT,
                                                 CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_BTC,
                                                 CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)
        else:
            MT4TransferBetweenTa(self.driver)\
                .make_transfer_between_ta_new_ui(MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT,
                                                 MT4ModuleConstants.ACCOUNT_NUMBER_CREDIT,
                                                 CRMConstants.AMOUNT_TRANSFER_BETWEEN_TA_1,
                                                 CRMConstants.DESCRIPTION_TRANSFER_BETWEEN_TA)

        # Check confirmation message:
        MT4CreateAccountModule(self.driver) \
            .verify_success_message()
        CRMHomePage(self.driver) \
            .click_ok()

        # Check the balance of first account updated:
        ClientProfilePage(self.driver) \
            .refresh_page() \
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT)
        balance_first = TradingAccountsInformationPage(self.driver)\
            .get_balance_text()
        if global_var.current_brand_name != "trade99":
            balance_first = balance_first[0]

        count = 0
        while balance_first != expected_balance1:
            ClientProfilePage(self.driver).refresh_page()
            sleep(2)
            balance_first = TradingAccountsInformationPage(self.driver)\
                .get_balance_text()
            if global_var.current_brand_name != "trade99":
                balance_first = balance_first[0]
            count += 1
            if count == 7:
                break
        assert balance_first == expected_balance1

        # Check the balance of second account updated:
        ClientsPage(self.driver) \
            .came_back_on_previous_page()

        ClientProfilePage(self.driver) \
            .refresh_page() \
            .open_tab(ClientDetailsConstants.TRADING_ACCOUNTS_TAB) \
            .open_trading_account_by_number(MT4ModuleConstants.ACCOUNT_NUMBER_CREDIT)
        balance_second = TradingAccountsInformationPage(self.driver)\
            .get_balance_text()
        if global_var.current_brand_name != "trade99":
            balance_second = balance_second[0]

        count = 0
        while balance_second != expected_balance2:
            ClientProfilePage(self.driver).refresh_page()
            sleep(2)
            balance_second = TradingAccountsInformationPage(self.driver)\
                .get_balance_text()
            if global_var.current_brand_name != "trade99":
                balance_second = balance_second[0]
            count += 1
            if count == 7:
                break
        assert balance_second == expected_balance2
