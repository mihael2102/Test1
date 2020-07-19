from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage


class MDSmsPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def my_dashboard_sms_ui(self):
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

        """ Check SMS pop up """
        MyDashboardPage(self.driver) \
            .select_show_all_tab() \
            .enter_account_name(CRMConstants.TESTQA) \
            .click_sms_icon()
        pop_up = MyDashboardPage(self.driver) \
            .check_pop_up_send_sms()
        try:
            assert CRMConstants.SEND_SMS in pop_up
        except:
            assert CRMConstants.SERVER_NOT_CONFIGURATE in pop_up
