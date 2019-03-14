from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config


class AutoAssignPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def perform_add_rule(self, campaign):
        CRMHomePage().open_more_list_modules() \
            .select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
            .open_add_rule_module() \
            .perform_add_rule(AutoAssignConstants.RULE_NAME,
                              Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_BRAND),
                              Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_RULE_TYPE),
                              campaign, Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_DETAILS))

        return AutoAssignPrecondition()

    def perform_second_add_rule(self):
        CRMHomePage().open_more_list_modules() \
            .select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
            .open_add_rule_module() \
            .perform_second_add_rule(AutoAssignConstants.RULE_NAME,
                                     Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_BRAND),
                                     Config.data.get_data_auto_assign_info(AutoAssignConstants.THIRD_RULE_TYPE),
                                     Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_LANGUAGE),
                                     Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_DETAILS))

        return AutoAssignPrecondition()
