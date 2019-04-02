import pytest
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.FourthClientConstants import FourthClientConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.email.model.pages.EmailSignInPage import EmailSignInPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.modules.client_modules.send_email.SendEmailClientsModule import SendEmailClientsModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


@pytest.mark.run(order=30)
class SendEmailTestCRM(BaseTest):

    def test_send_email(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
                                 .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                                            self.config.get_value(TestDataConstants.CRM_PASSWORD),
                                            self.config.get_value(TestDataConstants.OTP_SECRET)) \
                                 .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                                TestDataConstants.FILTER)) \
                                 .find_client_by_email(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                                                      TestDataConstants.E_MAIL))
        sleep(2)
        ClientsPage(self.driver).click_send_mail_btn()
        SendEmailClientsModule(self.driver).set_subject(EmailConstants.FIRST_SUBJECT) \
                                           .set_comment(EmailConstants.CLIENTS_COMMENT) \
                                           .click_save_btn()
        ClientProfilePage(self.driver).scroll_to_emails_section() \
                                      .click_emails_tab()
        actual_email_subject = SendEmailClientsModule(self.driver).get_email_subject()
        expected_email_subject = EmailConstants.FIRST_SUBJECT
        assert actual_email_subject == expected_email_subject
        SendEmailClientsModule(self.driver).click_edit_email_btn()











    def test_make_send_email(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_client_module_clients_module() \
            .open_all_tab_clients_module() \
            .perform_searching_by_email(
            Config.data.get_data_client(FourthClientConstants.CLIENT_FOURTH, FourthClientConstants.EMAIL_ADDRESS)) \
            .click_search_button()

        crm_clients_module_page.select_record() \
            .click_send_email_module() \
            .perform_send_email(EmailConstants.FIRST_SUBJECT, EmailConstants.CLIENTS_COMMENT)

        confirm_message = crm_clients_module_page.get_confirm_message()

        assert confirm_message == TaskModuleConstants.EMAIL_CONFIRM_MESSAGE

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

        support_email = email_home_page.click_tool_tip() \
            .get_support_email()

        assert comment == EmailConstants.CLIENTS_COMMENT
        assert support_email == EmailConstants.FIRST_SUPPORT_EMAIL
