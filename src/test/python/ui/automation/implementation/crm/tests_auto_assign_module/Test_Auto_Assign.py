import pytest

from src.main.python.ui.crm.model.constants.AutoAssignConstants import AutoAssignConstants
from src.main.python.ui.crm.model.constants.CampaingsConstants import CampaignsConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.auto_assign.AutoAssignPage import AutoAssignPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.auto_assign.AutoAssignPrecondition import AutoAssignPrecondition
from src.test.python.ui.automation.utils.preconditions.campaigns.CampaignsPrecondition import CampaignsPrecondition


@pytest.mark.run(order=34)
class AutoAssignModuleTest(BaseTest):

    def test_add_auto_assign_rule(self):
        AutoAssignPrecondition(self.driver)




    # def test_perform_add_rule(self):
    #     CampaignsPrecondition().perform_create_new_campaigns()
    #     CRMHomePage().open_more_list_modules() \
    #         .select_audit_logs_module_more_list(AutoAssignConstants.AUTO_ASSIGN_MODULE)
    #
    #     AutoAssignPrecondition().perform_add_rule(CampaignsConstants.CAMPAIGN_NAME)
    #     auto_assign_module = AutoAssignPage()
    #     assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_MESSAGE
    #     auto_assign_module.click_ok()
    #
    #     auto_assign_module.perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME)
    #     assert auto_assign_module.get_rule_name_status(AutoAssignConstants.RULE_NAME)
    #     assert auto_assign_module.get_modules_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_MODULE),
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_MODULE))
    #     assert auto_assign_module.get_assign_to_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_TO))
    #     assert auto_assign_module.get_assigned_details_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_ASSIGN_DETAILS))
    #     assert auto_assign_module.get_rule_type_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_RULE_TYPE))
    #     assert auto_assign_module.get_status(Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_STATUS))
    #     assert auto_assign_module.get_brand_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_BRAND))
    #     assert auto_assign_module.get_created_by_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.CREATED_BY))
    #     assert auto_assign_module.get_date_created_status(
    #         AutoAssignConstants.TODAY_DATE.strftime(AutoAssignConstants.FORMAT_DATE))
    #
    # def test_perform_edit_rule(self):
    #     CRMLoginPage().open_first_tab_page(Config.url_crm) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET))
    #
    #     AutoAssignPrecondition().perform_second_add_rule()
    #     auto_assign_module = AutoAssignPage()
    #
    #     assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_MESSAGE
    #     auto_assign_module.click_ok()
    #
    #     auto_assign_module.perform_searching_auto_assign_module_by_name(
    #         AutoAssignConstants.RULE_NAME).click_edit_by_pencil() \
    #         .perform_edit_rule(AutoAssignConstants.SECOND_RULE_NAME,
    #                            Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_BRAND),
    #                            Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_USER),
    #                            Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_RULE_TYPE),
    #                            Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_CURRENCY))
    #
    #     assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_UPDATE_MESSAGE
    #     auto_assign_module.click_ok()
    #
    #     auto_assign_module.perform_searching_auto_assign_module_by_name(AutoAssignConstants.SECOND_RULE_NAME)
    #     assert auto_assign_module.get_rule_name_status(AutoAssignConstants.SECOND_RULE_NAME)
    #     assert auto_assign_module.get_modules_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_MODULE),
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_MODULE))
    #     assert auto_assign_module.get_assign_to_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_ASSIGN_TO))
    #     assert auto_assign_module.get_assigned_details_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_ASSIGN_DETAILS))
    #     assert auto_assign_module.get_rule_type_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_RULE_TYPE))
    #     assert auto_assign_module.get_status(Config.data.get_data_auto_assign_info(AutoAssignConstants.FIRST_STATUS))
    #     assert auto_assign_module.get_brand_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.SECOND_BRAND))
    #     assert auto_assign_module.get_created_by_status(
    #         Config.data.get_data_auto_assign_info(AutoAssignConstants.CREATED_BY))
    #     assert auto_assign_module.get_date_created_status(
    #         AutoAssignConstants.TODAY_DATE.strftime(AutoAssignConstants.FORMAT_DATE))
    #
    # def test_perform_delete_rule(self):
    #     CRMLoginPage().open_first_tab_page(Config.url_crm) \
    #         .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
    #                    self.config.get_value(TestDataConstants.CRM_PASSWORD),
    #                    self.config.get_value(TestDataConstants.OTP_SECRET))
    #
    #     AutoAssignPrecondition().perform_second_add_rule()
    #     auto_assign_module = AutoAssignPage()
    #
    #     assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_MESSAGE
    #     auto_assign_module.click_ok()
    #     auto_assign_module.perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME) \
    #         .make_delete_rule() \
    #         .confirm_delete_rule()
    #
    #     assert auto_assign_module.get_successfull_message() == AutoAssignConstants().SUCCESSFUL_DELETE_MESSAGE
    #     auto_assign_module.click_ok()
    #
    #     auto_assign_module.perform_searching_auto_assign_module_by_name(AutoAssignConstants.RULE_NAME)
    #     assert auto_assign_module.get_no_data_text() == AutoAssignConstants().NO_DATA_TEXT
