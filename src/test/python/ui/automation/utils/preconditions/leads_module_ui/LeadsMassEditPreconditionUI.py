from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassEditPageUI import MassEditPageUI


class LeadsMassEditPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_edit_leads_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Select records for Mass Edit """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_all_records_checkbox() \
            .click_mass_action_btn(MassActionsConstantsUI.MASS_EDIT)

        """ Mass Edit """
        status = MassEditPageUI(self.driver) \
            .get_item_from_list_by_number(
                pick_list=MassActionsConstantsUI.LIST_LEADS_STATUS,
                number='2')
        MassEditPageUI(self.driver) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_LEAD_STATUS) \
            .select_from_list(MassActionsConstantsUI.LIST_LEAD_STATUS, MassActionsConstantsUI.STATUS_R_NEW) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_LANGUAGE) \
            .set_text_field(MassActionsConstantsUI.FIELD_LANGUAGE, MassActionsConstantsUI.LANGUAGE_GERMAN) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_COUNTRY) \
            .select_from_list(MassActionsConstantsUI.FIELD_COUNTRY, MassActionsConstantsUI.COUNTRY_ALBANIA) \
            .click_save_changes_btn()

        """ Check confirmation message and updated data in table """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .global_data_checker_new_ui(MassActionsConstantsUI.LANGUAGE_GERMAN) \
            .global_data_checker_new_ui(MassActionsConstantsUI.STATUS_R_NEW) \
            .global_data_checker_new_ui(MassActionsConstantsUI.COUNTRY_ALBANIA)
