import pytest
from src.main.python.ui.crm.model.pages.mt4_ui.MT4CreateTAPageUI import MT4CreateTAPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4CreateTAConstantsUI import MT4CreateTAConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants_ui.mt4_ui.MT4ActionsConstantsUI import MT4ActionsConstantsUI
from src.main.python.ui.crm.model.constants_ui.tasks_ui.AddDeleteEventConstantsUI import AddDeleteEventConstantsUI
from src.main.python.ui.crm.model.pages.tasks_ui.AddDeleteEventPageUI import AddDeleteEventPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class AddInteractionPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def add_interaction_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module. Find client by 'pandaqa' email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   AddDeleteEventConstantsUI.SHORT_EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui(ClientsModuleConstantsUI.ROW_NUMBER_FOR_DATA_SEARCHING_1)

        """ Add Interaction """
        AddDeleteEventPageUI(self.driver)\
            .add_event(
            btn_interaction=AddDeleteEventConstantsUI.BTN_ADD_INT,
            list4=AddDeleteEventConstantsUI.LIST_ASSIGN_TO, assign_to=AddDeleteEventConstantsUI.ASSIGN_TO,
            field1=AddDeleteEventConstantsUI.FIELD_SUBJECT, subject=AddDeleteEventConstantsUI.INT_SUBJ_1,
            comments=AddDeleteEventConstantsUI.COMMENTS,
            final_btn=AddDeleteEventConstantsUI.BTN_SAVE_NEW)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()
