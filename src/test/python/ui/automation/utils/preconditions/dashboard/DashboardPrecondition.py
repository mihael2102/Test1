from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.DashboardConstants import DashboardConstants

class DashboardPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_dashboard(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        dashboard_page = CRMHomePage(self.driver).open_more_list_modules()\
            .select_dashboard_module_more_list(DashboardConstants.DASHBOARD_MODULE)
        # total_portfolio = dashboard_page.check_total_portfolio()
        balance = dashboard_page.check_balance()
        openpandl = dashboard_page.check_openpandl()

        # assert total_portfolio == DashboardConstants.TOTAL_PORTFOLIO
        assert balance == DashboardConstants.BALANCE
        assert openpandl == DashboardConstants.OPENPL
