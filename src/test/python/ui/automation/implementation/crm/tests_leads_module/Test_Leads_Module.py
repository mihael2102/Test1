from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


@pytest.mark.run(order=22)
class LeadModule(BaseTest):

    def test_create_lead(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        create_leads_module = CRMHomePage().open_lead_module() \
            .open_create_lead_module().perform_create_lead(
            Config.data.get_data_first_lead_info(LeadsModuleConstants.FIRST_NAME),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.LAST_NAME),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.MOBILE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.FAX),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.EMAIL),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.LANGUAGE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.REFERRAL),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.STREET),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.COUNTRY),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.DESCRIPTION),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.PHONE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.TITTLE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_SOURCE),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_STATUS),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.ASSIGNED_TO),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.SOURCE_NAME),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.BRAND),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.PO_BOX),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.CITY),
            Config.data.get_data_first_lead_info(LeadsModuleConstants.STATE))

    # def test_create_lead(self):
    #     CRMLoginPage().open_first_tab_page(Config.url_crm) \
    #         .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
    #                    Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))
    #
    #     create_leads_module = CRMHomePage().open_lead_module() \
    #         .open_create_lead_module().perform_create_lead(
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.FIRST_NAME),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.LAST_NAME),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.MOBILE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.FAX),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.EMAIL),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.SECONDARY_EMAIL),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.LANGUAGE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.PANDA_PARTNER),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.REFERRAL),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.STREET),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.POSTAL_CODE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.COUNTRY),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.DESCRIPTION),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.PHONE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.TITTLE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_SOURCE),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_STATUS),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.ASSIGNED_TO),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.SOURCE_NAME),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.BRAND),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.PO_BOX),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.CITY),
    #         Config.data.get_data_first_lead_info(LeadsModuleConstants.STATE))
    #
    #     create_leads_module.click_delete_button()
