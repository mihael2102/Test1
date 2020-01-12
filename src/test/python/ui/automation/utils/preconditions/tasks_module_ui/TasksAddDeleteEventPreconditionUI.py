from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI


class TasksAddDeleteEventPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def add_delete_event_ui(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TASKS) \
            .open_tab_list_view_ui(TasksModuleConstantsUI.TAB_ALL)

        """ Create Event """
        AddDeleteEventPageUI(self.driver)\
            .click_add_event_btn() \
            .select_pick_list_item(pick_list=AddDeleteEventConstantsUI.PICK_LIST_EVENT_STATUS,
                                   item=AddDeleteEventConstantsUI.EVENT_STATUS) \
            .select_pick_list_item(pick_list=AddDeleteEventConstantsUI.PICK_LIST_EVENT_TYPE,
                                   item=AddDeleteEventConstantsUI.EVENT_TYPE) \
            .select_pick_list_item(pick_list=AddDeleteEventConstantsUI.PICK_LIST_DURATION,
                                   item=AddDeleteEventConstantsUI.DURATION) \
            .select_pick_list_item(pick_list=AddDeleteEventConstantsUI.PICK_LIST_ASSIGN_TO,
                                   item=AddDeleteEventConstantsUI.ASSIGN_TO) \
            .set_attached_to(AddDeleteEventConstantsUI.ATTACHED_TO) \
            .set_text_field(field=AddDeleteEventConstantsUI.FIELD_SUBJECT,
                            text=AddDeleteEventConstantsUI.SUBJECT) \
            .select_pick_list_item(pick_list=AddDeleteEventConstantsUI.PICK_LIST_PRIORITY,
                                   item=AddDeleteEventConstantsUI.PRIORITY) \
            .set_text_field(field=AddDeleteEventConstantsUI.FIELD_COMMENTS,
                            text=AddDeleteEventConstantsUI.COMMENTS) \
            .click_save()

        """ Verify successful message """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Search for event """
        GlobalTablePageUI(self.driver) \
            .set_data_column_field(column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                                   data=AddDeleteEventConstantsUI.SUBJECT)

        """ Verify correct data found """
        GlobalTablePageUI(self.driver) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.EVENT_STATUS) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.EVENT_TYPE) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.ASSIGN_TO) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.ATTACHED_TO) \
            .global_data_checker_new_ui(AddDeleteEventConstantsUI.SUBJECT)

        """ Verify only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver) \
            .get_number_records()
        assert number_records == 1

        """ Delete Event from table """
        GlobalTablePageUI(self.driver) \
            .open_actions_list() \
            .click_delete_icon_list_view(TasksModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1) \
            .approve_deleting() \
            .verify_success_message() \
            .click_ok()

        """ Search for event and Verify data not found """
        GlobalTablePageUI(self.driver) \
            .set_data_column_field(column=TasksModuleConstantsUI.COLUMN_SUBJECT,
                                   data=AddDeleteEventConstantsUI.SUBJECT) \
            .verify_data_not_found()
