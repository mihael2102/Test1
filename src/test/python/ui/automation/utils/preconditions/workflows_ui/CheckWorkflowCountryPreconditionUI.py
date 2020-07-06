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
from src.main.python.ui.crm.model.pages.clients_ui.ClientEditPageUI import ClientEditPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientEditConstantsUI import ClientEditConstantsUI


@pytest.mark.run(order=13)
class CheckWorkflowCountryPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_workflow_by_country_ui(self):
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

        """ Check workflow by country """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)

        ClientsModulePageUI(self.driver) \
            .select_filter_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(
                column=ClientsModuleConstantsUI.COLUMN_EMAIL,
                data=ClientsModuleConstantsUI.SHORT_EMAIL) \
            .click_crm_id_ui(row=2)
        ClientEditPageUI(self.driver)\
            .edit_client(
                day=WorkflowsConstants.DAY, month=WorkflowsConstants.MONTH, year=WorkflowsConstants.YEAR,
                list1=ClientEditConstantsUI.LIST_CITIZENSHIP, citizenship=WorkflowsConstants.CITIZENSHIP,
                field4=ClientEditConstantsUI.FIELD_CITY, city=WorkflowsConstants.CITY,
                field6=ClientEditConstantsUI.FIELD_P_CODE, p_code=WorkflowsConstants.P_CODE,
                list2=ClientEditConstantsUI.LIST_COUNTRY, country=WorkflowsConstants.COUNTRY_GUAM,
                button=ClientEditConstantsUI.BTN_SAVE)
        country = ClientDetailsPageUI(self.driver) \
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
            if counter == 3:
                break
