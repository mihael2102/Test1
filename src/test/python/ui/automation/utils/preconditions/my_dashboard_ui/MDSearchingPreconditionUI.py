from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage


class MDSearchingPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def searching_columns_ui(self):
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

        """ Searching columns """
        MyDashboardPage(self.driver) \
            .select_show_all_tab() \
            .enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver) \
            .get_account_name()
        type = MyDashboardPage(self.driver) \
            .get_event_type()
        status = MyDashboardPage(self.driver) \
            .get_status()
        country = MyDashboardPage(self.driver) \
            .get_country()
        assigned_to = MyDashboardPage(self.driver) \
            .get_assigned_to()
        created_by = MyDashboardPage(self.driver) \
            .get_created_by()

        MyDashboardPage(self.driver) \
            .refresh_page()

        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@name='tradeChartFrame']"))

        MyDashboardPage(self.driver) \
            .select_show_all_tab() \
            .enter_account_name(account_name) \
            .enter_event_type(type) \
            .enter_status(status) \
            .enter_country(country) \
            .enter_assigned_to(assigned_to) \
            .enter_created_by(created_by)
        return_account_name = MyDashboardPage(self.driver) \
            .get_account_name()

        assert return_account_name == account_name
