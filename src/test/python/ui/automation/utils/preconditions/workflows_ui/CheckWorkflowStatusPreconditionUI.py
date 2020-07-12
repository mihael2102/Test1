import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.WorkflowsConstants import WorkflowsConstants
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class CheckWorkflowStatusPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_workflow_by_status_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Workflow module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CRM_Config)

        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))

        CRMConfigurationPage(self.driver) \
            .check_workflows_loaded()

        self.driver.switch_to_default_content()

        """ Check workflow by status """
        CRMBaseMethodsPage(self.driver)\
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        ClientsModulePageUI(self.driver) \
            .select_filter_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(
                column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                data=ClientsModuleConstantsUI.SHORT_EMAIL) \
            .click_crm_id_ui(row=5) \
            .edit_list_via_pencil(
                field=ClientDetailsConstantsUI.FIELD_CLIENT_STATUS,
                item=var.get_var('WorkflowsPrecondition')["client_status"]) \
            .refresh_client_page()
        country = ClientDetailsPageUI(self.driver)\
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
        address = ClientDetailsPageUI(self.driver) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)

        """ Verify data """
        counter = 0
        while country != WorkflowsConstants.COUNTRY_ALBANIA and address != WorkflowsConstants.TEST_ADDRESS:
            ClientDetailsPageUI(self.driver) \
                .refresh_client_page()
            country = ClientDetailsPageUI(self.driver) \
                .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
                .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
            address = ClientDetailsPageUI(self.driver) \
                .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)
            counter += 1
            if counter == 3:
                break
