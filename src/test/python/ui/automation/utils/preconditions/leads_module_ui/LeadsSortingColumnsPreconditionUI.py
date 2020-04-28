from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI


class LeadsSortingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def leads_sorting_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS) \
            .open_tab_list_view_ui(LeadsModuleConstantsUI.TAB_ALL)

        """ Get and compare lead's data from 1st and 2nd row of list view """
        get_data = GlobalModulePageUI(self.driver)
        lead_no = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        lead_status = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_LEAD_STATUS,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        email = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        phone = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_PHONE,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        country = get_data \
            .get_data_from_list_view_ui(column=LeadsModuleConstantsUI.COLUMN_COUNTRY,
                                        row=LeadsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalModulePageUI(self.driver)
        if lead_no:
            search \
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_LEAD_NO,
                                       data=lead_no)
        if phone and ("*" not in phone):
            search \
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_PHONE,
                                       data=phone)
        if lead_status:
            search \
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_LEAD_STATUS,
                                          data=lead_status)
        if assigned_to:
            search \
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if country:
            search \
                .select_data_column_field(column=LeadsModuleConstantsUI.COLUMN_COUNTRY,
                                          data=country)
        if email and ("*" not in email):
            search \
                .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                       data=email)

        """ Verify correct data found """
        result = GlobalModulePageUI(self.driver)
        if lead_no:
            result \
                .global_data_checker_new_ui(lead_no)
        if phone:
            result \
                .global_data_checker_new_ui(phone)
        if lead_status:
            result \
                .global_data_checker_new_ui(lead_status)
        if assigned_to:
            result \
                .global_data_checker_new_ui(assigned_to)
        if country:
            result \
                .global_data_checker_new_ui(country)
        if email and ("*" not in email):
            result \
                .global_data_checker_new_ui(email)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver) \
            .get_number_records()
        assert number_records == 1
