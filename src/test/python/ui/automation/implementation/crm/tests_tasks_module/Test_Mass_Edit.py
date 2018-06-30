import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.task_module.MassEditPrecondition import MassEditPrecondition


@pytest.mark.run(order=16)
class MassEditTaskModule(BaseTest):

    def test_mass_edit_task(self):
        MassEditPrecondition().create_first_event().create_second_event().create_third_event()

        task_module = TaskModule()
        task_module.open_this_week_tab().find_event_by_subject(
            TaskModuleConstants.FIFTH_SUBJECT).select_several_records_task_module() \
            .open_mass_edit_task().perform_mass_edit(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                     TaskModuleConstants.SECOND_EVENT_TYPE,
                                                     TaskModuleConstants.SECOND_DURATION,
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.SECOND_FORMAT_DATE),
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.FIRST_FORMAT_TIME),
                                                     TaskModuleConstants.SECOND_ASSIGN_TO,
                                                     TaskModuleConstants.SECOND_PRIORITY,
                                                     TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == TaskModuleConstants.MESSAGE_TASK_WERE_UPDATED
        task_module.perform_screen_shot()
