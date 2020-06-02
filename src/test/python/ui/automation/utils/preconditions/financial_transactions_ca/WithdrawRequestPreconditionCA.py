from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.pages.ca.CAMainMenuPage import CAMainMenuPage
from src.main.python.ui.ca.model.pages.ca.withdraw_ca.CAWithdrawPage import CAWithdrawPage
from src.main.python.ui.ca.model.constants.CAconstants.CAWithdrawConstants import CAWithdrawConstants
from src.main.python.ui.ca.model.pages.ca.withdraw_ca.CAWithdrawHistoryPage import CAWithdrawHistoryPage
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.fin_transactions_ui.FinTransactionsModuleConstantsUI import \
    FinTransactionsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from time import sleep


class WithdrawRequestPreconditionCA(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

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
        status_crm = CRMLoginPage(self.driver) \
            .open_second_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE,
                                                       TestDataConstants.FILTER)) \
            .find_client_by_email(self.config.get_value('email_live_acc')) \
            .scroll_to_financial_transactions_section() \
            .open_financial_transactions_tab() \
            .get_withdraw_status()

        """ Compare ca and crm statuses """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_ca, status_crm)

        """ Change ticket status to 'Closed' in CA """
        status_ca = CAWithdrawHistoryPage(self.driver)\
            .switch_first_tab_page() \
            .click_cancel_btn() \
            .get_withdraw_status("1")

        """ Verify status updated in CRM """
        CRMLoginPage(self.driver) \
            .switch_second_tab_page() \
            .refresh_page()
        status_crm = ClientProfilePage(self.driver) \
            .get_withdraw_status()

        """ Compare ca and crm statuses """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_ca, CAWithdrawConstants.STATUS_REQUEST_CA)
        counter = 0
        while status_crm != CAWithdrawConstants.STATUS_REQUEST_CRM:
            status_crm = ClientProfilePage(self.driver) \
                .refresh_page() \
                .get_withdraw_status()
            sleep(1)
            counter += 1
            if counter == 3:
                break
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_crm, CAWithdrawConstants.STATUS_REQUEST_CRM)

    def withdraw_request_ca_ui(self):
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
        CRMLoginPageUI(self.driver) \
            .crm_login_second_tab(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        status_crm = ClientsModulePageUI(self.driver)\
            .select_filter_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   data=self.config.get_value('email_live_acc')) \
            .click_crm_id_ui() \
            .open_tab(ClientDetailsConstantsUI.TAB_FINANCIAL_TRANSACTIONS) \
            .get_data_cell_table(column=FinTransactionsModuleConstantsUI.COLUMN_F_APPROVAL)

        """ Compare ca and crm statuses """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_ca, status_crm)

        """ Change ticket status to 'Closed' in CA """
        status_ca = CAWithdrawHistoryPage(self.driver) \
            .switch_first_tab_page() \
            .click_cancel_btn() \
            .get_withdraw_status("1")

        """ Verify status updated in CRM """
        CRMLoginPageUI(self.driver) \
            .switch_second_tab_page() \
            .refresh_page()
        status_crm = ClientDetailsPageUI(self.driver)\
            .open_tab(ClientDetailsConstantsUI.TAB_FINANCIAL_TRANSACTIONS) \
            .get_data_cell_table(column=FinTransactionsModuleConstantsUI.COLUMN_F_APPROVAL)

        """ Compare ca and crm statuses """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_ca, CAWithdrawConstants.STATUS_REQUEST_CA)
        counter = 0
        while status_crm != CAWithdrawConstants.STATUS_REQUEST_CRM:
            status_crm = ClientDetailsPageUI(self.driver) \
                .refresh_client_page() \
                .open_tab(ClientDetailsConstantsUI.TAB_FINANCIAL_TRANSACTIONS) \
                .get_data_cell_table(column=FinTransactionsModuleConstantsUI.COLUMN_F_APPROVAL)
            sleep(1)
            counter += 1
            if counter == 3:
                break
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(status_crm, CAWithdrawConstants.STATUS_REQUEST_CRM)
