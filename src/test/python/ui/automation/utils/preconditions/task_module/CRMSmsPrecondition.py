from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.modules.tasks_module.CRMTaskModule import CRMTaskModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class MassSmSPrecondition(object):

    def __init__(self) -> None:
        super().__init__()

    def create_first_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(CRMTaskModuleConstants.FIRST_EVENT_STATUS,
                                                         CRMTaskModuleConstants.FIRST_EVENT_TYPE,
                                                         CRMTaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.SECOND_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.SECOND_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         CRMTaskModuleConstants.FIRST_ASSIGN_TO,
                                                         CRMTaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         CRMTaskModuleConstants.FIRST_SUBJECT,
                                                         CRMTaskModuleConstants.FIRST_PRIORITY,
                                                         CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)
        return MassSmSPrecondition()

    def create_second_event(self):
        task_module = CRMTaskModule()
        task_module.open_add_event_module().create_event(CRMTaskModuleConstants.SECOND_EVENT_STATUS,
                                                         CRMTaskModuleConstants.SECOND_EVENT_TYPE,
                                                         CRMTaskModuleConstants.SECOND_DURATION,
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         CRMTaskModuleConstants.SECOND_ASSIGN_TO,
                                                         CRMTaskModuleConstants.SECOND_ACCOUNT_NAME,
                                                         CRMTaskModuleConstants.SECOND_SUBJECT,
                                                         CRMTaskModuleConstants.SECOND_PRIORITY,
                                                         CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        return MassSmSPrecondition()

    def create_third_event(self):
        task_module = CRMTaskModule()
        task_module.open_add_event_module().create_event(CRMTaskModuleConstants.THIRD_EVENT_STATUS,
                                                         CRMTaskModuleConstants.THIRD_EVENT_TYPE,
                                                         CRMTaskModuleConstants.THIRD_DURATION,
                                                         CRMConstants.FOURTH_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.FOURTH_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         CRMTaskModuleConstants.THIRD_ASSIGN_TO,
                                                         CRMTaskModuleConstants.THIRD_ACCOUNT_NAME,
                                                         CRMTaskModuleConstants.THIRD_SUBJECT,
                                                         CRMTaskModuleConstants.THIRD_PRIORITY,
                                                         CRMTaskModuleConstants.DESCRIPTION_ADD_EVENT)

        return MassSmSPrecondition()
