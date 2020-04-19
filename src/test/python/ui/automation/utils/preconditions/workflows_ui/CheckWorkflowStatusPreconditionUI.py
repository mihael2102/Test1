import pytest
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage
from src.test.python.ui.automation.utils.preconditions.workflows.WorkflowsPrecondition import WorkflowsPrecondition
from src.main.python.ui.crm.model.pages.workflows.WorkflowsPage import WorkflowsPage
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

        """ Create new workflow """
        name_workflow = WorkflowsPage(self.driver) \
            .click_add_new_workflow() \
            .enter_workflow_name(WorkflowsConstants.NAME_WORKFLOW) \
            .enter_workflow_priority(WorkflowsConstants.PRIORITY_WORKFLOW) \
            .click_radio_btn_modified() \
            .click_next() \
            .select_module(WorkflowsConstants.CLIENTS_MODULE) \
            .click_add_condition() \
            .select_accept_promotions(WorkflowsConstants.CLIENT_STATUS) \
            .select_condition(WorkflowsConstants.CONDITION_IS) \
            .select_status(var.get_var('WorkflowsPrecondition')["client_status"]) \
            .click_add_condition() \
            .select_second_accept_promotions(WorkflowsConstants.COUNTRY) \
            .select_second_condition(WorkflowsConstants.CONDITION_IS) \
            .select_second_country(WorkflowsConstants.COUNTRY_GUAM) \
            .select_condition_between(WorkflowsConstants.CONDITION_OR) \
            .click_add_condition() \
            .select_third_accept_promotions(WorkflowsConstants.EMAIl) \
            .select_third_conditions(WorkflowsConstants.CONDITION_CONTAINS) \
            .click_enter_email() \
            .enter_email(WorkflowsConstants.PANDATS_EMAIL) \
            .click_save_value() \
            .select_second_condition_between(WorkflowsConstants.CONDITION_AND) \
            .click_next() \
            .select_add_task(WorkflowsConstants.UPDATE_FIELD) \
            .enter_task_title(WorkflowsConstants.TASK_TITLE) \
            .click_add_field() \
            .select_field(WorkflowsConstants.ADDRESS) \
            .click_enter_value() \
            .enter_value(WorkflowsConstants.TEST_ADDRESS) \
            .click_save_value_task() \
            .click_add_field() \
            .select_second_field(WorkflowsConstants.COUNTRY) \
            .select_country(WorkflowsConstants.COUNTRY_ALBANIA) \
            .click_save_task() \
            .click_save_workflow() \
            .check_name_workflow(WorkflowsConstants.NAME_WORKFLOW)
        assert name_workflow == WorkflowsConstants.NAME_WORKFLOW
