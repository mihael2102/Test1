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


class LeadsMassEditPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_edit_leads_ui(self):
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Select records for Mass Edit """
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstants.FILTER_TEST_LEADS) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_all_records() \
            .click_mass_action_btn(MassActionsConstants.MASS_EDIT)

        """ Mass Edit """
        MassEditPageUI(self.driver) \
            .select_field_to_edit(MassActionsConstants.FIELD_LEAD_STATUS) \
            .select_from_list(MassActionsConstants.LIST_LEAD_STATUS, MassActionsConstants.STATUS_R_NEW) \
            .select_field_to_edit(MassActionsConstants.FIELD_LANGUAGE) \
            .set_text_field(MassActionsConstants.FIELD_LANGUAGE, MassActionsConstants.LANGUAGE_GERMAN) \
            .select_field_to_edit(MassActionsConstants.FIELD_COUNTRY) \
            .select_from_list(MassActionsConstants.FIELD_COUNTRY, MassActionsConstants.COUNTRY_ALBANIA) \
            .click_save_changes_btn()

        """ Check confirmation message and updated data in table """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .global_data_checker_new_ui(MassActionsConstants.LANGUAGE_GERMAN) \
            .global_data_checker_new_ui(MassActionsConstants.STATUS_R_NEW) \
            .global_data_checker_new_ui(MassActionsConstants.COUNTRY_ALBANIA)
