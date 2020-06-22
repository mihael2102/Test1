from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants


class AutoAssignDeletePreconditionUI(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def delete_rule(self):
        """ Login to CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
            url=self.config.get_value('url'),
            user_name=self.config.get_value(TestDataConstants.USER_NAME),
            password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
            otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .open_module_ui(TestDataConstants.MODULE_AUTO_ASSIGN)

        """ Delete rules """
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            "//iframe[@name='tradeChartFrame']"))

        AutoAssignPage(self.driver)\
            .perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.RULE_NAME)
        AutoAssignPage(self.driver).make_delete_rule() \
            .confirm_delete_rule() \
            .check_delete_message()

        AutoAssignPage(self.driver)\
            .perform_searching_auto_assign_module_by_name(AutoAssignConstants.SECOND_RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.SECOND_RULE_NAME)
        AutoAssignPage(self.driver).make_delete_rule() \
            .confirm_delete_rule() \
            .check_delete_message()
