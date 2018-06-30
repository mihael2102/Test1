import pytest

from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=13)
class TabTasksModuleCRM(BaseTest):

    def test_check_tab_tasks_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        show_all_tab_name = task_module.get_show_all_tab_text()
        show_mine_tab_name = task_module.get_show_mine_tab_text()
        today_tab_name = task_module.get_today_tab_text()
        this_week_tab_name = task_module.get_this_week_tab_text()
        history_tab_name = task_module.get_history_tab_text()

        assert show_all_tab_name == Config.data.get_data_task_module(TaskModuleConstants.FIRST_TAB)
        assert show_mine_tab_name == Config.data.get_data_task_module(TaskModuleConstants.SECOND_TAB)
        assert today_tab_name == Config.data.get_data_task_module(TaskModuleConstants.THIRD_TAB)
        assert this_week_tab_name == Config.data.get_data_task_module(TaskModuleConstants.FOURTH_TAB)
        assert history_tab_name == Config.data.get_data_task_module(TaskModuleConstants.FIFTH_TAB)
