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
class TestClientsListView(BaseTest):

    def test_searching_clients_module(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_CLIENTS) \
            .open_tab_list_view(ClientsModuleConstants.TAB_ALL)

        """ Get client's data from the first row of list view """
        crm_id = ClientsModulePage(self.driver) \
            .get_client_crm_id_list_view(ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_status = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_CLIENT_STATUS,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        email = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_EMAIL,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_name = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_CLIENT_NAME,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_ASSIGNED_TO,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        country = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_vtiger(column=ClientsModuleConstants.COLUMN_COUNTRY,
                                            row=ClientsModuleConstants.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """

