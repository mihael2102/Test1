import pytest
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksSearchingColumnsPreconditionUI import \
    TasksSearchingColumnsPreconditionUI
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksAddEventPreconditionUI import \
    TasksAddEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksDeleteEventPreconditionUI import \
    TasksDeleteEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksMassEditPreconditionUI import \
    TasksMassEditPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksEmailPreconditionUI import \
    TasksEmailPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksEditEventPreconditionUI import \
    TasksEditEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.tasks_module_ui.TasksSortingColumnsPreconditionUI import \
    TasksSortingColumnsPreconditionUI


@pytest.mark.run(order=26)
class TestTasksModuleUI(BaseTest):

    def test_tasks_searching_columns_ui(self):
        TasksSearchingColumnsPreconditionUI(self.driver, self.config).tasks_searching_columns_ui()

    def test_tasks_sorting_columns_ui(self):
        TasksSortingColumnsPreconditionUI(self.driver, self.config).tasks_sorting_columns_ui()

    def test_add_event_ui(self):
        TasksAddEventPreconditionUI(self.driver, self.config).add_event_ui()

    def test_edit_event_ui(self):
        TasksEditEventPreconditionUI(self.driver, self.config).edit_event_ui()

    def test_delete_event_ui(self):
        TasksDeleteEventPreconditionUI(self.driver, self.config).delete_event_ui()

    def test_tasks_mass_edit(self):
        TasksMassEditPreconditionUI(self.driver, self.config).mass_edit_tasks_ui()

    def test_tasks_email_ui(self):
        TasksEmailPreconditionUI(self.driver, self.config).send_email_tasks_ui()
