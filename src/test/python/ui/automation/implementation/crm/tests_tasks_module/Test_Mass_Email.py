from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.modules.tasks_module.TaskModule import TaskModule
from src.main.python.ui.email.pages.EmailSignInPage import EmailSignInPage

from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.MassEmailPrecondition import MassEmailPrecondition

from src.test.python.utils.TestDataConstants import TestDataConstants


class MassEmailTaskModule(BaseTest):

    def test_make_mass_email(self):
        # MassEmailPrecondition().create_first_event().create_second_event()
        #
        # task_module = TaskModule()
        #
        # task_module.open_show_all_tab().find_event_by_subject(
        #     TaskModuleConstants.FIFTH_SUBJECT).select_two_records_task_module() \
        #     .open_mass_email_task_module() \
        #     .perform_mass_email(EmailConstants.FIRST_SUBJECT, EmailConstants.TASK_COMMENT)
        #
        # confirm_message = task_module.get_confirm_message_task_module()
        #
        # assert confirm_message == EmailConstants.SECOND_EMAIL_CONFIRM_MESSAGE

        email_home_page = EmailSignInPage().open_second_tab_page(Config.url_gmail) \
            .set_login_email(
            Config.data.get_data_client(TestDataConstants.CLIENT_FOURTH, EmailConstants.FIRST_EMAIL_ADDRESS)) \
            .click_first_next() \
            .set_password_email(
            Config.data.get_data_client(TestDataConstants.CLIENT_FOURTH, EmailConstants.FIRST_EMAIL_PASSWORD)) \
            .click_second_next()

        # comment = email_home_page.enter_subject("Email subject 747") \
        #     .click_searching_button() \
        #     .click_exist_subject_link("Email subject 747") \
        #     .get_comment_text()

        # support_email = email_home_page.click_tool_tip() \
        #     .get_support_email()

        # assert comment == EmailConstants.TASK_COMMENT
        # assert support_email == EmailConstants.FIRST_SUPPORT_EMAIL

        email_home_page.open_google_accounts().perform_add_account()

        email_home_page = EmailSignInPage().open_second_tab_page(Config.url_gmail) \
            .click_use_another_email() \
            .set_login_email(
            Config.data.get_data_client(TestDataConstants.CLIENT_FOURTH, EmailConstants.SECOND_EMAIL_ADDRESS)) \
            .click_first_next() \
            .set_password_email(
            Config.data.get_data_client(TestDataConstants.CLIENT_FOURTH, EmailConstants.SECOND_EMAIL_PASSWORD)) \
            .click_second_next()

        comment = email_home_page.enter_subject(EmailConstants.FIRST_SUBJECT) \
            .click_searching_button() \
            .click_exist_subject_link(EmailConstants.FIRST_SUBJECT) \
            .get_comment_text()

        support_email = email_home_page.click_tool_tip() \
            .get_support_email()

        assert comment == EmailConstants.TASK_COMMENT
        assert support_email == EmailConstants.FIRST_SUPPORT_EMAIL
