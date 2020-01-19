import pytest
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.client_deposit.CRMClientDeposit import CRMClientDeposit
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.mt4.create_account.MT4CreateAccountModule import MT4CreateAccountModule
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI


@pytest.mark.run(order=13)
class DepositPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def deposit_crm_new_ui(self):
        client1 = self.config.get_value(TestDataConstants.CLIENT_ONE)
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url'))\
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """
            ADD LIVE ACCOUNT IN CRM
            Open clients module. Find created client by email and open his profile
        """
        CRMHomePage(self.driver)\
            .open_client_module_new_ui()\
            .select_filter_new_ui(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))\
            .find_client_by_email_new_ui(client1[LeadsModuleConstants.EMAIL])

        """ Create LIVE account for client using MT4 Actions """
        crm_client_profile = ClientProfilePage(self.driver)
        MT4DropDown(self.driver) \
            .open_mt4_module_newui(CRMConstants.CREATE_MT_ACCOUNT)

        MT4CreateAccountModule(self.driver) \
            .create_account_new_ui(
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_SERVER_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_CURRENCY_EUR),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_GROUP_LIVE),
                self.config.get_value(TestDataConstants.TRADING_ACCOUNT1_LIVE, TestDataConstants.TRADING_LEVERAGE_LIVE))
        ClientProfilePage(self.driver)\
            .click_ok()

        """ Get account number to make deposit in future """
        account_number = ClientProfilePage(self.driver) \
            .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)\
            .get_ta_number()

        MT4ModuleConstants.ACCOUNT_NUMBER_DEPOSIT = account_number

        """ Make deposit for account number using MT4 Actions """
        MT4DropDown(self.driver) \
            .open_mt4_module_newui(CRMConstants.CREATE_MT_DEPOSIT)

        if global_var.current_brand_name == "trade99":
            MT4DepositModule(self.driver)\
                .make_deposit_new_ui(account_number,
                                     CRMConstants.AMOUNT_DEPOSIT_BTC,
                                     CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                     CRMConstants.STATUS_DEPOSIT,
                                     CRMConstants.DESCRIPTION_DEPOSIT,
                                     MT4ModuleConstants.CLEARED_BY)
        else:
            MT4DepositModule(self.driver)\
                .make_deposit_new_ui(account_number,
                                     CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT,
                                     CRMConstants.PAYMENT_METHOD_DEPOSIT,
                                     CRMConstants.STATUS_DEPOSIT,
                                     CRMConstants.DESCRIPTION_DEPOSIT,
                                     MT4ModuleConstants.CLEARED_BY1)

        """ Check confirmation message """
        MT4CreateAccountModule(self.driver) \
            .verify_success_message()
        CRMHomePage(self.driver) \
            .click_ok()

        """ Check balance was updated """
        crm_client_profile\
            .refresh_page()

        if global_var.current_brand_name == "trade99":
            deposit_amount_text = crm_client_profile\
                .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)\
                .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_BTC)
            assert CRMConstants.AMOUNT_DEPOSIT_BTC == deposit_amount_text
        else:
            deposit_amount_text = crm_client_profile\
                .open_tab(ClientDetailsConstantsUI.TAB_TRADING_ACCOUNTS)\
                .get_amount_text(CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT)
            assert CRMConstants.AMOUNT_DEPOSIT_FOR_CREDIT_OUT == deposit_amount_text

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
