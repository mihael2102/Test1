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
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants


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


    def edit_event(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver).get_account_name()
        MyDashboardPage(self.driver).click_pencil_icon()
        EditEventModule(self.driver).edit_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                                              TaskModuleConstants.SECOND_EVENT_TYPE,
                                              TaskModuleConstants.SECOND_DURATION,
                                              CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                              CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                              TaskModuleConstants.SECOND_ASSIGN_TO,
                                              TaskModuleConstants.SECOND_SUBJECT,
                                              TaskModuleConstants.SECOND_PRIORITY,
                                              TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        MyDashboardPage(self.driver).refresh_page()
        MyDashboardPage(self.driver).enter_account_name(account_name)
        status = MyDashboardPage(self.driver).get_status()
        type = MyDashboardPage(self.driver).get_type()
        time = MyDashboardPage(self.driver).get_time()
        assert status == TaskModuleConstants.SECOND_EVENT_STATUS
        assert type == TaskModuleConstants.SECOND_EVENT_TYPE
        assert time == CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE) + CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME)






