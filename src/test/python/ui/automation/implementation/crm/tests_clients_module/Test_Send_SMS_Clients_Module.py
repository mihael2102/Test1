import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=11)
class SendSMSClientsModule(BaseTest):

    def test_perform_send_sms_clients_module(self):
        crm_clients_module_page = CRMLoginPage() \
            .open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .perform_searching(Config.data.get_data_client(CRMConstants.CLIENT_STATUS),
                               Config.data.get_data_client(CRMConstants.SHORT_E_MAIL),
                               Config.data.get_data_client(CRMConstants.SHORT_CLIENT_NAME),
                               Config.data.get_data_client(TestDataConstants.SECOND_COUNTRY),
                               Config.data.get_data_client(CRMConstants.SHORT_FIRST_NAME),
                               Config.data.get_data_client(CRMConstants.SHORT_LAST_NAME),
                               Config.data.get_data_client(TestDataConstants.CITY),
                               Config.data.get_data_client(CRMConstants.BRAND_NEW_FOREX))

        first_client = crm_clients_module_page.get_first_client_email()
        crm_clients_module_page.came_back_on_previous_page().click_search_button()

        send_message_module = crm_clients_module_page.select_record() \
            .open_send_sms_module() \
            .perform_send_sms(CRMConstants.DESCRIPTION_SEND_SMS) \
            .click_send_button()

        confirmation_message = crm_clients_module_page.get_confirm_message()
        assert confirmation_message == CRMConstants().SEND_SMS_MESSAGE
        send_message_module.click_ok()

        crm_client_profile = crm_clients_module_page.refresh() \
            .select_filter(Config.data.get_data_client(TestDataConstants.FILTER)) \
            .perform_searching_by_email(first_client) \
            .click_search_button() \
            .open_client_id()

        counter = crm_client_profile.get_counter_sms()
        assert counter == CRMConstants.COUNTER_SMS

        message = crm_client_profile \
            .perform_scroll_down() \
            .open_sms_tab()

        assert message == CRMConstants.DESCRIPTION_SEND_SMS
