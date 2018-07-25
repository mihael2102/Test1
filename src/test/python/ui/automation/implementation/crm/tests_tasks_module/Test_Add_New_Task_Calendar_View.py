import pytest
from _pytest.config import Config

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=19)
class AddNewTaskCalendarView(BaseTest):

    def test_check_add_tasks_calendar_view(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        calendar_module = task_module.open_calendar_view_module()

        calendar_module.add_new_task().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                    TaskModuleConstants.FIRST_EVENT_TYPE,
                                                    TaskModuleConstants.FIRST_DURATION,
                                                    CRMConstants.SECOND_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.SECOND_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    TaskModuleConstants.FIRST_ASSIGN_TO,
                                                    TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                    TaskModuleConstants.FIRST_SUBJECT,
                                                    TaskModuleConstants.FIRST_PRIORITY,
                                                    TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT

        calendar_module.add_new_task().create_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                    TaskModuleConstants.SECOND_EVENT_TYPE,
                                                    TaskModuleConstants.SECOND_DURATION,
                                                    CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    TaskModuleConstants.SECOND_ASSIGN_TO,
                                                    TaskModuleConstants.SECOND_ACCOUNT_NAME,
                                                    TaskModuleConstants.SECOND_SUBJECT,
                                                    TaskModuleConstants.SECOND_PRIORITY,
                                                    TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT

        calendar_module.add_new_task().create_event(TaskModuleConstants.THIRD_EVENT_STATUS,
                                                    TaskModuleConstants.THIRD_EVENT_TYPE,
                                                    TaskModuleConstants.THIRD_DURATION,
                                                    CRMConstants.FOURTH_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.FOURTH_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    TaskModuleConstants.THIRD_ASSIGN_TO,
                                                    TaskModuleConstants.THIRD_ACCOUNT_NAME,
                                                    TaskModuleConstants.THIRD_SUBJECT,
                                                    TaskModuleConstants.THIRD_PRIORITY,
                                                    TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT
        calendar_module.click_calendar_display(CRMConstants.SECOND_DATE.strftime(CRMConstants.SECOND_FORMAT_TIME)) \
            .perform_screen_shot() \
            .close_calendar_view()

        task_module.open_show_all_tab().select_three_records_task_module().perform_mass_delete()
        task_delete_message = task_module.get_confirm_message_task_module()
        assert task_delete_message == TaskModuleConstants.MESSAGE_TASK_WAS_DELETED
