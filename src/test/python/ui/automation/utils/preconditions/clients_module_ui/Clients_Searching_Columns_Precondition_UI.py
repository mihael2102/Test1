from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class ClientsSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def clients_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                self.config.get_value('url'),
                self.config.get_value(TestDataConstants.USER_NAME),
                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS) \
            .open_tab_list_view_ui(ClientsModuleConstantsUI.TAB_ALL)

        """ Get client's data from the first row of list view """
        crm_id = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_status = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_CLIENT_STATUS,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        email = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        client_name = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_CLIENT_NAME,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        country = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=ClientsModuleConstantsUI.COLUMN_COUNTRY,
                                        row=ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if crm_id:
            search\
                .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_CRM_ID,
                                       data=crm_id)
        if client_name:
            search\
                .set_data_column_field(column=ClientsModuleConstantsUI.COLUMN_CLIENT_NAME,
                                       data=client_name)
        if client_status:
            search\
                .select_data_column_field(column=ClientsModuleConstantsUI.COLUMN_CLIENT_STATUS,
                                          data=client_status)
        if assigned_to:
            search\
                .select_data_column_field(column=ClientsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if country:
            search\
                .select_data_column_field(column=ClientsModuleConstantsUI.COLUMN_COUNTRY,
                                          data=country)
        if email and ("*" not in email):
            search\
                .select_data_column_field(column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                                          data=email)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if crm_id:
            result\
                .global_data_checker_new_ui(crm_id)
        if client_name:
            result\
                .global_data_checker_new_ui(client_name)
        if client_status:
            result\
                .global_data_checker_new_ui(client_status)
        if assigned_to:
            result\
                .global_data_checker_new_ui(assigned_to)
        if country:
            result\
                .global_data_checker_new_ui(country)
        if email and ("*" not in email):
            result\
                .global_data_checker_new_ui(email)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver)\
            .get_number_records()
        assert number_records == 1
