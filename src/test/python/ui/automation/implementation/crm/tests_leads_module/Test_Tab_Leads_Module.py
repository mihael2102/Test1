from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition


class TabLeadsModuleCRM(BaseTest):

    def test_searching_lead_modules(self):
        LeadPrecondition().create_lead()

        CRMHomePage().refresh_page() \
            .open_client_module()

        lead_module = CRMHomePage().open_lead_module()

        lead_module.perform_searching_lead_module(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE))

        lead_module.perform_screen_shot_lead_module()
