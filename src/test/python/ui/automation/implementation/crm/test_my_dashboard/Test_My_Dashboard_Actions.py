from src.main.python.ui.crm.model.constants.MyDashboardConstants import MyDashboardConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.ActionsTasksPrecondition import \
    ActionsTasksPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.MassSmsPrecondition import MassSmSPrecondition


class MyDashboardActions(BaseTest):

    def test_check_send_sms_actions_section(self):
        ActionsTasksPrecondition().create_first_event()

        dashboard_module = CRMHomePage().refresh_page().open_client_module().open_more_list_modules() \
            .select_my_dashboard_module_more_list(MyDashboardConstants.MY_DASHBOARD_MODULE)

        phone_number = dashboard_module.perform_scroll_down().open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_first_client_profile() \
            .get_phone_text()

        dashboard_module.came_back_on_previous_page() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_sms_module_my_dashboard() \
            .perform_send_sms(phone_number, TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        message = dashboard_module.open_first_client_profile() \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .get_sms_text()

        assert message == TaskModuleConstants.DESCRIPTION_SEND_SMS

    def test_check_phone_actions_section(self):
        MassSmSPrecondition().create_first_event()

        dashboard_module = CRMHomePage().refresh_page().open_client_module().open_more_list_modules() \
            .select_my_dashboard_module_more_list(MyDashboardConstants.MY_DASHBOARD_MODULE)

        dashboard_module.perform_scroll_down().open_call_module_my_dashboard() \
            .perform_call_section(Config.data.get_data_task_module(TaskModuleConstants.SECOND_CALL_OUTCOME),
                                  Config.data.get_data_task_module(TaskModuleConstants.SECOND_POSITIVE_OUTCOME),
                                  Config.data.get_data_task_module(TaskModuleConstants.THIRD_NEGATIVE_OUTCOME),
                                  TaskModuleConstants.COMMENTS_CALL_PHONE) \
            .click_submit_button()

        client_status = dashboard_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_first_client_profile() \
            .get_client_status()

        assert client_status == Config.data.get_data_task_module(TaskModuleConstants.THIRD_NEGATIVE_OUTCOME)
