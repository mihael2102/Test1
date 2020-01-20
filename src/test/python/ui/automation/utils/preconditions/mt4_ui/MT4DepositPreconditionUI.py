import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstants import MT4DepositConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
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
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI


@pytest.mark.run(order=13)
class MT4DepositPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def deposit_crm_new_ui(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open clients module. Find created client by email and open his profile """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   ConvertLeadConstantsUI.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .open_mt4_module_newui(CRMConstants.CREATE_MT_ACCOUNT)

        """ Create LIVE account for client using MT4 Actions """
        MT4CreateTAPageUI(self.driver) \
            .mt4_create_ta_ui(
            list1=MT4CreateTAConstantsUI.LIST_SERVER, server=MT4CreateTAConstantsUI.SERVER_LIVE,
            list2=MT4CreateTAConstantsUI.LIST_CURRENCY, currency=MT4CreateTAConstantsUI.CURRENCY,
            list3=MT4CreateTAConstantsUI.LIST_GROUP, group=MT4CreateTAConstantsUI.GROUP_LIVE,
            list4=MT4CreateTAConstantsUI.LIST_LEVERAGE, leverage=MT4CreateTAConstantsUI.LEVERAGE)

        """ Get account number to make deposit in future """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        account_number = GlobalTablePageUI(self.driver)\
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_TRADING_ACCOUNT_LOGIN,
                row=ClientDetailsConstantsUI.ROW_1)

        MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT = account_number

        """ Make deposit for account number using MT4 Actions """
        ClientDetailsPageUI(self.driver) \
            .open_mt4_module_newui(MT4ActionsConstantsUI.DEPOSIT)

        MT4DepositPageUI(self.driver)\
            .mt4_deposit_ui(
                list1=MT4DepositConstants.LIST_P_METHOD, p_method=MT4DepositConstants.P_METHOD,
                list2=MT4DepositConstants.LIST_STATUS, status=MT4DepositConstants.STATUS,
                list3=MT4DepositConstants.LIST_TA, t_account=account_number,
                field1=MT4DepositConstants.FIELD_AMOUNT, amount=MT4DepositConstants.AMOUNT,
                field2=MT4DepositConstants.FIELD_COMMENT, comment=MT4DepositConstants.COMMENT,
                list4=MT4DepositConstants.LIST_CLEARED_BY, cleared_by=MT4DepositConstants.CLEARED_BY)

        """ Verify successful message """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .refresh_page()

        """ Check balance was updated """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        balance = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_BALANCE,
                row=ClientDetailsConstantsUI.ROW_1)
        CRMBaseMethodsPage(self.driver)\
            .comparator_string(
                balance,
                MT4DepositConstants.AMOUNT)

        """ Verify data in info tag Balance was updated """
        balance_tag = ClientDetailsPageUI(self.driver)\
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_BALANCE)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_DEPOSIT_BTC in balance_tag
        else:
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in balance_tag

        """ Verify data in info tag Deposit was updated """
        deposit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_DEPOSIT)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_DEPOSIT_BTC in deposit_tag
        else:
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in deposit_tag

        """ Verify data in info tag Equity was updated """
        equity_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_EQUITY)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_DEPOSIT_BTC in equity_tag
        else:
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in equity_tag

        """ Verify data in info tag Free Margin was updated """
        free_margin_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_FREE_MARGIN)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_DEPOSIT_BTC in free_margin_tag
        else:
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in free_margin_tag

        """ Verify data in info tag Net Deposit was updated """
        net_deposit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_NET_DEPOSIT)
        if global_var.current_brand_name == "trade99":
            assert CRMConstants.AMOUNT_DEPOSIT_BTC in net_deposit_tag
        else:
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in net_deposit_tag
