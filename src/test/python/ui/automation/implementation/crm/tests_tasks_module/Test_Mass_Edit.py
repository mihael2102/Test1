from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.MassEditPrecondition import MassEditPrecondition


class MassEditTaskModule(BaseTest):

    def test_mass_edit_task(self):
        MassEditPrecondition().create_first_event()\
            .create_second_event()\
            .create_third_event()

        task_module = TasksPage()
        task_module.open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.FIFTH_SUBJECT).select_three_records_task_module() \
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

        assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_TASK_WERE_UPDATED
        task_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.FIFTH_SUBJECT) \
            .perform_screen_shot()
