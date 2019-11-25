from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.tasks_module.EditEventModule import EditEventModule
from src.test.python.ui.automation.BaseTest import *
import pytest
from src.main.python.ui.crm.model.modules.tasks_module.MassEditTaskModule import MassEditTaskModule
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class EventPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def test_sorting_columns(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.open_show_all_tab()
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_EVENT_TYPE)
        type1 = task_module.get_first_column_frow_text()
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_EVENT_TYPE)
        type2 = task_module.get_first_column_frow_text()
        assert type1 != type2
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_STATUS)
        status1 = task_module.get_second_column_frow_text()
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_STATUS)
        status2 = task_module.get_second_column_frow_text()
        assert status1 != status2
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_ACCOUNT_NAME)
        account_name1 = task_module.get_third_column_frow_text()
        task_module.click_column_title(TaskModuleConstants.COLUMN_TITLE_ACCOUNT_NAME)
        account_name2 = task_module.get_third_column_frow_text()
        assert account_name1 != account_name2

    def test_email_icon(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        mail_subject = global_var.current_brand_name + CRMConstants.SUBJECT_TASK_MAIL
        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.open_show_all_tab()
        task_module.search_account_name(CRMConstants.TESTQA)
        sleep(1)
        task_module.open_email_actions_section()
        task_module.enter_subject_mail(mail_subject)
        task_module.enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        task_module.enter_cc_mail(CRMConstants.CC_EMAIL)
        task_module.enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        task_module.click_send()
        sleep(10)
        msg = task_module.check_email(mail_subject)
        assert mail_subject in msg

    def test_sms_icon(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver)\
            .open_task_module()
        task_module\
            .open_show_all_tab()
        task_module\
            .search_account_name(CRMConstants.TESTQA)
        sleep(2)
        task_module\
            .open_sms_actions_section()
        title = task_module\
            .check_pop_up_send_sms()

        # Check, SMS pop up is opened. Else: Check, that appear message "There are no phones"
        if title:
            try:
                assert CRMConstants.SEND_SMS in title
            except:
                assert CRMConstants.SERVER_NOT_CONFIGURATE in title
        else:
            message = task_module.get_allert_message()
            assert CRMConstants.ALLERT_MSG_NO_PHONES in message

    def test_mass_edit_tasks(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.open_show_all_tab()
        task_module.search_account_name(CRMConstants.TESTQA)
        sleep(2)
        task = task_module.get_first_account_name()
        task_module.select_all_event()
        task_module.open_mass_edit_task().perform_mass_edit(CRMConstants.STATUS_EVENT, CRMConstants.TYPE_EVENT, CRMConstants.DURATION_EVENT)
        task_module.refresh_page()
        task_module.search_account_name(task)
        sleep(2)
        status = task_module.get_first_status()
        type = task_module.get_first_type()
        assert type == CRMConstants.TYPE_EVENT
        assert status == CRMConstants.STATUS_EVENT

    def test_searching_by_columns(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.open_show_all_tab()
        task_module.search_account_name(CRMConstants.TESTQA)
        sleep(2)
        task = task_module.get_first_account_name()
        status = task_module.get_first_status()
        type = task_module.get_first_type()
        task_module.refresh_page()
        sleep(2)
        task_module.wait_crm_loading_to_finish_tasks(55)
        task_module.search_account_name(task)
        sleep(2)
        task_module.search_by_status(status)
        sleep(2)
        task_module.search_by_type(type)
        sleep(2)
        verify_task = task_module.get_first_account_name()
        verify_status = task_module.get_first_status()
        verify_type = task_module.get_first_type()
        assert task == verify_task
        assert status == verify_status
        assert type == verify_type

    def create_first_event(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver)\
            .open_task_module()

        task_module\
            .open_add_event_module()\
            .create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                          TaskModuleConstants.FIRST_EVENT_TYPE,
                          TaskModuleConstants.FIRST_DURATION,
                          CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                          CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                          TaskModuleConstants.FIRST_ASSIGN_TO,
                          CRMConstants.CLIENT_NAME_FOR_EVENT,
                          TaskModuleConstants.FOURTH_SUBJECT,
                          TaskModuleConstants.FIRST_PRIORITY,
                          TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        res_count = task_module\
            .open_show_all_tab()\
            .find_event_by_subject(TaskModuleConstants.SUBJECT)\
            .get_results_count()

        assert res_count >= 1

        return EventPrecondition(self.driver, self.config)

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def edit_first_event(self):

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver)\
            .open_task_module()
        task_module\
            .open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.FOURTH_SUBJECT)\
            .open_edit_event()\
            .edit_event(TaskModuleConstants.SECOND_EVENT_STATUS,
                        TaskModuleConstants.SECOND_EVENT_TYPE,
                        TaskModuleConstants.SECOND_DURATION,
                        CRMConstants.THIRD_DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                        CRMConstants.THIRD_DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                        TaskModuleConstants.SECOND_ASSIGN_TO,
                        TaskModuleConstants.SECOND_SUBJECT,
                        TaskModuleConstants.SECOND_PRIORITY,
                        TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        task_was_updated_text = task_module.task_was_updated()
        text = "Task was updated"
        assert text == task_was_updated_text
