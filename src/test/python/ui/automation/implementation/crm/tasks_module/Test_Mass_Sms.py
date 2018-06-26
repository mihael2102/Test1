import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.CRMSmsPrecondition import MassSmSPrecondition


@pytest.mark.run(order=5)
class MassSmsTaskModule(BaseTest):

    def test_perform_mass_sms_task_module(self):
        MassSmSPrecondition().create_first_event().create_second_event().create_third_event()

        task_module = CRMTaskModule()
        task_module.open_this_week_tab().select_several_records_task_module() \
            .open_mass_sms_module().perform_mass_sms(CRMConstants.PHONE, CRMConstants.MESSAGE_MASS_SMS) \
            .click_send_button()

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_SMS_SUCCESSFULLY

        CRMLoginPage().open_first_tab_page(Config.url_task)
        message = task_module.open_first_client_profile() \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(CRMConstants.MESSAGE_MASS_SMS) \
            .get_sms_text()

        assert message == CRMConstants.MESSAGE_MASS_SMS
        CRMLoginPage().open_first_tab_page(Config.url_task)

        second_message = task_module.open_second_client_profile() \
            .perform_scroll_down() \
            .open_sms_view_module(CRMConstants.MESSAGE_MASS_SMS) \
            .get_sms_text()
        assert second_message == CRMConstants.MESSAGE_MASS_SMS
        CRMLoginPage().open_first_tab_page(Config.url_task)

        third_message = task_module.open_third_client_profile() \
            .perform_scroll_down() \
            .open_sms_view_module(CRMConstants.MESSAGE_MASS_SMS) \
            .get_sms_text()
        assert third_message == CRMConstants.MESSAGE_MASS_SMS
