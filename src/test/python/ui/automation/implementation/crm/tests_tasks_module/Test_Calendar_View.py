import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants

@pytest.mark.run(order=15)
class CalendarView(BaseTest):

    def test_check_month_tab(self):
        try:
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET))

            calendar_module = CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_month_tab()

            sun_day = calendar_module.get_sunday_text()
            mon_day = calendar_module.get_monday_text()
            tue_day = calendar_module.get_tuesday_text()
            wed_day = calendar_module.get_wednesday_text()
            thu_day = calendar_module.get_thursday_text()
            fri_day = calendar_module.get_friday_text()
            sat_day = calendar_module.get_saturday_text()

            assert sun_day == TaskModuleConstants.SUNDAY
            assert mon_day == TaskModuleConstants.MONDAY
            assert tue_day == TaskModuleConstants.TUESDAY
            assert wed_day == TaskModuleConstants.WEDNESDAY
            assert thu_day == TaskModuleConstants.THURSDAY
            assert fri_day == TaskModuleConstants.FRIDAY
            assert sat_day == TaskModuleConstants.SATURDAY

        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                calendar_module = CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_month_tab()

                sun_day = calendar_module.get_sunday_text()
                mon_day = calendar_module.get_monday_text()
                tue_day = calendar_module.get_tuesday_text()
                wed_day = calendar_module.get_wednesday_text()
                thu_day = calendar_module.get_thursday_text()
                fri_day = calendar_module.get_friday_text()
                sat_day = calendar_module.get_saturday_text()

                assert sun_day == TaskModuleConstants.SUNDAY
                assert mon_day == TaskModuleConstants.MONDAY
                assert tue_day == TaskModuleConstants.TUESDAY
                assert wed_day == TaskModuleConstants.WEDNESDAY
                assert thu_day == TaskModuleConstants.THURSDAY
                assert fri_day == TaskModuleConstants.FRIDAY
                assert sat_day == TaskModuleConstants.SATURDAY
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                calendar_module = CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_month_tab()

                sun_day = calendar_module.get_sunday_text()
                mon_day = calendar_module.get_monday_text()
                tue_day = calendar_module.get_tuesday_text()
                wed_day = calendar_module.get_wednesday_text()
                thu_day = calendar_module.get_thursday_text()
                fri_day = calendar_module.get_friday_text()
                sat_day = calendar_module.get_saturday_text()

                assert sun_day == TaskModuleConstants.SUNDAY
                assert mon_day == TaskModuleConstants.MONDAY
                assert tue_day == TaskModuleConstants.TUESDAY
                assert wed_day == TaskModuleConstants.WEDNESDAY
                assert thu_day == TaskModuleConstants.THURSDAY
                assert fri_day == TaskModuleConstants.FRIDAY
                assert sat_day == TaskModuleConstants.SATURDAY


    def test_check_week_tab(self):
        try:
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET))

            CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_week_tab() \
                .perform_screen_shot()

        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_week_tab() \
                    .perform_screen_shot()
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_week_tab() \
                    .perform_screen_shot()


    def test_check_day_tab(self):
        try:
            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                           self.config.get_value(TestDataConstants.CRM_PASSWORD),
                           self.config.get_value(TestDataConstants.OTP_SECRET))

            calendar_module = CRMHomePage(self.driver)\
                .open_task_module() \
                .open_calendar_view_module() \
                .open_day_tab()

            current_day = calendar_module.get_current_date()
            day_of_week = calendar_module.get_day_of_week()

            assert current_day == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT)
            assert day_of_week == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT_DATE)

        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            try:
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                calendar_module = CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_day_tab()

                current_day = calendar_module.get_current_date()
                day_of_week = calendar_module.get_day_of_week()

                assert current_day == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT)
                assert day_of_week == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT_DATE)
            except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
                TasksPage(self.driver).Sign_Out()
                CRMLoginPage(self.driver) \
                    .open_first_tab_page(self.config.get_value('url')) \
                    .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                               self.config.get_value(TestDataConstants.CRM_PASSWORD))

                calendar_module = CRMHomePage(self.driver) \
                    .open_task_module() \
                    .open_calendar_view_module() \
                    .open_day_tab()

                current_day = calendar_module.get_current_date()
                day_of_week = calendar_module.get_day_of_week()

                assert current_day == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT)
                assert day_of_week == CRMConstants.TODAY_DATE.strftime(CRMConstants.THIRD_FORMAT_DATE)

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def test_check_add_tasks_calendar_view(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()

        calendar_module = task_module.open_calendar_view_module()

        calendar_module.add_new_task().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                    TaskModuleConstants.FIRST_EVENT_TYPE,
                                                    TaskModuleConstants.FIRST_DURATION,
                                                    CRMConstants.SECOND_DATE.strftime(
                                                        CRMConstants.SECOND_FORMAT_DATE),
                                                    CRMConstants.TIME_ZERO,
                                                    TaskModuleConstants.FIRST_ASSIGN_TO,
                                                    self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME],
                                                    self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME],
                                                    TaskModuleConstants.FIRST_PRIORITY,
                                                    TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT
        sleep(2)
        assert task_module.get_task_subject(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]) == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                        LeadsModuleConstants.FIRST_NAME]

        # calendar_module.add_new_task().create_event(TaskModuleConstants.SECOND_EVENT_STATUS,
        #                                             TaskModuleConstants.SECOND_EVENT_TYPE,
        #                                             TaskModuleConstants.SECOND_DURATION,
        #                                             CRMConstants.THIRD_DATE.strftime(
        #                                                 CRMConstants.SECOND_FORMAT_DATE),
        #                                             CRMConstants.THIRD_DATE.strftime(
        #                                                 CRMConstants.FIRST_FORMAT_TIME),
        #                                             TaskModuleConstants.SECOND_ASSIGN_TO,
        #                                             TaskModuleConstants.SECOND_ACCOUNT_NAME,
        #                                             TaskModuleConstants.SECOND_SUBJECT,
        #                                             TaskModuleConstants.SECOND_PRIORITY,
        #                                             TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        #
        # assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT
        #
        # calendar_module.add_new_task().create_event(TaskModuleConstants.THIRD_EVENT_STATUS,
        #                                             TaskModuleConstants.THIRD_EVENT_TYPE,
        #                                             TaskModuleConstants.THIRD_DURATION,
        #                                             CRMConstants.FOURTH_DATE.strftime(
        #                                                 CRMConstants.SECOND_FORMAT_DATE),
        #                                             CRMConstants.FOURTH_DATE.strftime(
        #                                                 CRMConstants.FIRST_FORMAT_TIME),
        #                                             TaskModuleConstants.THIRD_ASSIGN_TO,
        #                                             TaskModuleConstants.THIRD_ACCOUNT_NAME,
        #                                             TaskModuleConstants.THIRD_SUBJECT,
        #                                             TaskModuleConstants.THIRD_PRIORITY,
        #                                             TaskModuleConstants.DESCRIPTION_ADD_EVENT)
        #
        # assert task_module.get_confirm_message_task_module() == TaskModuleConstants.MESSAGE_CREATE_EVENT
        # calendar_module.click_calendar_display(CRMConstants.SECOND_DATE.strftime(CRMConstants.SECOND_FORMAT_TIME)) \
        #     .perform_screen_shot() \
        #     .close_calendar_view()

        # task_module.open_show_all_tab().select_three_records_task_module().perform_mass_delete()
        # task_delete_message = task_module.get_confirm_message_task_module()
        # assert task_delete_message == TaskModuleConstants.MESSAGE_TASK_WAS_DELETED
