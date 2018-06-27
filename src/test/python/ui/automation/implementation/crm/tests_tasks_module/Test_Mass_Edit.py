from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.utils.preconditions.task_module.CRMSmsPrecondition import MassSmSPrecondition


class MassEditTaskModule(BaseTest):

    def test_mass_edit_task(self):
        MassSmSPrecondition().create_first_event().create_second_event().create_third_event()

        task_module = CRMTaskModule()
        task_module.open_this_week_tab().find_event_by_subject(
            CRMTaskModuleConstants.FIRST_SUBJECT).select_several_records_task_module() \
            .open_mass_edit_task().perform_mass_edit(CRMTaskModuleConstants.SECOND_EVENT_STATUS,
                                                     CRMTaskModuleConstants.SECOND_EVENT_TYPE,
                                                     CRMTaskModuleConstants.SECOND_DURATION,
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.SECOND_FORMAT_DATE),
                                                     CRMConstants.THIRD_DATE.strftime(
                                                         CRMConstants.FIRST_FORMAT_TIME),
                                                     CRMTaskModuleConstants.SECOND_ASSIGN_TO,
                                                     CRMTaskModuleConstants.SECOND_PRIORITY,
                                                     CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_message_task() == CRMTaskModuleConstants.MESSAGE_TASK_WERE_UPDATED
        task_module.perform_screen_shot()
