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
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage

@pytest.mark.run(order=14)
class AddEventTaskModule(BaseTest):

    def test_add_event(self):
        try:
            EventPrecondition(self.driver, self.config).create_first_event()
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                TasksPage(self.driver).Sign_Out()
                EventPrecondition(self.driver, self.config).create_first_event()
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                TasksPage(self.driver).Sign_Out()
                EventPrecondition(self.driver, self.config).create_first_event()

        # Assert is in method 'create_first_event()'. So need to place it here after refactoring

    def test_edit_event(self):
        try:
            EventPrecondition(self.driver, self.config).edit_first_event()
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                TasksPage(self.driver).Sign_Out()
                EventPrecondition(self.driver, self.config).edit_first_event()
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                TasksPage(self.driver).Sign_Out()
                EventPrecondition(self.driver, self.config).edit_first_event()
        # Assert is in method 'edit_first_event()'. So need to place it here after refactoring

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
            ClientProfilePage(self.driver).click_activities_tab() \
                                          .open_activities_tab() \
                                          .click_delete_interaction() \
                                          .verify_delete_interaction_message(CRMConstants.DELETE_INTERACTION_MESSAGE) \
                                          .confirm_delete_interaction() \
                                          .interaction_successfully_deleted_message(CRMConstants.INTERACTION_DELETED_MESSAGE)

