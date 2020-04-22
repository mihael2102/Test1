import pytest
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage
from src.test.python.ui.automation.utils.preconditions.workflows.WorkflowsPrecondition import WorkflowsPrecondition
from src.main.python.ui.crm.model.pages.workflows.WorkflowsPage import WorkflowsPage
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.MassActionsConstantsUI import MassActionsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.MassAssignPageUI import MassAssignPageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.crm.model.constants.WorkflowsConstants import WorkflowsConstants
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

        """ Check workflow by status is working """
        CRMBaseMethodsPage(self.driver)\
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        """ Select records for Mass Assign """
        ClientsModulePageUI(self.driver) \
            .select_filter_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   ClientsModuleConstantsUI.SHORT_EMAIL) \
            .click_crm_id_ui(row=5) \

        CRMHomePage(self.driver) \
            .open_client_module() \
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))
        ClientsModulePage(self.driver) \
            .set_data_to_email_column_search_field(WorkflowsConstants.PANDATS_EMAIL) \
            .click_search_btn() \
            .click_crm_id_list_view(row=5)
        ClientProfilePage(self.driver) \
            .change_client_status_with_pencil(var.get_var(self.__class__.__name__)["client_status"]) \
            .refresh_page()
        country = ClientProfilePage(self.driver) \
            .open_address_information() \
            .get_country_text()
        assert country == WorkflowsConstants.COUNTRY_ALBANIA
        address = ClientProfilePage(self.driver).get_address_text()
        assert address == WorkflowsConstants.TEST_ADDRESS
