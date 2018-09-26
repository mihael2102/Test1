import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage


@pytest.mark.run(order=6)
class AddInteraction(BaseTest):

    def test_add_interaction(self):
        crm_client_profile = CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CLIENT_STATUS),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                               self.config.get_data_client(TestDataConstants.CLIENT_ONE,TestDataConstants.FIRST_COUNTRY))

        crm_client_profile.perform_scroll_up()
        crm_client_profile = crm_client_profile.open_client_id()

        SidebarModules(self.driver)\
            .open_create_event_module() \
            .create_event(self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_STATUS),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DURATION),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TIME),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DATE),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_ASSIGN_TO),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_PRIORITY),
                          self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_DESCRIPTION))

        confirmation_message = crm_client_profile.get_confirm_message()
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
            .find_event_by_subject(self.config.get_value(TaskModuleConstants.EVENT1, TaskModuleConstants.EVENT_TYPE))\
            .get_results_count()

        self.assertGreaterEqual(res_count, 1)

