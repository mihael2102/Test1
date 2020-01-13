from src.main.python.ui.crm.model.constants_ui.base_crm_constants.FiltersConstants import FiltersConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_constants.MassActionsConstants import MassActionsConstants
from src.main.python.ui.crm.model.pages.global_module_ui.MassEditPageUI import MassEditPageUI


class ClientsMassEditPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_edit_clients_ui(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        """ Select records for Mass Edit """
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstants.FILTER_TEST_CLIENTS) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_all_records() \
            .click_mass_action_btn(MassActionsConstants.MASS_EDIT)

        """ Mass Edit """
        MassEditPageUI(self.driver) \
            .select_field_to_edit(MassActionsConstants.FIELD_CLIENT_STATUS) \
            .select_from_list(MassActionsConstants.FIELD_CLIENT_STATUS, MassActionsConstants.STATUS_B_TEST) \
            .select_field_to_edit(MassActionsConstants.FIELD_ASSIGNED_TO) \
            .select_from_list(MassActionsConstants.FIELD_ASSIGNED_TO, MassActionsConstants.USER_NAME_1) \
            .click_save_changes_btn()

        """ Check confirmation message and updated data in table """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .global_data_checker_new_ui(MassActionsConstants.USER_NAME_1) \
            .global_data_checker_new_ui(MassActionsConstants.STATUS_B_TEST)
