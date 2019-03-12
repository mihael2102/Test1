from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from time import sleep
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.mt4.credit_out.MT4CreditOutModule import MT4CreditOutModule
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.my_dashboard.MyDashboardPage import MyDashboardPage


class MyDashboardPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_mydashboard_loading(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules()\
                                .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).check_latest_sales_loaded() \
                                    .check_task_section_contains_record() \
                                    .check_client_segmentation_contains_record()
