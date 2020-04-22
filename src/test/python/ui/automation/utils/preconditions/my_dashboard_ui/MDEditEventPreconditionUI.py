from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.BaseTest import *
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class MDEditEventPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def my_dashboard_edit_event_ui(self):
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
        MyDashboardPage(self.driver)\
            .select_show_all_tab()\
            .enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver)\
            .get_account_name()
        MyDashboardPage(self.driver)\
            .click_pencil_icon()
        EditEventModule(self.driver)\
            .edit_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                        TaskModuleConstants.SECOND_EVENT_TYPE,
                        TaskModuleConstants.SECOND_DURATION,
                        CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                        CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                        TaskModuleConstants.SECOND_ASSIGN_TO,
                        TaskModuleConstants.SECOND_SUBJECT,
                        TaskModuleConstants.SECOND_PRIORITY,
                        TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        MyDashboardPage(self.driver)\
            .refresh_page()
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@name='tradeChartFrame']"))
        MyDashboardPage(self.driver)\
            .select_show_all_tab()\
            .enter_account_name(account_name)
        status = MyDashboardPage(self.driver).get_status()
        task_type = MyDashboardPage(self.driver).get_event_type()
        assert status == TaskModuleConstants.SECOND_EVENT_STATUS
        assert task_type == TaskModuleConstants.SECOND_EVENT_TYPE
