import pytest
from _pytest.config import Config

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=19)
class AddNewTaskCalendarView(BaseTest):

    def test_check_add_tasks_calendar_view(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        calendar_module = task_module.open_calendar_view_module()

        calendar_module.add_new_task().create_event(CRMTaskModuleConstants.FIRST_EVENT_STATUS,
                                                    CRMTaskModuleConstants.FIRST_EVENT_TYPE,
                                                    CRMTaskModuleConstants.FIRST_DURATION,
                                                    CRMConstants.SECOND_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.SECOND_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    CRMTaskModuleConstants.FIRST_ASSIGN_TO,
                                                    CRMTaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                    CRMTaskModuleConstants.FIRST_SUBJECT,
                                                    CRMTaskModuleConstants.FIRST_PRIORITY,
                                                    CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_CREATE_EVENT

        calendar_module.add_new_task().create_event(CRMTaskModuleConstants.SECOND_EVENT_STATUS,
                                                    CRMTaskModuleConstants.SECOND_EVENT_TYPE,
                                                    CRMTaskModuleConstants.SECOND_DURATION,
                                                    CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    CRMTaskModuleConstants.SECOND_ASSIGN_TO,
                                                    CRMTaskModuleConstants.SECOND_ACCOUNT_NAME,
                                                    CRMTaskModuleConstants.SECOND_SUBJECT,
                                                    CRMTaskModuleConstants.SECOND_PRIORITY,
                                                    CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_CREATE_EVENT

        calendar_module.add_new_task().create_event(CRMTaskModuleConstants.THIRD_EVENT_STATUS,
                                                    CRMTaskModuleConstants.THIRD_EVENT_TYPE,
                                                    CRMTaskModuleConstants.THIRD_DURATION,
                                                    CRMConstants.FOURTH_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.FOURTH_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                    CRMTaskModuleConstants.THIRD_ASSIGN_TO,
                                                    CRMTaskModuleConstants.THIRD_ACCOUNT_NAME,
                                                    CRMTaskModuleConstants.THIRD_SUBJECT,
                                                    CRMTaskModuleConstants.THIRD_PRIORITY,
                                                    CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_CREATE_EVENT
        calendar_module.click_calendar_display(CRMConstants.SECOND_DATE.strftime(CRMConstants.SECOND_FORMAT_TIME)) \
            .perform_screen_shot() \
            .close_calendar_view()

        task_module.open_this_week_tab().select_several_records_task_module().perform_mass_delete()
        task_delete_message = task_module.get_message_task()
        assert task_delete_message == CRMTaskModuleConstants.MESSAGE_TASK_WAS_DELETED
