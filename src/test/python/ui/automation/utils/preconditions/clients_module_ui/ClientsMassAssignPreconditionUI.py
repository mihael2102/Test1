from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassAssignPageUI import MassAssignPageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI


class ClientsMassAssignPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_assign_clients_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        """ Select records for Mass Assign """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .refresh_page_ui() \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=LeadsModuleConstantsUI.SHORT_EMAIL)\
            .select_all_records_checkbox()

        """ Mass Assign """
        mass_page = MassAssignPageUI(self.driver)
        status = mass_page\
            .click_mass_action_btn(MassActionsConstantsUI.MASS_ASSIGN)\
            .get_item_from_list_by_number(
                pick_list=MassActionsConstantsUI.LIST_CLIENTS_STATUS,
                number='3')
        mass_page \
            .mass_assign(
                department=MassActionsConstantsUI.DEPARTMENT_ALL,
                user=MassActionsConstantsUI.USER_NAME,
                status=status,
                final_btn=MassActionsConstantsUI.BTN_FINAL)\
            .refresh_page()

        """ Check updated data in list view """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS)\
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME)\
            .global_data_checker_new_ui(MassActionsConstantsUI.STATUS_R_NEW)
