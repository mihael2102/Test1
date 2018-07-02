from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads_pages.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class LeadPrecondition(object):

    def __init__(self) -> None:
        super().__init__()

    def create_lead(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_lead_module() \
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

        return LeadPrecondition()

    def edit_lead_profile(self):
        LeadDetailViewInfo().open_edit_lead_profile().perform_edit_lead(
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

        return LeadDetailViewInfo()
