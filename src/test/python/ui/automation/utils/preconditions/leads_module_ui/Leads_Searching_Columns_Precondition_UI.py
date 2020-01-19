from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI


class LeadsSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def leads_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS) \
            .open_tab_list_view_ui(LeadsModuleConstantsUI.TAB_ALL)

        """ Get lead's data from the first row of list view """
        lead_no = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        lead_status = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_LEAD_STATUS,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        email = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        phone = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_PHONE,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        country = CRMBaseMethodsPage(self.driver) \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_COUNTRY,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if lead_no:
            search\
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                                       data=lead_no)
        if phone:
            search\
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_PHONE,
                                       data=phone)
        if lead_status:
            search\
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_LEAD_STATUS,
                                          data=lead_status)
        if assigned_to:
            search\
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if country:
            search\
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_COUNTRY,
                                          data=country)
        if email and ("*" not in email):
            search\
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                          data=email)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if lead_no:
            result\
                .global_data_checker_new_ui(lead_no)
        if phone:
            result\
                .global_data_checker_new_ui(phone)
        if lead_status:
            result\
                .global_data_checker_new_ui(lead_status)
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
