import pytest
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage

@pytest.mark.run(order=35)
class CRMConfigurationsTest(BaseTest):

    def test_crm_configurations_pages_loading(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).open_crm_configuration(CRMConstants.CRM_CONFIGURATION)
        CRMConfigurationPage(self.driver).check_common_configuration_loaded() \
                                         .check_brand_configuration_loaded() \
                                         .check_sms_configuration_loaded() \
                                         .check_smtp_configuration_loaded() \
                                         .check_minimum_deposit_loaded() \
                                         .check_cashier_loaded() \
                                         .check_manage_psp_loaded() \
                                         .check_click2call_loaded() \
                                         .check_referral_configuration_loaded() \
                                         .check_workflows_loaded() \
                                         .check_sharing_access_loaded() \
                                         .check_email_templates_loaded()
