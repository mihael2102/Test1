import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstantsUI import MT4DepositConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4WithdrawConstantsUI import MT4WithdrawConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4WithdrawPageUI import MT4WithdrawPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI


@pytest.mark.run(order=13)
class MT4WithdrawPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def withdraw_crm_ui(self):
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
            .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   data=CreateLeadConstantsUI.EMAIL)

        """ Make Withdraw for account number using MT4 Actions """
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(row='1') \
            .open_mt4_module_newui(MT4ActionsConstantsUI.WITHDRAW)

        if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
            amount = MT4WithdrawConstantsUI.AMOUNT_CRYPTO
        else:
            amount = MT4WithdrawConstantsUI.AMOUNT

        MT4WithdrawPageUI(self.driver)\
            .mt4_withdraw_ui(
                list1=MT4WithdrawConstantsUI.LIST_P_METHOD, p_method='2',
                list2=MT4WithdrawConstantsUI.LIST_STATUS, status=MT4WithdrawConstantsUI.STATUS,
                list3=MT4WithdrawConstantsUI.LIST_TA, t_account=MT4DepositConstantsUI.TA,
                field1=MT4WithdrawConstantsUI.FIELD_AMOUNT, amount=amount,
                field2=MT4WithdrawConstantsUI.FIELD_COMMENT, comment=MT4WithdrawConstantsUI.COMMENT,
                list4=MT4WithdrawConstantsUI.LIST_CLEARED_BY, cleared_by='2',
                final_btn=MT4WithdrawConstantsUI.BTN_FINAL) \
            .refresh_page()

        """ Check balance was updated """
        record_num = ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS) \
            .get_last_record_number()
        actual_balance = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_BALANCE,
                row=record_num)
        actual_balance = actual_balance.split(" ")[1]

        if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
            balance = MT4WithdrawConstantsUI.BALANCE_CRYPTO
        else:
            balance = MT4WithdrawConstantsUI.BALANCE
        count = 0
        while actual_balance != balance:
            GlobalModulePageUI(self.driver)\
                .refresh_page()
            sleep(2)
            ClientDetailsPageUI(self.driver) \
                .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
            actual_balance = GlobalModulePageUI(self.driver) \
                .get_data_from_list_view_ui(
                    column=ClientDetailsConstantsUI.COLUMN_BALANCE,
                    row=record_num)
            actual_balance = actual_balance.split(" ")[1]
            count += 1
            if count == 10:
                break
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
                actual_balance,
                balance)

        # """ Verify data in info tag Withdrawals was updated """
        # withdrawals_tag = ClientDetailsPageUI(self.driver) \
        #     .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_WITHDRAWALS)
        # if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
        #     assert amount in withdrawals_tag
        # else:
        #     assert amount.split(".")[0] in withdrawals_tag
        #
        # """ Verify data in info tag Balance, Equity, Free Margin, Net Deposit was updated """
        # balance_tag = ClientDetailsPageUI(self.driver) \
        #     .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_BALANCE)
        # equity_tag = ClientDetailsPageUI(self.driver) \
        #     .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_EQUITY)
        # free_margin_tag = ClientDetailsPageUI(self.driver) \
        #     .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_FREE_MARGIN)
        # net_deposit_tag = ClientDetailsPageUI(self.driver) \
        #     .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_NET_DEPOSIT)
        # if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
        #     expected_balance = float(MT4DepositConstantsUI.AMOUNT_CRYPTO) - float(MT4WithdrawConstantsUI.AMOUNT_CRYPTO)
        #     assert str(expected_balance) in balance_tag
        #     assert str(expected_balance) in equity_tag
        #     assert str(expected_balance) in free_margin_tag
        #     assert str(expected_balance) in net_deposit_tag
        # else:
        #     expected_balance = int((MT4DepositConstantsUI.AMOUNT.split('.'))[0]) \
        #                        - int((MT4WithdrawConstantsUI.AMOUNT.split('.'))[0])
        #     assert str(expected_balance) in balance_tag
        #     assert str(expected_balance) in equity_tag
        #     assert str(expected_balance) in free_margin_tag
        #     assert str(expected_balance) in net_deposit_tag
