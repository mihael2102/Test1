from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
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
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS)\
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL)\
            .select_all_records_checkbox()\
            .click_mass_action_btn(MassActionsConstantsUI.MASS_ASSIGN)

        """ Mass Assign """
        MassAssignPageUI(self.driver)\
            .select_department(MassActionsConstantsUI.DEPARTMENT_ALL)\
            .set_users_field(MassActionsConstantsUI.USER_NAME)\
            .select_user_by_title(MassActionsConstantsUI.USER_NAME)\
            .select_status(MassActionsConstantsUI.STATUS_R_NEW)\
            .click_assign_btn()

        """ Check confirmation message and updated data in table """
        GlobalModulePageUI(self.driver) \
            .verify_success_message()\
            .click_ok() \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS)\
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME)\
            .global_data_checker_new_ui(MassActionsConstantsUI.STATUS_R_NEW)
