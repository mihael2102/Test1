from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage


class MDSortingPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def sorting_columns_ui(self):
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

        """ Sorting columns """
        MyDashboardPage(self.driver) \
            .select_show_all_tab()

        my_dashboard_page = MyDashboardPage(self.driver)
        type1 = my_dashboard_page\
            .get_event_type()
        my_dashboard_page\
            .sort_by_type()
        type2 = my_dashboard_page\
            .get_event_type()

        count = 0
        while type1 != type2:
            my_dashboard_page \
                .sort_by_type()
            type2 = my_dashboard_page \
                .get_event_type()
            count += 1
            if count == 3:
                break

        my_dashboard_page\
            .sort_by_status()
        status1 = my_dashboard_page\
            .get_status()
        my_dashboard_page\
            .sort_by_status()
        status2 = my_dashboard_page\
            .get_status()

        count = 0
        while status1 != status2:
            my_dashboard_page \
                .sort_by_status()
            status2 = my_dashboard_page \
                .get_status()
            count += 1
            if count == 3:
                break
