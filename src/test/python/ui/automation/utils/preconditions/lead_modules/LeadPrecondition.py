from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class LeadPrecondition(object):

    def __init__(self) -> None:
        super().__init__()

    def create_lead(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        CRMHomePage().open_lead_module() \
            .open_create_lead_module().perform_create_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        return LeadPrecondition()

    def create_three_leads(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        home_page = CRMHomePage()
        home_page.open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))
        home_page.refresh_page()\
            .open_client_module() \
            .open_lead_module() \
            .open_create_lead_module()\
            .perform_create_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECOND_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FAX),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.STREET),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PHONE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.BRAND),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.CITY),
            Config.data.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))
        home_page.refresh_page()\
            .open_client_module()\
            .open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.THIRD_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FAX),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.STREET),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PHONE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.BRAND),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.CITY),
            Config.data.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        return LeadPrecondition()

    def edit_lead_profile(self):
        LeadDetailViewInfo().open_edit_lead_profile().perform_edit_lead(
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LAST_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.SECONDARY_EMAIL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.PANDA_PARTNER),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_ASSIGNED_TO),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY),
            Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        return LeadDetailViewInfo()
