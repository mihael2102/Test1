from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.tasks_ui.TasksModuleConstantsUI import TasksModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.EmailConstantsUI import EmailConstantsUI


class TasksEmailPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def send_email_tasks_ui(self):
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

        """ Send Email """
        subject = global_var.current_brand_name + EmailConstantsUI.SUBJECT_TASKS
        GlobalTablePageUI(self.driver) \
            .set_data_column_field(TasksModuleConstantsUI.COLUMN_ACCOUNT_NAME,
                                   TasksModuleConstantsUI.ACCOUNT_NAME) \
            .open_actions_list() \
            .click_email_icon_list_view() \
            .set_text_field(EmailConstantsUI.FIELD_SUBJECT, subject) \
            .set_body_mail(EmailConstantsUI.MESSAGE) \
            .click_send_btn()

        """ Verify successful message """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Search for event """
        # sleep(10)
        # msg = task_module.check_email(brand + CRMConstants.SUBJECT_TASK_MAIL)
        # assert brand + CRMConstants.SUBJECT_TASK_MAIL in msg
