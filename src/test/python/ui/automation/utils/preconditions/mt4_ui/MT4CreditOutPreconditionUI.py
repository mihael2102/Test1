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
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreditOutPageUI import MT4CreditOutPageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreditInConstantsUI import MT4CreditInConstantsUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreditOutConstantsUI import MT4CreditOutConstantsUI


@pytest.mark.run(order=13)
class MT4CreditOutPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def credit_out_crm_ui(self):
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
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   CreateLeadConstantsUI.EMAIL)

        """ Make Credit Out """
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .open_mt4_module_newui(MT4ActionsConstantsUI.CREDIT_OUT)

        MT4CreditOutPageUI(self.driver)\
            .mt4_credit_out_ui(
                list1=MT4CreditOutConstantsUI.LIST_TA, t_account=MT4CreditInConstantsUI.TA_CREDIT,
                field1=MT4CreditOutConstantsUI.FIELD_AMOUNT, amount=MT4CreditOutConstantsUI.AMOUNT,
                field2=MT4CreditOutConstantsUI.FIELD_GRANTED_BY, granted_by=MT4CreditOutConstantsUI.GRANTED_BY,
                field3=MT4CreditOutConstantsUI.FIELD_COMMENT, comment=MT4CreditOutConstantsUI.COMMENT)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .refresh_page()

        """ Check credit was updated """
        ClientDetailsPageUI(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
        credit = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_CREDIT,
                row=ClientDetailsConstantsUI.ROW_3)

        counter = 0
        while MT4CreditOutConstantsUI.EXPECTED_CREDIT != credit:
            ClientDetailsPageUI(self.driver)\
                .refresh_page()
            ClientDetailsPageUI(self.driver) \
                .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)
            credit = GlobalModulePageUI(self.driver) \
                .get_data_from_list_view_ui(
                column=ClientDetailsConstantsUI.COLUMN_CREDIT,
                row=ClientDetailsConstantsUI.ROW_3)
            counter += 1
            if counter == 7:
                break

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(
                credit,
                MT4CreditOutConstantsUI.EXPECTED_CREDIT)

        """ Verify data in info tag Credit was updated """
        credit_tag = ClientDetailsPageUI(self.driver) \
            .get_data_from_info_tag(ClientDetailsConstantsUI.TAG_CREDIT)
        expected_credit = MT4CreditOutConstantsUI.EXPECTED_CREDIT.split('.')[0]
        assert expected_credit in credit_tag
