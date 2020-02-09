from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.ca.CAMainMenuPage import CAMainMenuPage
from src.main.python.ui.ca.model.pages.ca.withdraw_ca.CAWithdrawPage import CAWithdrawPage
from src.main.python.ui.ca.model.constants.CAconstants.CAWithdrawConstants import CAWithdrawConstants
from src.main.python.ui.ca.model.pages.ca.withdraw_ca.CAWithdrawHistoryPage import CAWithdrawHistoryPage


class WithdrawRequestPreconditionCA(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def withdraw_request_ca(self):
        """ CA Login """
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .login() \
            .enter_email(self.config.get_value('email_live_acc')) \
            .enter_password(self.config.get_value('password_live_acc')) \
            .click_login() \
            .verify() \
            .open_ca_menu() \
            .click_transactions_history()

        """ Execute withdraw on CA side """
        CAMainMenuPage(self.driver) \
            .open_withdraw_tab() \
            .check_withdraw_loaded()
        CAWithdrawPage(self.driver) \
            .click_withdraw_funds() \
            .select_payment_method(CAWithdrawConstants.PAYMENT_METHOD) \
            .set_expiry_month(CAWithdrawConstants.EXPIRY_MONTH) \
            .set_expiry_year(CAWithdrawConstants.EXPIRY_YEAR) \
            .set_cc_last_digits(CAWithdrawConstants.CC_LAST_DIGITS) \
            .select_withdrawal_reason(CAWithdrawConstants.REASON) \
            .click_submit()

        """ Verify withdraw status on CA side (pending) """
        status_ca = CAWithdrawHistoryPage(self.driver) \
            .open_withdraw_history_tab() \
            .get_withdraw_status("1")

        """ Verify withdraw status in CRM (pending) """
        CRMLoginPage(self.driver) \
            .open_second_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_value('email_live_acc')) \
            .scroll_to_financial_transactions_section() \
            .open_financial_transactions_tab()
