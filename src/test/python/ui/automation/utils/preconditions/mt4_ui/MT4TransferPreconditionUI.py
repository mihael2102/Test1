import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstantsUI import MT4DepositConstantsUI
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4DepositPageUI import MT4DepositPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreateTAPageUI import MT4CreateTAPageUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4TransferPageUI import MT4TransferPageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreditInConstantsUI import MT4CreditInConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4TransferConstantsUI import MT4TransferConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalDetailsPageUI import GlobalDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.pages.trading_ui.TradingModulePageUI import TradingModulePageUI
from src.main.python.ui.crm.model.constants_ui.trading_ui.TradingDetailsConstantsUI import TradingDetailsConstantsUI


@pytest.mark.run(order=13)
class MT4TransferPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def transfer_crm_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                new_design=0,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open clients module. Find created client by email and open his profile """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CreateLeadConstantsUI.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .open_mt4_module_newui(MT4ActionsConstantsUI.TRANSFER)

        """ Make Transfer """
        MT4TransferPageUI(self.driver)\
            .mt4_transfer_ui(
                list1=MT4TransferConstantsUI.LIST_SOURCE, source=MT4DepositConstantsUI.TA,
                list2=MT4TransferConstantsUI.LIST_DESTINATION, destination=MT4CreditInConstantsUI.TA_CREDIT,
                field1=MT4TransferConstantsUI.FIELD_AMOUNT, amount=MT4TransferConstantsUI.AMOUNT)

        """ Verify successful message """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .refresh_page()

        """ Check balance of both ta was updated """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        balance1 = TradingModulePageUI(self.driver) \
            .click_on_ta_number(MT4DepositConstantsUI.TA) \
            .get_text_from_field(TradingDetailsConstantsUI.FIELD_BALANCE)
        expected_balance1 = MT4TransferConstantsUI.EXPECTED_BALANCE_1

        count = 0
        while balance1 != expected_balance1:
            ClientDetailsPageUI(self.driver).refresh_page()
            sleep(2)
            balance1 = GlobalDetailsPageUI(self.driver) \
                .get_text_from_field(TradingDetailsConstantsUI.FIELD_BALANCE)
            count += 1
            if count == 7:
                break

        CRMBaseMethodsPage(self.driver)\
            .comparator_string(
                balance1,
                expected_balance1) \
            .came_back_on_previous_page()

        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        balance2 = TradingModulePageUI(self.driver) \
            .click_on_ta_number(MT4CreditInConstantsUI.TA_CREDIT) \
            .get_text_from_field(TradingDetailsConstantsUI.FIELD_BALANCE)
        expected_balance2 = MT4TransferConstantsUI.EXPECTED_BALANCE_2

        count = 0
        while balance2 != expected_balance2:
            ClientDetailsPageUI(self.driver).refresh_page()
            sleep(2)
            balance2 = GlobalDetailsPageUI(self.driver) \
                .get_text_from_field(TradingDetailsConstantsUI.FIELD_BALANCE)
            count += 1
            if count == 7:
                break

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
            balance2,
            expected_balance2)
