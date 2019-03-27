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

class EventPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def test_email_icon(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.search_account_name(CRMConstants.TESTQA)
        first_account_name = task_module.get_first_account_name()
        task_module.open_email_actions_section()
        task_module.enter_subject_mail(CRMConstants.SUBJECT_TASK_MAIL)
        task_module.enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        task_module.enter_cc_mail(CRMConstants.CC_EMAIL)
        task_module.enter_body_mail(CRMConstants.BODY_LEAD_MAIL)
        task_module.click_send()
        sleep(60)
        task_module.check_email()






    def create_first_event(self):

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()

        task_module.open_add_event_module().create_event(TaskModuleConstants.FIRST_EVENT_STATUS,
                                                         TaskModuleConstants.FIRST_EVENT_TYPE,
                                                         TaskModuleConstants.FIRST_DURATION,
                                                         CRMConstants.DATE.strftime(CRMConstants.SECOND_FORMAT_DATE),
                                                         CRMConstants.DATE.strftime(CRMConstants.FIRST_FORMAT_TIME),
                                                         TaskModuleConstants.FIRST_ASSIGN_TO,
                                                         self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME],
                                                         TaskModuleConstants.FOURTH_SUBJECT,
                                                         TaskModuleConstants.FIRST_PRIORITY,
                                                         TaskModuleConstants.DESCRIPTION_ADD_EVENT)

        task_module.open_show_all_tab() \
            .search_account_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])
        search_account_name_text = task_module.open_show_all_tab() \
                                         .get_account_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])
        name = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME] + " Doe"
        assert name == search_account_name_text

        return EventPrecondition(self.driver, self.config)

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def edit_first_event(self):

        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        task_module = CRMHomePage(self.driver).open_task_module()
        task_module.open_show_all_tab() \
            .search_account_name(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[LeadsModuleConstants.FIRST_NAME])\
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


