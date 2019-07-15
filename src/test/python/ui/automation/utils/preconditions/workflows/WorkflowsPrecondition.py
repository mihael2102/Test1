from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4DepositModule import MT4DepositModule
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from time import sleep
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.mt4.credit_out.MT4CreditOutModule import MT4CreditOutModule
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.workflows.WorkflowsPage import WorkflowsPage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMConfigurationPage import CRMConfigurationPage
from src.main.python.ui.crm.model.pages.workflows.WorkflowsPage import WorkflowsPage
from src.main.python.ui.crm.model.constants.WorkflowsConstants import WorkflowsConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class WorkflowsPrecondition(object):
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_workflows(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_crm_configuration(CRMConstants.CRM_CONFIGURATION)
        CRMConfigurationPage(self.driver).check_workflows_loaded()
        WorkflowsPage(self.driver).click_add_new_workflow()\
                                  .enter_workflow_name(WorkflowsConstants.NAME_WORKFLOW)\
                                  .enter_workflow_priority(WorkflowsConstants.PRIORITY_WORKFLOW)\
                                  .click_radio_btn_modified()\
                                  .click_next()\
                                  .select_module(WorkflowsConstants.CLIENTS_MODULE)\
                                  .click_add_condition()\
                                  .select_accept_promotions(WorkflowsConstants.CLIENT_STATUS)\
                                  .select_condition(WorkflowsConstants.CONDITION_IS)

        if global_var.current_brand_name == "ptbanc" or global_var.current_brand_name == "kontofx" or \
                global_var.current_brand_name == "newforexstage2" or global_var.current_brand_name == "brokerz" \
                or global_var.current_brand_name == "4xfx":
            WorkflowsPage(self.driver).select_status(WorkflowsConstants.STATUS_B_TEST)
        elif global_var.current_brand_name == "gigafx":
            WorkflowsPage(self.driver).select_status(WorkflowsConstants.STATUS_R_NO_ANSWER)
        else:
            WorkflowsPage(self.driver).select_status(WorkflowsConstants.STATUS_TEST)

        WorkflowsPage(self.driver).click_add_condition() \
                                  .select_second_accept_promotions(WorkflowsConstants.COUNTRY) \
                                  .select_second_condition(WorkflowsConstants.CONDITION_IS) \
                                  .select_second_country(WorkflowsConstants.COUNTRY_AUSTRIA)\
                                  .select_condition_between(WorkflowsConstants.CONDITION_OR)\
                                  .click_add_condition()\
                                  .select_third_accept_promotions(WorkflowsConstants.EMAIl) \
                                  .select_third_conditions(WorkflowsConstants.CONDITION_CONTAINS) \
                                  .click_enter_email() \
                                  .enter_email(WorkflowsConstants.PANDATS_EMAIL) \
                                  .click_save_value() \
                                  .select_second_condition_between(WorkflowsConstants.CONDITION_AND) \
                                  .click_next() \
                                  .select_add_task(WorkflowsConstants.UPDATE_FIELD)\
                                  .enter_task_title(WorkflowsConstants.TASK_TITLE)\
                                  .click_add_field()\
                                  .select_field(WorkflowsConstants.ADDRESS)\
                                  .click_enter_value()\
                                  .enter_value(WorkflowsConstants.TEST_ADDRESS)\
                                  .click_save_value_task()\
                                  .click_add_field()\
                                  .select_second_field(WorkflowsConstants.COUNTRY)\
                                  .select_country(WorkflowsConstants.COUNTRY_ALBANIA)\
                                  .click_save_task()\
                                  .click_save_workflow()
        name_workflow = WorkflowsPage(self.driver).check_name_workflow(WorkflowsConstants.NAME_WORKFLOW)
        assert name_workflow == WorkflowsConstants.NAME_WORKFLOW

    def check_workflow_by_status(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver)\
            .open_client_module() \
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_first_client_by_email(WorkflowsConstants.PANDATS_EMAIL)
        if global_var.current_brand_name == "q8" or global_var.current_brand_name == "trade99":
            ClientProfilePage(self.driver).change_client_status_with_pencil(WorkflowsConstants.STATUS_TEST)
        elif global_var.current_brand_name == "gigafx":
            ClientProfilePage(self.driver).change_client_status_with_pencil(WorkflowsConstants.STATUS_R_NO_ANSWER)
        else:
            ClientProfilePage(self.driver).change_client_status_with_pencil(WorkflowsConstants.STATUS_B_TEST)
        CRMHomePage(self.driver).refresh_page()
        if global_var.current_brand_name == "q8":
            ClientProfilePage(self.driver).open_address_information()
        country = ClientProfilePage(self.driver).get_country_text()
        assert country == WorkflowsConstants.COUNTRY_ALBANIA
        address = ClientProfilePage(self.driver).get_address_text()
        assert address == WorkflowsConstants.TEST_ADDRESS

    def check_workflow_by_country(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        CRMHomePage(self.driver)\
            .open_client_module() \
            .select_filter(self.config.get_value(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_second_client_by_email(WorkflowsConstants.PANDATS_EMAIL)
        ClientProfilePage(self.driver).click_edit_personal_detail()
        ClientProfilePage(self.driver).select_country(WorkflowsConstants.COUNTRY_AUSTRIA)
        ClientProfilePage(self.driver).enter_date_birth(CRMConstants.DATE_BIRTH)
        ClientProfilePage(self.driver).click_save()
        sleep(2)
        CRMHomePage(self.driver).refresh_page()
        actual_country = ClientProfilePage(self.driver).get_country_text()
        expected_country = WorkflowsConstants.COUNTRY_ALBANIA
        actual_address = ClientProfilePage(self.driver).get_address_text()
        expected_address = WorkflowsConstants.TEST_ADDRESS

        # Check Address and Country fields were updated
        count = 0
        while expected_address != actual_address and expected_country != actual_country:
            CRMHomePage(self.driver).refresh_page()
            sleep(1)
            actual_country = ClientProfilePage(self.driver).get_country_text()
            actual_address = ClientProfilePage(self.driver).get_address_text()
            count += 1
            if count == 5:
                break
        assert actual_country == WorkflowsConstants.COUNTRY_ALBANIA
        assert actual_address == WorkflowsConstants.TEST_ADDRESS

    def delete_workflow(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        CRMHomePage(self.driver).open_crm_configuration(CRMConstants.CRM_CONFIGURATION)
        CRMConfigurationPage(self.driver).check_workflows_loaded()

        WorkflowsPage(self.driver).search_workflow_by_name(WorkflowsConstants.NAME_WORKFLOW)\
                                  .delete_workflow()\
                                  .confirmation_delete_workflow()\
                                  .search_workflow_by_name(WorkflowsConstants.NAME_WORKFLOW)\
                                  .check_workflow_not_found()
