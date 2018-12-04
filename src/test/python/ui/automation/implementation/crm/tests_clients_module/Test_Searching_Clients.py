import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage

@pytest.mark.run(order=3)
class SearchingClientsTestCRM(BaseTest):

    def test_make_searching_client_module(self):
        # Test depends on test 'test_perform_convert_lead'
        # Please run it before current test because we need to create new client firstly.
        crm_client_profile = CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            # .perform_searching(
            # self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
            # self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
            # self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        if (global_var.current_brand_name == "xtraderfx") or (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "itrader"):
                sleep(15)
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif (global_var.current_brand_name == "4xfx") or (global_var.current_brand_name == "fxpmarkets"):
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_C_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "safemarkets":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "q8":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "goldenmarkets":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_F_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "ptbanc":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "oinvestsa":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY_SA))

        elif global_var.current_brand_name == "itrader_global":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY_ME))
        else:
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        # TODO: verify that only one client was found

        crm_client_profile.perform_scroll_up()
        # crm_client_profile = crm_client_profile.open_client_id()

        try:
            ClientsPage(self.driver).open_client_id()
        except NoSuchElementException:
            if (global_var.current_brand_name == "finmarket") or (global_var.current_brand_name == "itrader") or (global_var.current_brand_name == "oinvestsa"):
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))
                ClientsPage(self.driver).open_client_id()

            elif global_var.current_brand_name == "highfx":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))
                ClientsPage(self.driver).open_client_id()

        first_name_crm = ClientProfilePage(self.driver).get_first_name()
        last_name_crm = ClientProfilePage(self.driver).get_last_name()
        email = ClientProfilePage(self.driver).get_email_text()

        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME) == first_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME) == last_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL) == email
