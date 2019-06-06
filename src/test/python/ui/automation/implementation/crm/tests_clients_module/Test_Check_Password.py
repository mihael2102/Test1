import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.mt4.password.MT4CheckPasswordModule import MT4CheckPasswordModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.mt4.MT4DropDown import MT4DropDown
from src.main.python.ui.crm.model.constants.MT4ModuleConstants import MT4ModuleConstants


@pytest.mark.run(order=4)
class CheckPasswordTestCRM(BaseTest):

    def test_check_client_password_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        SidebarModules(self.driver)\
            .open_check_client_password() \
            .set_password_to_check(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                         LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
            .click_check()

        confirmation_message = crm_client_profile.get_confirm_message()
        self.assertEqual(confirmation_message, CRMConstants.CUSTOMER_PASSWORD_VALID_MESSAGE)
        crm_client_profile.click_ok()

    def test_check_mt4_password_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(
                        self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        crm_client_profile.perform_scroll_up()
        MT4DropDown(self.driver).open_mt4_module(MT4ModuleConstants.CHECK_MT_PASSWORD)

        MT4CheckPasswordModule(self.driver).select_account(account_number) \
                                           .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                        LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
                                           .click_check_button()

        message = crm_client_profile.get_confirm_message()
        crm_client_profile.click_ok()

        self.assertEqual(message, CRMConstants.MT4_PASSWORD_VALID_MESSAGE)

