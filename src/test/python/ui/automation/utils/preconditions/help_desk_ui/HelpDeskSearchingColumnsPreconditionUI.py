from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.help_desk_ui.HelpDeskModuleConstantsUI import HelpDeskModuleConstantsUI


class HelpDeskSearchingColumnsPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def help_desk_searching_columns_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                self.config.get_value('url'),
                self.config.get_value(TestDataConstants.USER_NAME),
                self.config.get_value(TestDataConstants.CRM_PASSWORD),
                self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Help Desk module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_HELP_DESK) \
            .open_tab_list_view_ui(HelpDeskModuleConstantsUI.TAB_ALL)

        """ Get ticket's data from the first row of list view """
        ticket_no = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=HelpDeskModuleConstantsUI.COLUMN_TICKET_NO,
                                        row=HelpDeskModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        status = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=HelpDeskModuleConstantsUI.COLUMN_STATUS,
                                        row=HelpDeskModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)
        assigned_to = GlobalTablePageUI(self.driver) \
            .get_data_from_list_view_ui(column=HelpDeskModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                        row=HelpDeskModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Search by table """
        search = GlobalTablePageUI(self.driver)
        if status:
            search\
                .select_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_STATUS,
                                          data=status)
        if assigned_to:
            search\
                .select_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_ASSIGNED_TO,
                                          data=assigned_to)
        if ticket_no:
            search\
                .set_data_column_field(column=HelpDeskModuleConstantsUI.COLUMN_TICKET_NO,
                                       data=ticket_no)

        """ Verify correct data found """
        result = GlobalTablePageUI(self.driver)
        if ticket_no:
            result\
                .global_data_checker_new_ui(ticket_no)
        if status:
            result\
                .global_data_checker_new_ui(status)
        if assigned_to:
            result\
                .global_data_checker_new_ui(assigned_to)

        """ Verify, only 1 record was found """
        number_records = CRMBaseMethodsPage(self.driver)\
            .get_number_records()
        assert number_records == 1
