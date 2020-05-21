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

    def test_mass_edit_leads(self):
        LeadPrecondition(self.driver, self.config).mass_edit_leads()

    def export_full_list(self):
        LeadPrecondition(self.driver, self.config).export_full_list()

    def export_select_records(self):
        LeadPrecondition(self.driver, self.config).export_select_records()

    def import_leads(self):
        LeadPrecondition(self.driver, self.config).import_leads()

    def test_searching_lead_modules(self):
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
            first_name=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                      LeadsModuleConstants.FIRST_NAME),
            last_name=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                     LeadsModuleConstants.FIRST_LAST_NAME),
            assigned_to=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                       LeadsModuleConstants.FIRST_ASSIGNED_TO),
            tittle=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                  LeadsModuleConstants.FIRST_TITTLE),
            lead_source=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                       LeadsModuleConstants.FIRST_LEAD_SOURCE),
            lead_status=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                       LeadsModuleConstants.FIRST_LEAD_STATUS),
            language=self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                    LeadsModuleConstants.FIRST_LANGUAGE))

        result_count = lead_module.get_results_count()
        self.assertEqual(1, result_count, "The number of expected search results does not match")
