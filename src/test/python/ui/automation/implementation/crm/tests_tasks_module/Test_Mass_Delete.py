from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.task_module.CRMSmsPrecondition import MassSmSPrecondition


class MassDeleteTaskModule(BaseTest):

    def test_mass_delete_task_module(self):
        MassSmSPrecondition().create_first_event().create_second_event().create_third_event()
        task_module = CRMTaskModule()
        task_module.open_this_week_tab().find_event_by_subject(
            CRMTaskModuleConstants.FIRST_SUBJECT).select_several_records_task_module().perform_mass_delete()
        task_delete_message = task_module.get_message_task()

        assert task_delete_message == CRMTaskModuleConstants.MESSAGE_TASK_WAS_DELETED
