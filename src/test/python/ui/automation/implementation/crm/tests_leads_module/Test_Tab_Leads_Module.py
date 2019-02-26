import pytest

from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage


@pytest.mark.run(order=26)
class TabLeadsModuleCRM(BaseTest):

    def setUp(self):
        super(TabLeadsModuleCRM, self).setUp()
        self.lead1 = self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
        self.lead2 = self.load_lead_from_config(LeadsModuleConstants.SECOND_LEAD_INFO)

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def sorting_lead_module(self):
        LeadPrecondition(self.driver, self.config).sorting_leads()

    def test_mass_assign_leads(self):
        LeadPrecondition(self.driver, self.config).mass_assign_leads()
    # def test_mass_edit_leads(self):
    # def export_full_list(self):
    #
    # def export_select_records(self):
    # def import_leads(self):

    def test_searching_lead_modules(self):
        try:
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)

            CRMHomePage(self.driver)\
                .refresh_page()\
                .open_client_module()

            lead_module = CRMHomePage(self.driver)\
                .open_lead_module()

            lead_module.select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
            sleep(8)
            lead_module.perform_searching_lead_module(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_ASSIGNED_TO),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_SOURCE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_STATUS),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE))

            result_count = lead_module.get_results_count()
            self.assertEqual(1, result_count, "The number of expected search results does not match")
        except(ValueError, AssertionError, TimeoutError, TimeoutException, TypeError, NoSuchElementException):
            ClientProfilePage(self.driver).Sign_Out()
            LeadPrecondition(self.driver, self.config).create_lead(self.lead1)

            CRMHomePage(self.driver) \
                .refresh_page() \
                .open_client_module()

            lead_module = CRMHomePage(self.driver) \
                .open_lead_module()

            lead_module.select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))
            sleep(8)
            lead_module.perform_searching_lead_module(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LAST_NAME),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_ASSIGNED_TO),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_SOURCE),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LEAD_STATUS),
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                               LeadsModuleConstants.FIRST_LANGUAGE))

            result_count = lead_module.get_results_count()
            self.assertEqual(1, result_count, "The number of expected search results does not match")
