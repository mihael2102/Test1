from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.CRMTaskModule import CRMTaskModuleConstants
from src.main.python.ui.crm.model.main_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class CalendarView(BaseTest):

    def test_check_month_tab(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        calendar_module = CRMHomePage().open_task_module() \
            .open_calendar_view_module() \
            .open_month_tab()

        sun_day = calendar_module.get_sunday_text()
        mon_day = calendar_module.get_monday_text()
        tue_day = calendar_module.get_tuesday_text()
        wed_day = calendar_module.get_wednesday_text()
        thu_day = calendar_module.get_thursday_text()
        fri_day = calendar_module.get_friday_text()
        sat_day = calendar_module.get_saturday_text()

        assert sun_day == CRMTaskModuleConstants.SUNDAY
        assert mon_day == CRMTaskModuleConstants.MONDAY
        assert tue_day == CRMTaskModuleConstants.TUESDAY
        assert wed_day == CRMTaskModuleConstants.WEDNESDAY
        assert thu_day == CRMTaskModuleConstants.THURSDAY
        assert fri_day == CRMTaskModuleConstants.FRIDAY
        assert sat_day == CRMTaskModuleConstants.SATURDAY

    def test_check_week_tab(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_task_module() \
            .open_calendar_view_module() \
            .open_week_tab() \
            .perform_screen_shot()

    def test_check_day_tab(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        calendar_module = CRMHomePage().open_task_module() \
            .open_calendar_view_module() \
            .open_day_tab()

        current_day = calendar_module.get_current_date()
        day_of_week = calendar_module.get_day_of_week()

        assert current_day == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT)
        assert day_of_week == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT_DATE)
