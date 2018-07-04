import pytest

from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.task_module.MassDeletePrecondition import MassDeletePrecondition


@pytest.mark.run(order=17)
class MassDeleteTaskModule(BaseTest):

    def test_mass_delete_task_module(self):
        MassDeletePrecondition().create_first_event().create_second_event().create_third_event()

        task_module = TaskModule()
        task_module.open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.SIXTH_SUBJECT).select_three_records_task_module().perform_mass_delete()
        task_delete_message = task_module.get_message_task()

        assert task_delete_message == TaskModuleConstants.MESSAGE_TASK_WAS_DELETED
