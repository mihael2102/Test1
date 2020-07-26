from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassEditPageUI import MassEditPageUI


class ClientsMassEditPreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def mass_edit_clients_ui(self):
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

        """ Select records for Mass Edit """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .refresh_page_ui() \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_all_records_checkbox()

        """ Mass Edit """
        MassEditPageUI(self.driver) \
            .click_mass_action_btn(MassActionsConstantsUI.MASS_EDIT) \
            .mass_edit(
                field_to_edit1=MassActionsConstantsUI.FIELD_CLIENT_STATUS,
                field_to_edit4=MassActionsConstantsUI.FIELD_ASSIGNED_TO,
                assign_to=MassActionsConstantsUI.USER_NAME_1,
                final_btn=MassActionsConstantsUI.BTN_FINAL2)\
            .refresh_page()

        """ Check confirmation message and updated data in table """
        GlobalModulePageUI(self.driver) \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=LeadsModuleConstantsUI.SHORT_EMAIL) \
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME_1) \
            .global_data_checker_new_ui(MassActionsConstantsUI.STATUS)
