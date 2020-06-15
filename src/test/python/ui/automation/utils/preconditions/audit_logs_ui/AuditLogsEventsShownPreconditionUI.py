from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.audit_logs.AuditLogsPage import AuditLogsPage
from src.main.python.ui.crm.model.constants.AuditLogsConstants import AuditLogsConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage


class AuditLogsEventsShownPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def new_events_shown_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Audit Logs module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_AUDIT_LOGS)

        """ Searching by data: Module=Users, Actions=Login, User=pandaauto and pull Active Date """
        active_date = AuditLogsPage(self.driver) \
            .perform_searching(AuditLogsConstants.MODULE_USERS,
                               AuditLogsConstants.ACTION_OTP_LOGIN,
                               AuditLogsConstants.USER_PANDAAUTO) \
            .get_active_date_list_view(AuditLogsConstants.ROW_1_LIST_VIEW)

        active_date = active_date.split(" ")[0]

        current_date = CRMBaseMethodsPage(self.driver) \
            .get_current_date()

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(active_date, current_date)

        """ Open Clients module and open details page of pandats client """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_CLIENTS)

        client_email = ClientsPage(self.driver) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .perform_searching_by_email(CRMConstants.SHORT_EMAIL) \
            .click_search_button() \
            .open_client_id() \
            .get_email_text()

        """ Open Audit Logs module """
        CRMBaseMethodsPage(self.driver) \
            .open_module(TestDataConstants.MODULE_AUDIT_LOGS)

        """ Searching by data: Module=Accounts, Actions=DetailView, User=pandaauto, Email and pull Active Date """
        active_date = AuditLogsPage(self.driver) \
            .perform_searching(AuditLogsConstants.MODULE_CLIENTS,
                               AuditLogsConstants.ACTION_DETAIL_VIEW,
                               AuditLogsConstants.USER_PANDAAUTO,
                               client_email) \
            .get_active_date_list_view(AuditLogsConstants.ROW_1_LIST_VIEW)

        """ Verify Active Date """
        active_date = active_date.split(" ")[0]

        current_date = CRMBaseMethodsPage(self.driver) \
            .get_current_date()

        CRMBaseMethodsPage(self.driver) \
            .comparator_string(active_date, current_date)
