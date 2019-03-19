from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage


class AutoAssignPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def perform_add_lead_rule(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
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
        AutoAssignPage(self.driver).perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.RULE_NAME)

    def perform_add_client_rule(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
            .open_add_rule_module() \
            .set_rule_name(AutoAssignConstants.SECOND_RULE_NAME) \
            .select_brand_by_number() \
            .set_clients_module_check_box() \
            .set_assign_to_check_box() \
            .select_destination_user(AutoAssignConstants.USER) \
            .select_rule_type(AutoAssignConstants.RULE_TYPE1) \
            .select_item(AutoAssignConstants.COUNTRY) \
            .select_item(AutoAssignConstants.COUNTRY1) \
            .perform_submit() \
            .click_ok()
        AutoAssignPage(self.driver).perform_searching_auto_assign_module_by_name(AutoAssignConstants.SECOND_RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.RULE_NAME)

    def test_perform_delete_rule(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver).select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE)

        AutoAssignPage(self.driver).perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.RULE_NAME)
        AutoAssignPage(self.driver).make_delete_rule() \
                                   .confirm_delete_rule() \
                                   .check_delete_message()

        AutoAssignPage(self.driver).perform_searching_auto_assign_module_by_name(AutoAssignConstants.SECOND_RULE_NAME) \
            .get_rule_name_status(AutoAssignConstants.SECOND_RULE_NAME)
        AutoAssignPage(self.driver).make_delete_rule() \
            .confirm_delete_rule() \
            .check_delete_message()



    # def perform_add_rule(self, campaign):
    #     CRMHomePage().open_more_list_modules() \
    #         .select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
    #         .open_add_rule_module() \
    #         .perform_add_rule(AutoAssignConstants.RULE_NAME,
    #                           Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_BRAND),
    #                           Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_RULE_TYPE),
    #                           campaign, Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_DETAILS))
    #
    #     return AutoAssignPrecondition()
    #
    # def perform_second_add_rule(self):
    #     CRMHomePage().open_more_list_modules() \
    #         .select_auto_assign_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE) \
    #         .open_add_rule_module() \
    #         .perform_second_add_rule(AutoAssignConstants.RULE_NAME,
    #                                  Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_BRAND),
    #                                  Config.data.get_data_auto_assign_info(AutoAssignConstants.THIRD_RULE_TYPE),
    #                                  Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_LANGUAGE),
    #                                  Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_DETAILS))
    #
    #     return AutoAssignPrecondition()