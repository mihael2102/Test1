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
class DeleteWorkflowPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def delete_workflow_ui(self):
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

        """ Delete workflow """
        WorkflowsPage(self.driver) \
            .search_workflow_by_name(WorkflowsConstants.NAME_WORKFLOW) \
            .delete_workflow() \
            .confirmation_delete_workflow() \
            .search_workflow_by_name(WorkflowsConstants.NAME_WORKFLOW) \
            .check_workflow_not_found()
