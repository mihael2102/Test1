import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstantsUI import MT4DepositConstantsUI
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4DepositPageUI import MT4DepositPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreateTAPageUI import MT4CreateTAPageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class MT4DepositPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def deposit_crm_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open clients module. Find created client by email and open his profile """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CreateLeadConstantsUI.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .open_mt4_module_newui(var.get_var(self.__class__.__name__)["create_mt_user"])

        """ Create LIVE account for client using MT4 Actions """
        MT4CreateTAPageUI(self.driver) \
            .mt4_create_ta_ui(
            list1=MT4CreateTAConstantsUI.LIST_SERVER, server=MT4CreateTAConstantsUI.SERVER_LIVE,
            list2=MT4CreateTAConstantsUI.LIST_CURRENCY,
            # currency=var.get_var(self.__class__.__name__)["l_acc_currency"],
            list3=MT4CreateTAConstantsUI.LIST_GROUP, group_number="1",
            list4=MT4CreateTAConstantsUI.LIST_LEVERAGE, leverage=MT4CreateTAConstantsUI.LEVERAGE)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Get account number to make deposit in future """
        record_num = ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS) \
            .get_last_record_number()
        account_number = GlobalModulePageUI(self.driver)\
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_LOGIN,
                row=record_num)

        MT4DepositConstantsUI.TA = account_number

        """ Make deposit for account number using MT4 Actions """
        ClientDetailsPageUI(self.driver) \
            .open_mt4_module_newui(MT4ActionsConstantsUI.DEPOSIT)
        if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
            amount = MT4DepositConstantsUI.AMOUNT_CRYPTO
        else:
            amount = MT4DepositConstantsUI.AMOUNT
        MT4DepositPageUI(self.driver)\
            .mt4_deposit_ui(
                list1=MT4DepositConstantsUI.LIST_P_METHOD, p_method=MT4DepositConstantsUI.P_METHOD,
                list2=MT4DepositConstantsUI.LIST_STATUS, status=MT4DepositConstantsUI.STATUS,
                list3=MT4DepositConstantsUI.LIST_TA, t_account=account_number,
                field1=MT4DepositConstantsUI.FIELD_AMOUNT, amount=amount,
                field2=MT4DepositConstantsUI.FIELD_COMMENT, comment=MT4DepositConstantsUI.COMMENT,
                list4=MT4DepositConstantsUI.LIST_CLEARED_BY, cleared_by=MT4DepositConstantsUI.CLEARED_BY,
                final_btn=MT4DepositConstantsUI.BTN_FINAL)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .refresh_page()

        """ Check balance was updated """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        balance = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_BALANCE,
                row=record_num)
        CRMBaseMethodsPage(self.driver)\
            .comparator_string(
                balance,
                amount)

        """ Verify data in info tag Balance was updated """
        balance_tag = ClientDetailsPageUI(self.driver)\
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_BALANCE)
        if ConvertLeadConstantsUI.GET_CURRENCY != "BTC":
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in balance_tag

        """ Verify data in info tag Deposit was updated """
        deposit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_DEPOSIT)
        if ConvertLeadConstantsUI.GET_CURRENCY != "BTC":
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in deposit_tag

        """ Verify data in info tag Equity was updated """
        equity_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_EQUITY)
        if ConvertLeadConstantsUI.GET_CURRENCY != "BTC":
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in equity_tag

        """ Verify data in info tag Free Margin was updated """
        free_margin_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_FREE_MARGIN)
        if ConvertLeadConstantsUI.GET_CURRENCY != "BTC":
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in free_margin_tag

        """ Verify data in info tag Net Deposit was updated """
        net_deposit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_NET_DEPOSIT)
        if ConvertLeadConstantsUI.GET_CURRENCY != "BTC":
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT.split(".")[0] in net_deposit_tag
