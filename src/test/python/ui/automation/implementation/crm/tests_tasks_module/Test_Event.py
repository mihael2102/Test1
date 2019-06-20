import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.task_module.EventPrecondition import EventPrecondition
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


@pytest.mark.run(order=14)
class AddEventTaskModule(BaseTest):

    def test_email_icon(self):
        EventPrecondition(self.driver, self.config).test_email_icon()

    def test_sms_icon(self):
        EventPrecondition(self.driver, self.config).test_sms_icon()

    def test_mass_edit_tasks(self):
        EventPrecondition(self.driver, self.config).test_mass_edit_tasks()

    def test_searching_by_columns(self):
        EventPrecondition(self.driver, self.config).test_searching_by_columns()

    def test_sorting_columns(self):
        EventPrecondition(self.driver, self.config).test_sorting_columns()

    def test_add_event(self):
        EventPrecondition(self.driver, self.config).create_first_event()

    def test_edit_event(self):
        EventPrecondition(self.driver, self.config).edit_first_event()

    def test_delete_interaction(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        sleep(2)
        ClientsPage(self.driver).find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                                  TestDataConstants.E_MAIL))
        sleep(2)
        while (ClientProfilePage(self.driver).check_event_exist()):
            ClientProfilePage(self.driver).click_activities_tab()
            try:
                ClientProfilePage(self.driver).open_activities_tab()
                ClientProfilePage(self.driver).click_delete_interaction()
            except:
                ClientProfilePage(self.driver).click_delete_interaction()

        close_activities = ClientProfilePage(self.driver).verify_activities()
        assert close_activities == CRMConstants.NONE_INCLUDED




