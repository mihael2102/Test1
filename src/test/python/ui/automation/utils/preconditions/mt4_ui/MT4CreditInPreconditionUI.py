import pytest
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4DepositConstantsUI import MT4DepositConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreateTAPageUI import MT4CreateTAPageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreditInPageUI import MT4CreditInPageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreditInConstantsUI import MT4CreditInConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4WithdrawConstantsUI import MT4WithdrawConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class MT4CreditInPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def credit_in_crm_ui(self):
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
        currency = ConvertLeadConstantsUI.GET_CURRENCY
        MT4CreateTAPageUI(self.driver) \
            .mt4_create_ta_ui(
            list1=MT4CreateTAConstantsUI.LIST_SERVER, server=MT4CreateTAConstantsUI.SERVER_LIVE,
            list2=MT4CreateTAConstantsUI.LIST_CURRENCY, currency=currency,
            list3=MT4CreateTAConstantsUI.LIST_GROUP, group_number="1",
            list4=MT4CreateTAConstantsUI.LIST_LEVERAGE, leverage=MT4CreateTAConstantsUI.LEVERAGE,
            final_btn=MT4CreateTAConstantsUI.BTN_FINAL)

        """ Get account number to make Credit in """
        record_num = ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS) \
            .get_last_record_number()
        account_number = GlobalModulePageUI(self.driver)\
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_LOGIN,
                row=record_num)

        MT4CreditInConstantsUI.TA_CREDIT = account_number

        """ Make Credit in """
        ClientDetailsPageUI(self.driver) \
            .open_mt4_module_newui(MT4ActionsConstantsUI.CREDIT_IN)

        if ConvertLeadConstantsUI.GET_CURRENCY == "BTC":
            amount = MT4DepositConstantsUI.AMOUNT_CRYPTO
        else:
            amount = MT4CreditInConstantsUI.AMOUNT

        MT4CreditInPageUI(self.driver)\
            .mt4_credit_in_ui(
                list1=MT4CreditInConstantsUI.LIST_TA, t_account=MT4CreditInConstantsUI.TA_CREDIT,
                field1=MT4CreditInConstantsUI.FIELD_AMOUNT, amount=amount,
                day=MT4CreditInConstantsUI.DAY, month=MT4CreditInConstantsUI.MONTH, year=MT4CreditInConstantsUI.YEAR,
                field2=MT4CreditInConstantsUI.FIELD_GRANTED_BY, granted_by=MT4CreditInConstantsUI.GRANTED_BY,
                field3=MT4CreditInConstantsUI.FIELD_COMMENT, comment=MT4CreditInConstantsUI.COMMENT,
                final_btn=MT4CreditInConstantsUI.BTN_FINAL) \
            .refresh_page()

        """ Check credit was updated """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        credit = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_CREDIT,
                row=record_num)

        counter = 0
        while amount != credit:
            ClientDetailsPageUI(self.driver)\
                .refresh_page()
            ClientDetailsPageUI(self.driver) \
                .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
            credit = GlobalModulePageUI(self.driver) \
                .get_data_from_list_view_ui(
                    column=ClientDetailsConstantsUI.COLUMN_CREDIT,
                    row=record_num)
            counter += 1
            if counter == 7:
                break

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
                credit,
                amount)

        """ Verify data in info tag Credit was updated """
        credit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_CREDIT)
        assert MT4CreditInConstantsUI.AMOUNT.split('.')[0] in credit_tag

        """ Verify data in info tag Equity, Free Margin were updated """
        equity_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_EQUITY)
        free_margin_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_FREE_MARGIN)

        expected_equity = int(MT4DepositConstantsUI.AMOUNT.split('.')[0]) - \
                          int(MT4WithdrawConstantsUI.AMOUNT.split('.')[0]) + \
                          int(MT4CreditInConstantsUI.AMOUNT.split('.')[0])
        assert str(expected_equity) in equity_tag
        assert str(expected_equity) in free_margin_tag
