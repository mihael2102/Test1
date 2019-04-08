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
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule


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
        MyDashboardPage(self.driver).select_show_all_tab()
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
        MyDashboardPage(self.driver).select_show_all_tab()
        MyDashboardPage(self.driver).enter_account_name(account_name)
        status = MyDashboardPage(self.driver).get_status()
        type = MyDashboardPage(self.driver).get_type()
        assert status == TaskModuleConstants.SECOND_EVENT_STATUS
        assert type == TaskModuleConstants.SECOND_EVENT_TYPE

    def email_icon(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).select_show_all_tab()
        MyDashboardPage(self.driver).enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver).get_account_name()
        MyDashboardPage(self.driver).open_email_actions_section()
        MyDashboardPage(self.driver).enter_subject_mail(CRMConstants.SUBJECT_TASK_MAIL)
        MyDashboardPage(self.driver).enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        MyDashboardPage(self.driver).enter_cc_mail(CRMConstants.CC_EMAIL)
        MyDashboardPage(self.driver).enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        MyDashboardPage(self.driver).click_send()
        sleep(10)
        msg = TasksPage(self.driver).check_email(CRMConstants.SUBJECT_TASK_MAIL)
        assert CRMConstants.SUBJECT_TASK_MAIL in msg

    def sms_icon(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).select_show_all_tab()
        MyDashboardPage(self.driver).enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver).get_account_name()
        MyDashboardPage(self.driver).click_sms_icon()
        pop_up = MyDashboardPage(self.driver).check_pop_up_send_sms()
        try:
            assert CRMConstants.SEND_SMS in pop_up
        except:
            assert CRMConstants.SERVER_NOT_CONFIGURATE in pop_up

    def test_searching_by_columns(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).select_show_all_tab()
        MyDashboardPage(self.driver).enter_account_name(CRMConstants.TESTQA)
        account_name = MyDashboardPage(self.driver).get_account_name()
        type = MyDashboardPage(self.driver).get_type()
        status = MyDashboardPage(self.driver).get_status()
        # account_status = MyDashboardPage(self.driver).get_account_status()
        country = MyDashboardPage(self.driver).get_country()
        assigned_to = MyDashboardPage(self.driver).get_assigned_to()
        created_by = MyDashboardPage(self.driver).get_created_by()
        local_time = MyDashboardPage(self.driver).get_local_time()
        # balance = MyDashboardPage(self.driver).get_balance()
        # total_p_l = MyDashboardPage(self.driver).get_total_p_l()
        # priority = MyDashboardPage(self.driver).get_priority()
        # subject = MyDashboardPage(self.driver).get_subject()

        MyDashboardPage(self.driver).refresh_page()

        MyDashboardPage(self.driver).enter_account_name(account_name) \
            .enter_event_type(type) \
            .enter_status(status) \
            .enter_country(country) \
            .enter_assigned_to(assigned_to) \
            .enter_created_by(created_by) \
            .enter_local_time(local_time) \


        return_account_name = MyDashboardPage(self.driver).get_account_name()

        assert return_account_name == account_name

    def test_sorting_columns(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_more_list_modules() \
            .select_my_dashboard_module_more_list(CRMConstants.MYDASHBOARD_MODULE)
        MyDashboardPage(self.driver).select_show_all_tab()
        type1 = MyDashboardPage(self.driver).get_type()
        MyDashboardPage(self.driver).sort_by_type()
        type2 = MyDashboardPage(self.driver).get_type()
        assert type1 != type2
        MyDashboardPage(self.driver).sort_by_status()
        status1 = MyDashboardPage(self.driver).get_status()
        MyDashboardPage(self.driver).sort_by_status()
        status2 = MyDashboardPage(self.driver).get_status()
        assert status1 != status2
