from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class TasksSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def tasks_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                self.config.get_value('url'),
                self.config.get_value(TestDataConstants.USER_NAME),
                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TASKS) \
            .open_tab_list_view_ui(TasksModuleConstantsUI.TAB_ALL)

        """ Get task data from the first row of list view """
        event_type = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TasksModuleConstantsUI.COLUMN_EVENT_TYPE,
                                        row=TasksModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        status = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TasksModuleConstantsUI.COLUMN_STATUS,
                                        row=TasksModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        account_name = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=TasksModuleConstantsUI.COLUMN_ACCOUNT_NAME,
                                        row=TasksModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if event_type:
            search\
                .select_data_column_field(column=TasksModuleConstantsUI.COLUMN_EVENT_TYPE,
                                          data=event_type)
        if status:
            search\
                .select_data_column_field(column=TasksModuleConstantsUI.COLUMN_STATUS,
                                          data=status)
        if account_name:
            search\
                .set_data_column_field(column=TasksModuleConstantsUI.COLUMN_ACCOUNT_NAME,
                                       data=account_name)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if event_type:
            result\
                .global_data_checker_new_ui(event_type)
        if status:
            result\
                .global_data_checker_new_ui(status)
        if account_name:
            result\
                .global_data_checker_new_ui(account_name)
