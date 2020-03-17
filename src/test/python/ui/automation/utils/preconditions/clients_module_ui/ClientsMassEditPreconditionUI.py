from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassEditPageUI import MassEditPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


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
                new_design=0,
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        """ Select records for Mass Edit """
        GlobalTablePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .select_all_records_checkbox() \
            .click_mass_action_btn(MassActionsConstantsUI.MASS_EDIT)

        """ Mass Edit """
        MassEditPageUI(self.driver) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_CLIENT_STATUS) \
            .select_from_list(MassActionsConstantsUI.FIELD_CLIENT_STATUS,
                              var.get_var(self.__class__.__name__)["client_status"]) \
            .select_field_to_edit(MassActionsConstantsUI.FIELD_ASSIGNED_TO) \
            .select_from_list(MassActionsConstantsUI.FIELD_ASSIGNED_TO,
                              MassActionsConstantsUI.USER_NAME_1) \
            .click_save_changes_btn()

        """ Check confirmation message and updated data in table """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok() \
            .set_data_column_field(LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   LeadsModuleConstantsUI.SHORT_EMAIL) \
            .global_data_checker_new_ui(MassActionsConstantsUI.USER_NAME_1) \
            .global_data_checker_new_ui(var.get_var(self.__class__.__name__)["field_citizenship"])
