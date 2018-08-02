import pytest

from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.FourthClientConstants import FourthClientConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.main.python.ui.email.pages.EmailSignInPage import EmailSignInPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.ActionsTasksPrecondition import \
    ActionsTasksPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.MassEmailPrecondition import MassEmailPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.MassSmsPrecondition import MassSmSPrecondition


@pytest.mark.run(order=20)
class ActionsTaskModuleTest(BaseTest):

    def test_check_send_sms_actions_section(self):
        ActionsTasksPrecondition().create_first_event()

        task_module = TasksPage()
        phone_number = task_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_first_client_profile() \
            .get_phone_text()

        task_module = CRMHomePage().open_task_module()
        task_module.find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_sms_actions_section() \
            .perform_send_sms(phone_number, TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        message = task_module.open_first_client_profile() \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .get_sms_text()

        assert message == TaskModuleConstants.DESCRIPTION_SEND_SMS

    def test_check_phone_actions_section(self):
        ActionsTasksPrecondition().create_second_event()
        task_module = TasksPage()
        task_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_phone_actions() \
            .perform_call_section(Config.data.get_data_task_module(TaskModuleConstants.SECOND_CALL_OUTCOME),
                                  Config.data.get_data_task_module(TaskModuleConstants.SECOND_POSITIVE_OUTCOME),
                                  Config.data.get_data_task_module(TaskModuleConstants.THIRD_NEGATIVE_OUTCOME),
                                  TaskModuleConstants.COMMENTS_CALL_PHONE) \
            .click_submit_button()

        client_status = task_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_first_client_profile() \
            .get_client_status()

        assert client_status == Config.data.get_data_task_module(TaskModuleConstants.THIRD_NEGATIVE_OUTCOME)

    def test_send_email_actions_section(self):
        MassEmailPrecondition().create_first_event()

        task_module = TasksPage()

        task_module.open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.FIFTH_SUBJECT) \
            .open_email_actions_section() \
            .perform_send_email(EmailConstants.FIRST_SUBJECT, EmailConstants.TASK_COMMENT)

        confirm_message = task_module.get_confirm_message_task_module()

        assert confirm_message == EmailConstants.SECOND_EMAIL_CONFIRM_MESSAGE

        email_home_page = EmailSignInPage().open_second_tab_page(Config.url_gmail) \
            .set_login_email(
            Config.data.get_data_client(FourthClientConstants.CLIENT_FOURTH, FourthClientConstants.EMAIL_ADDRESS)) \
            .click_first_next() \
            .set_password_email(
            Config.data.get_data_client(FourthClientConstants.CLIENT_FOURTH, FourthClientConstants.EMAIL_PASSWORD)) \
            .click_second_next()

        comment = email_home_page.enter_subject(EmailConstants.FIRST_SUBJECT) \
            .click_searching_button() \
            .click_exist_subject_link(EmailConstants.FIRST_SUBJECT) \
            .get_comment_text()

        support_email = email_home_page.click_tool_tip().get_support_email()

        assert comment == EmailConstants.TASK_COMMENT
        assert support_email == EmailConstants.FIRST_SUPPORT_EMAIL

    def test_send_email_from_phone_actions_section(self):
        MassEmailPrecondition().create_third_event()

        task_module = TasksPage()

        task_module.open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.FIFTH_SUBJECT) \
            .open_phone_actions() \
            .open_send_email_module() \
            .perform_send_email(EmailConstants.FIRST_SUBJECT, EmailConstants.TASK_COMMENT)

        confirm_message = task_module.get_confirm_message_task_module()

        assert confirm_message == EmailConstants.SECOND_EMAIL_CONFIRM_MESSAGE

        email_home_page = EmailSignInPage().open_second_tab_page(Config.url_gmail) \
            .set_login_email(
            Config.data.get_data_client(FourthClientConstants.CLIENT_FOURTH, FourthClientConstants.EMAIL_ADDRESS)) \
            .click_first_next() \
            .set_password_email(
            Config.data.get_data_client(FourthClientConstants.CLIENT_FOURTH, FourthClientConstants.EMAIL_PASSWORD)) \
            .click_second_next()

        comment = email_home_page.enter_subject(EmailConstants.FIRST_SUBJECT) \
            .click_searching_button() \
            .click_exist_subject_link(EmailConstants.FIRST_SUBJECT) \
            .get_comment_text()

        support_email = email_home_page.click_tool_tip().get_support_email()

        assert comment == EmailConstants.TASK_COMMENT
        assert support_email == EmailConstants.FIRST_SUPPORT_EMAIL

    def test_send_sms_from_phone_actions_section(self):
        MassSmSPrecondition().create_fourth_event()

        task_module = TasksPage()

        phone_number = task_module.open_show_all_tab() \
            .find_event_by_subject(TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_first_client_profile() \
            .get_phone_text()

        task_module.open_task_module() \
            .open_show_all_tab().find_event_by_subject(
            TaskModuleConstants.SEVENTH_SUBJECT) \
            .open_phone_actions() \
            .open_send_sms_module() \
            .perform_send_sms(phone_number, TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        message = task_module.open_first_client_profile() \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(TaskModuleConstants.DESCRIPTION_SEND_SMS) \
            .get_sms_text()

        assert message == TaskModuleConstants.DESCRIPTION_SEND_SMS
