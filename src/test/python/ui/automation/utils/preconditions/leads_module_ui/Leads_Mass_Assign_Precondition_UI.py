from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassAssignPageUI import MassAssignPageUI


class LeadsMassAssignPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_assign_leads_ui(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Select records for Mass Assign """
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS)\
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL)\
            .select_all_records()\
            .click_mass_action_btn(MassActionsConstantsUI.MASS_ASSIGN)

        """ Mass Assign """
        MassAssignPageUI(self.driver)\
            .select_department(MassActionsConstantsUI.DEPARTMENT_ALL)\
            .set_users_field(MassActionsConstantsUI.USER_NAME)\
            .select_user_by_title(MassActionsConstantsUI.USER_NAME)\
            .select_status(MassActionsConstantsUI.STATUS_R_NEW)\
            .click_assign_btn()

        """ Check confirmation message and updated data in table """
        GlobalTablePageUI(self.driver) \
            .verify_success_message()\
            .click_ok()\
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME)\
            .global_data_checker_new_ui(MassActionsConstantsUI.STATUS_R_NEW)
