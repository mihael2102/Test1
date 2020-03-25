from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassEditPageUI import MassEditPageUI


class TasksMassEditPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_edit_tasks_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                new_design=0,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Tasks module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_TASKS) \
            .open_tab_list_view_ui(TasksModuleConstantsUI.TAB_ALL)

        """ Select records for Mass Edit """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(TasksModuleConstantsUI.COLUMN_ACCOUNT_NAME,
                                   TasksModuleConstantsUI.ACCOUNT_NAME) \
            .select_all_records_checkbox() \
            .click_mass_action_btn(MassActionsConstantsUI.MASS_EDIT)

        """ Mass Edit """
        MassEditPageUI(self.driver) \
            .select_field_to_edit(MassActionsConstantsUI.LIST_EVENT_TYPE) \
            .select_from_list(MassActionsConstantsUI.LIST_EVENT_TYPE, MassActionsConstantsUI.EVENT_TYPE) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_ASSIGNED_TO) \
            .select_from_list(MassActionsConstantsUI.FIELD_ASSIGNED_TO, MassActionsConstantsUI.USER_NAME) \
            .select_field_to_edit(MassActionsConstantsUI.LIST_PRIORITY) \
            .select_from_list(MassActionsConstantsUI.LIST_PRIORITY, MassActionsConstantsUI.PRIORITY) \
            .click_save_changes_btn()

        """ Check confirmation message and updated data in table """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .refresh_page_ui() \
            .set_data_column_field(TasksModuleConstantsUI.COLUMN_ACCOUNT_NAME,
                                   TasksModuleConstantsUI.ACCOUNT_NAME) \
            .global_data_checker_new_ui(MassActionsConstantsUI.EVENT_TYPE) \
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME) \
            .global_data_checker_new_ui(MassActionsConstantsUI.PRIORITY)
