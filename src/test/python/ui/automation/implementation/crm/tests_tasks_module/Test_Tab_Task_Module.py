import pytest

from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=13)
class TabTasksModuleCRM(BaseTest):

    def test_check_tab_tasks_module(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

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

    # def test_check_searching_module(self):
    #     EventPrecondition().create_first_event()
    #
    #     task_module = TaskModule()
    #     task_module.open_show_all_tab().find_event_by_subject(
    #         TaskModuleConstants.FIFTH_SUBJECT)
    #     #
    #     # task_module.perform_searching(TaskModuleConstants.SECOND_EVENT_STATUS,
    #     #                               TaskModuleConstants.SECOND_EVENT_TYPE,
    #     #                               TaskModuleConstants.SECOND_DURATION,
    #     #                               CRMConstants.THIRD_DATE.strftime(
    #     #                                   CRMConstants.SECOND_FORMAT_DATE),
    #     #                               CRMConstants.THIRD_DATE.strftime(
    #     #                                   CRMConstants.FIRST_FORMAT_TIME),
    #     #                               TaskModuleConstants.SECOND_ASSIGN_TO,
    #     #
    #     #                               task_module.perform_screen_shot()
