from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class MDEmailPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def my_dashboard_email_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open My Dashboard module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_MY_DASHBOARD)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@name='tradeChartFrame']"))
        brand = global_var.current_brand_name
        subject = brand + CRMConstants.SUBJECT_TASK_MAIL
        MyDashboardPage(self.driver) \
            .select_show_all_tab() \
            .enter_account_name(CRMConstants.TESTQA) \
            .open_email_actions_section()
        MyDashboardPage(self.driver) \
            .enter_subject_mail(subject) \
            .enter_body_mail(CRMConstants.BODY_LEAD_MAIL) \
            .enter_cc_mail(CRMConstants.CC_EMAIL) \
            .enter_body_mail(CRMConstants.BODY_LEAD_MAIL) \
            .click_send()
        sleep(10)
        msg = TasksPage(self.driver).check_email(subject)
        assert subject in msg
