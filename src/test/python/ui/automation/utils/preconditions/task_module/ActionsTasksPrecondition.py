from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


class ActionsTasksPrecondition(object):
    def __init__(self) -> None:
        super().__init__()

    def create_first_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                         TaskModuleConstants.SECOND_EVENT_TYPE,
                                                         TaskModuleConstants.SECOND_DURATION,
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.SECOND_ASSIGN_TO,
                                                         TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         TaskModuleConstants.SEVENTH_SUBJECT,
                                                         TaskModuleConstants.SECOND_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        return ActionsTasksPrecondition()

    def create_second_event(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        task_module = CRMHomePage().open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                                         TaskModuleConstants.SECOND_EVENT_TYPE,
                                                         TaskModuleConstants.SECOND_DURATION,
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.THIRD_DATE.strftime(
                                                             CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.SECOND_ASSIGN_TO,
                                                         TaskModuleConstants.FIRST_ACCOUNT_NAME,
                                                         TaskModuleConstants.SEVENTH_SUBJECT,
                                                         TaskModuleConstants.SECOND_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        return ActionsTasksPrecondition()
