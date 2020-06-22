from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI


class TasksEditEventPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def edit_event_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TASKS) \
            .open_tab_list_view_ui(TasksModuleConstantsUI.TAB_ALL)

        """ Search for event """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(
            column=TasksModuleConstantsUI.COLUMN_SUBJECT,
            data=AddDeleteEventConstantsUI.SUBJECT)

        """ Edit Event: event status """
        AddDeleteEventPageUI(self.driver) \
            .add_edit_event(
                row='1',
                list1=AddDeleteEventConstantsUI.LIST_EVENT_STATUS, e_status=AddDeleteEventConstantsUI.EVENT_STATUS_2,
                final_btn=AddDeleteEventConstantsUI.BTN_SAVE)

        """ Search for event """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(
            column=TasksModuleConstantsUI.COLUMN_SUBJECT,
            data=AddDeleteEventConstantsUI.SUBJECT)

        """ Get Event data: event status """
        status = GlobalModulePageUI(self.driver) \
            .get_data_from_list_view_ui(
                TasksModuleConstantsUI.COLUMN_STATUS,
                TasksModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Verify data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status, AddDeleteEventConstantsUI.EVENT_STATUS_2)
