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

