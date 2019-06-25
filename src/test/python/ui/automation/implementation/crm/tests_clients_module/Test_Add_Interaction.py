import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.side_bar.create_event.CreateEvent import CreateEvent
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage


@pytest.mark.run(order=6)
class AddInteraction(BaseTest):

    def test_add_interaction(self):
        crm_client_profile = CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        sleep(2)
        ClientsPage(self.driver).find_client_by_email(
            self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))
        SidebarModules(self.driver)\
            .open_create_event_module() \

        CreateEvent(self.driver).create_event(
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_STATUS),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DURATION),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TIME),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DATE),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_ASSIGN_TO),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_PRIORITY),
                    self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DESCRIPTION))

        confirmation_message = ClientProfilePage(self.driver).get_confirm_message_body()
        assert confirmation_message == CRMConstants.INTERACTION_SUCCESSFULLY
        crm_client_profile.click_ok()

    def test_interaction_search(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        res_count = CRMHomePage(self.driver)\
            .open_task_module()\
            .open_show_all_tab()\
            .find_event_by_subject(TaskModuleConstants.SUBJECT)\
            .get_results_count()

        self.assertGreaterEqual(res_count, 1)
