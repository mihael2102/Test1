from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants


class AutoAssignLeadRulePreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def add_rule_lead(self):
        """ Login to CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_AUTO_ASSIGN)

        """ Create lead rule """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))

        AutoAssignPage(self.driver) \
            .open_add_rule_module() \
            .set_rule_name(AutoAssignConstants.RULE_NAME) \
            .select_brand_by_number() \
            .set_lead_module_check_box() \
            .set_assign_to_check_box() \
            .select_destination_user(AutoAssignConstants.USER) \
            .select_rule_type(AutoAssignConstants.RULE_TYPE1) \
            .select_item(AutoAssignConstants.COUNTRY) \
            .perform_submit() \
            .click_ok()
        AutoAssignPage(self.driver)\
            .perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.RULE_NAME)
