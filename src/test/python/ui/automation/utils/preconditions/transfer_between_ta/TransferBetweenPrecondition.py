from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from time import sleep
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.mt4.transfer_between_ta.MT4TransferBetweenTa import MT4TransferBetweenTa
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class TransferBetweenPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def transfer_between_accounts(self):
        lead1 = self.config.get_value(LeadsModuleConstants.FIRST_LEAD_INFO)
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER))

        sleep(2)
        if ConvertLeadConstantsUI.EMAIL_EDITABLE:
            ClientsPage(self.driver) \
                .find_client_by_email(client1[LeadsModuleConstants.EMAIL])
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(lead1[LeadsModuleConstants.EMAIL])
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
