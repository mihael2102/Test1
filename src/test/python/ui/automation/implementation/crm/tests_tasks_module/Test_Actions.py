import pytest

from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.CRMSmsPrecondition import MassSmSPrecondition


@pytest.mark.run(order=20)
class ActionsTask(BaseTest):

    def test_check_send_sms_actions_section(self):
        MassSmSPrecondition().create_first_event()

        task_module = CRMTaskModule()
        phone_number = task_module.open_this_week_tab() \
            .find_event_by_subject(CRMTaskModuleConstants.FIRST_SUBJECT) \
            .open_first_client_profile() \
            .get_phone_text()

        task_module.open_first_tab_page(Config.url_task)

        task_module.find_event_by_subject(CRMTaskModuleConstants.FIRST_SUBJECT) \
            .open_sms_module() \
            .perform_send_sms(phone_number, CRMTaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        message = task_module.open_first_client_profile() \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(CRMTaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .get_sms_text()

        assert message == CRMTaskModuleConstants.DESCRIPTION_SEND_SMS

    def test_check_phone_actions_section(self):
        MassSmSPrecondition().create_first_event()
        task_module = CRMTaskModule()
        task_module.open_this_week_tab() \
            .find_event_by_subject(CRMTaskModuleConstants.FIRST_SUBJECT) \
            .open_call_module() \
            .perform_call_section(Config.data.get_data_task_module(CRMTaskModuleConstants.SECOND_CALL_OUTCOME),
                                  Config.data.get_data_task_module(CRMTaskModuleConstants.SECOND_POSITIVE_OUTCOME),
                                  Config.data.get_data_task_module(CRMTaskModuleConstants.THIRD_NEGATIVE_OUTCOME),
                                  CRMTaskModuleConstants.COMMENTS_CALL_PHONE) \
            .click_submit_button()

        client_status = task_module.open_this_week_tab() \
            .find_event_by_subject(CRMTaskModuleConstants.FIRST_SUBJECT) \
            .open_first_client_profile() \
            .get_client_status()

        assert client_status == Config.data.get_data_task_module(CRMTaskModuleConstants.THIRD_NEGATIVE_OUTCOME)
