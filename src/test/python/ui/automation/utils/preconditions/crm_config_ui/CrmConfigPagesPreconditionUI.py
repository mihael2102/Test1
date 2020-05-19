import pytest
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage
import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
from src.main.python.ui.crm.model.constants.UserInformation import UserInformation


@pytest.mark.run(order=13)
class CrmConfigPagesPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def crm_config_pages_ui(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open CRM Configuration module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CRM_Config)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@class='dbiframe']"))
        CRMConfigurationPage(self.driver) \
            .check_common_configuration_loaded() \
            .check_brand_configuration_loaded() \
            .check_sms_configuration_loaded() \
            .check_smtp_configuration_loaded() \
            .check_minimum_deposit_loaded() \
            .check_cashier_loaded() \
            .check_manage_psp_loaded() \
            .check_click2call_loaded() \
            .check_referral_configuration_loaded() \
            .check_workflows_loaded() \
            .check_sharing_access_loaded()
