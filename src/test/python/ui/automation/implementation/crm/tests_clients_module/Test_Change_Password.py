import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.mt4.password.MT4CheckPasswordModule import MT4CheckPasswordModule
from src.main.python.ui.crm.model.mt4.password.MT4UpdatePasswordModule import MT4UpdatePasswordModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


@pytest.mark.run(order=5)
class ChangePasswordTestCRM(BaseTest):

    def test_change_client_password_from_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        # change the password to a new password
        SidebarModules(self.driver) \
            .open_change_client_password() \
            .set_password(self.config.get_value(TestDataConstants.CLIENT_ONE,
                                                TestDataConstants.NEW_PASSWORD)) \
            .click_change()

        message_confirm = crm_client_profile.get_confirm_message()
        crm_client_profile.click_ok()

        self.assertEqual(message_confirm, CRMConstants.CRM_CLIENT_AREA_PASSWORD_CHANGE)

    def test_change_mt4_password_from_crm(self):
        crm_client_profile = CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        if (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "gmo"):
            ClientsPage(self.driver) \
                .find_client_by_fname(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME))
        else:
            ClientsPage(self.driver) \
                .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        # Change the password to a new password
        crm_client_profile.perform_scroll_up().open_mt4_actions(CRMConstants.CHANGE_PASSWORD)

        MT4UpdatePasswordModule(self.driver).select_account(account_number) \
            .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.NEW_PASSWORD)) \
            .click_check_button()

        message_confirm = crm_client_profile.get_confirm_message_body()
        crm_client_profile.click_ok()

        self.assertEqual(message_confirm, CRMConstants.PASSWORD_CHANGE)

        # check the new password
        crm_client_profile.refresh_page().open_mt4_actions(CRMConstants.CHECK_PASSWORD_OLD_FOREX)

        MT4CheckPasswordModule(self.driver)\
            .select_account(account_number) \
            .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.NEW_PASSWORD))\
            .click_check_button()

        message_confirm = crm_client_profile.get_confirm_message_body()
        crm_client_profile.click_ok()

        if message_confirm:
            self.assertEqual(message_confirm, CRMConstants.CUSTOMER_PASSWORD_VALID_MESSAGE)

        # change the password back to the original password
        crm_client_profile.refresh_page().open_mt4_actions(CRMConstants.CHANGE_PASSWORD)

        MT4UpdatePasswordModule(self.driver)\
            .select_account(account_number) \
            .enter_password(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                        LeadsModuleConstants.FIRST_PASSWORD_LEAD)) \
            .click_check_button()

        message_confirm = crm_client_profile.get_confirm_message_body()
        crm_client_profile.click_ok()
        if message_confirm != "":
            self.assertEqual(message_confirm, CRMConstants.PASSWORD_CHANGE)
