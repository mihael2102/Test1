from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
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
        MassEditPageUI(self.driver) \
            .mass_edit(
                field_to_edit1=MassActionsConstantsUI.FIELD_LEAD_STATUS,
                list1=MassActionsConstantsUI.LIST_LEAD_STATUS,
                field_to_edit2=MassActionsConstantsUI.FIELD_LANGUAGE,
                field1=MassActionsConstantsUI.FIELD_LANGUAGE, language=MassActionsConstantsUI.LANGUAGE_GERMAN,
                field_to_edit3=MassActionsConstantsUI.FIELD_COUNTRY,
                field2=MassActionsConstantsUI.FIELD_COUNTRY, country=MassActionsConstantsUI.COUNTRY_ALBANIA,
                final_btn=MassActionsConstantsUI.BTN_FINAL2)

        """ Check updated data in list view """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .global_data_checker_new_ui(MassActionsConstantsUI.LANGUAGE_GERMAN) \
            .global_data_checker_new_ui(MassActionsConstantsUI.LEAD_STATUS) \
            .global_data_checker_new_ui(MassActionsConstantsUI.COUNTRY_ALBANIA)
