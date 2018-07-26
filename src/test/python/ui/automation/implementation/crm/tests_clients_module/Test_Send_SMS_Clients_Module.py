import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=13)
class SendSMSClientsModuleTest(BaseTest):

    def test_perform_send_sms_clients_module(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE,
                                                           TestDataConstants.FIRST_COUNTRY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY),
                               Config.data.get_data_client(TestDataConstants.CLIENT_ONE, CRMConstants.BRAND))

        initial_counter_client = crm_clients_module_page.open_client_id().get_counter_sms()
        first_client = crm_clients_module_page.get_first_client_email()

        total_counter = initial_counter_client + 1

        crm_clients_module_page.came_back_on_previous_page().click_search_button()

        send_message_module = crm_clients_module_page.select_record() \
            .open_send_sms_module() \
            .perform_send_sms(CRMConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        confirmation_message = crm_clients_module_page.get_confirm_message()
        assert confirmation_message == CRMConstants().SEND_SMS_MESSAGE
        send_message_module.click_ok()

        crm_client_profile = crm_clients_module_page.refresh() \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching_by_email(first_client) \
            .click_search_button() \
            .open_client_id()

        counter = crm_client_profile.get_counter_sms()
        assert counter == total_counter

        message = crm_client_profile \
            .perform_scroll_down() \
            .open_sms_tab() \
            .open_sms_view_module(CRMConstants.DESCRIPTION_SEND_SMS) \
            .get_sms_text()

        assert message == CRMConstants.DESCRIPTION_SEND_SMS
