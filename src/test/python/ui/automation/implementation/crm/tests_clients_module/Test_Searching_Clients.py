import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants.ClientsModuleConstants import ClientsModuleConstants
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.constants.SearchModuleConstants import SearchModuleConstants
from src.main.python.ui.crm.model.pages.clients.ClientsModulePage import ClientsModulePage
from src.main.python.ui.crm.model.pages.crm_base_page.ModuleSearchPage import ModuleSearchPage


@pytest.mark.run(order=3)
class SearchingClientsTestCRM(BaseTest):

    def test_make_searching_client_module(self):
        """
           Test depends on test 'test_perform_convert_lead'
        """

        """ Login CRM """
        crm_client_profile = CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \

        if (global_var.current_brand_name == "royal_cfds") or (global_var.current_brand_name == "swiftcfd") \
                or (global_var.current_brand_name == "b-finance"):
                sleep(15)
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "4xfx" or global_var.current_brand_name == "gigafx":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_C_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif (global_var.current_brand_name == "safemarkets") or (global_var.current_brand_name == "uft") or \
                (global_var.current_brand_name == "q8"):
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_NEW),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "goldenmarkets":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS_B_TEST),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif global_var.current_brand_name == "ptbanc":
                ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        elif (global_var.current_brand_name == "uprofx") or (global_var.current_brand_name == "xtraderfx"):
            ClientsPage(self.driver).enter_email(
                self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        else:
            ClientsPage(self.driver).perform_searching(
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                    self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        """ Verify only one client was found """
        crm_client_profile.perform_scroll_up()
        crm_client_profile = crm_client_profile.open_client_id()

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        email = crm_client_profile.get_email_text()

        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_NAME) == first_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME) == last_name_crm
        assert self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL) == email

    def test_search_client_magnifying_glass(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_CLIENTS)\
            .open_tab_list_view(ClientsModuleConstants.TAB_ALL)

        """ Get client's data from the first row of list view """
        crm_id = ClientsModulePage(self.driver)\
            .get_client_crm_id_list_view(ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_status = CRMBaseMethodsPage(self.driver)\
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_CLIENT_STATUS,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        email = CRMBaseMethodsPage(self.driver)\
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_EMAIL,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_name = CRMBaseMethodsPage(self.driver)\
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_CLIENT_NAME,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_ASSIGNED_TO,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        country = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_COUNTRY,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Searching via 'Search in...' button (magnifying glass) by CRM ID """
        CRMBaseMethodsPage(self.driver) \
            .click_magnifying_glass_btn()\
            .set_search_for_field(crm_id)\
            .select_in_list(SearchModuleConstants.IN_CRM_ID)\
            .click_search_now_btn()
        CRMBaseMethodsPage(self.driver) \
            .global_data_checker(crm_id)

        """ Searching via 'Search in...' button (magnifying glass) by CLIENT STATUS """
        ModuleSearchPage(self.driver) \
            .set_search_for_field(client_status) \
            .select_in_list(SearchModuleConstants.IN_CLIENT_STATUS) \
            .click_search_now_btn()
        CRMBaseMethodsPage(self.driver) \
            .global_data_checker(client_status)

        """ Searching via 'Search in...' button (magnifying glass) by EMAIL """
        """ In case email addresses are hidden under 'Send mail' label, don't execute searching """
        if email.lower() != "send mail":
            ModuleSearchPage(self.driver) \
                .set_search_for_field(email) \
                .select_in_list(SearchModuleConstants.IN_EMAIL) \
                .click_search_now_btn()
            CRMBaseMethodsPage(self.driver) \
                .global_data_checker(email)

        """ Searching via 'Search in...' button (magnifying glass) by CLIENT NAME """
        ModuleSearchPage(self.driver) \
            .set_search_for_field(client_name) \
            .select_in_list(SearchModuleConstants.IN_CLIENT_NAME) \
            .click_search_now_btn()
        CRMBaseMethodsPage(self.driver) \
            .global_data_checker(client_name)

        """ Searching via 'Search in...' button (magnifying glass) by ASSIGNED TO """
        ModuleSearchPage(self.driver) \
            .set_search_for_field(assigned_to) \
            .select_in_list(SearchModuleConstants.IN_ASSIGNED_TO) \
            .click_search_now_btn()
        CRMBaseMethodsPage(self.driver) \
            .global_data_checker(assigned_to)

        """ Searching via 'Search in...' button (magnifying glass) by COUNTRY """
        ModuleSearchPage(self.driver) \
            .set_search_for_field(country) \
            .select_in_list(SearchModuleConstants.IN_COUNTRY) \
            .click_search_now_btn()
        CRMBaseMethodsPage(self.driver) \
            .global_data_checker(country)
