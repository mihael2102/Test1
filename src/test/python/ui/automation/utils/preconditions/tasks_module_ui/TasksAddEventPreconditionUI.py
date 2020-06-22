from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI


class TasksAddEventPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def add_event_ui(self):
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

        """ Create Event """
        AddDeleteEventPageUI(self.driver)\
            .add_edit_event(
                btn_event=1,
                list1=AddDeleteEventConstantsUI.LIST_EVENT_STATUS, e_status=AddDeleteEventConstantsUI.EVENT_STATUS,
                list2=AddDeleteEventConstantsUI.LIST_EVENT_TYPE, e_type=AddDeleteEventConstantsUI.EVENT_TYPE,
                list3=AddDeleteEventConstantsUI.LIST_DURATION, duration=AddDeleteEventConstantsUI.DURATION,
                list4=AddDeleteEventConstantsUI.LIST_ASSIGN_TO, assign_to=AddDeleteEventConstantsUI.ASSIGN_TO,
                attached_to=AddDeleteEventConstantsUI.ATTACHED_TO,
                field1=AddDeleteEventConstantsUI.FIELD_SUBJECT, subject=AddDeleteEventConstantsUI.SUBJECT,
                list5=AddDeleteEventConstantsUI.LIST_PRIORITY, priority=AddDeleteEventConstantsUI.PRIORITY,
                comments=AddDeleteEventConstantsUI.COMMENTS, final_btn=AddDeleteEventConstantsUI.BTN_SAVE)

        """ Search for event """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                                   data=AddDeleteEventConstantsUI.SUBJECT)

        """ Verify correct data found """
        GlobalModulePageUI(self.driver) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.EVENT_STATUS) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.EVENT_TYPE) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.ASSIGN_TO) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.ATTACHED_TO) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.SUBJECT)

        """ Verify only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver) \
            .get_number_records()
        assert number_records == 1
