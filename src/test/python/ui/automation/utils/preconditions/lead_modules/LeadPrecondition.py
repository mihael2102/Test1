from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage

class LeadPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def create_lead(self, lead):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD))

        CRMHomePage(self.driver).open_lead_module() \
            .open_create_lead_module()\


        if global_var.current_brand_name == "safemarkets":
            CreateLeadsProfilePage(self.driver).perform_create_lead(
            lead[LeadsModuleConstants.FIRST_NAME],
            lead[LeadsModuleConstants.FIRST_LAST_NAME],
            lead[LeadsModuleConstants.FIRST_MOBILE],
            lead[LeadsModuleConstants.FAX],
            lead[LeadsModuleConstants.EMAIL],
            lead[LeadsModuleConstants.SECONDARY_EMAIL],
            lead[LeadsModuleConstants.FIRST_LANGUAGE],
            lead[LeadsModuleConstants.PANDA_PARTNER],
            lead[LeadsModuleConstants.FIRST_REFERRAL],
            lead[LeadsModuleConstants.STREET],
            lead[LeadsModuleConstants.POSTAL_CODE],
            lead[LeadsModuleConstants.FIRST_COUNTRY],
            lead[LeadsModuleConstants.FIRST_DESCRIPTION],
            lead[LeadsModuleConstants.PHONE],
            lead[LeadsModuleConstants.FIRST_TITTLE],
            lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
            lead[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW],
            lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
            lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
            lead[LeadsModuleConstants.BRAND],
            lead[LeadsModuleConstants.PO_BOX],
            lead[LeadsModuleConstants.CITY],
            lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        elif global_var.current_brand_name == "fxpmarkets":
            CreateLeadsProfilePage(self.driver).perform_create_lead(
                lead[LeadsModuleConstants.FIRST_NAME],
                lead[LeadsModuleConstants.FIRST_LAST_NAME],
                lead[LeadsModuleConstants.FIRST_MOBILE],
                lead[LeadsModuleConstants.FAX],
                lead[LeadsModuleConstants.EMAIL],
                lead[LeadsModuleConstants.SECONDARY_EMAIL],
                lead[LeadsModuleConstants.FIRST_LANGUAGE],
                lead[LeadsModuleConstants.PANDA_PARTNER],
                lead[LeadsModuleConstants.FIRST_REFERRAL],
                lead[LeadsModuleConstants.STREET],
                lead[LeadsModuleConstants.POSTAL_CODE],
                lead[LeadsModuleConstants.FIRST_COUNTRY],
                lead[LeadsModuleConstants.FIRST_DESCRIPTION],
                lead[LeadsModuleConstants.PHONE],
                lead[LeadsModuleConstants.FIRST_TITTLE],
                lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                lead[LeadsModuleConstants.FIRST_LEAD_STATUS_C_NEW],
                lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
                lead[LeadsModuleConstants.BRAND],
                lead[LeadsModuleConstants.PO_BOX],
                lead[LeadsModuleConstants.CITY],
                lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        elif global_var.current_brand_name == "ogtrade":
            CreateLeadsProfilePage(self.driver).perform_create_lead_ogtrade(
                lead[LeadsModuleConstants.FIRST_NAME],
                lead[LeadsModuleConstants.FIRST_LAST_NAME],
                lead[LeadsModuleConstants.FIRST_MOBILE],
                lead[LeadsModuleConstants.FAX],
                lead[LeadsModuleConstants.EMAIL],
                lead[LeadsModuleConstants.SECONDARY_EMAIL],
                lead[LeadsModuleConstants.STREET],
                lead[LeadsModuleConstants.POSTAL_CODE],
                lead[LeadsModuleConstants.FIRST_DESCRIPTION],
                lead[LeadsModuleConstants.PHONE],
                lead[LeadsModuleConstants.FIRST_TITTLE],
                lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
                lead[LeadsModuleConstants.PO_BOX],
                lead[LeadsModuleConstants.CITY],
                lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

        else:

            CreateLeadsProfilePage(self.driver).perform_create_lead(
            lead[LeadsModuleConstants.FIRST_NAME],
            lead[LeadsModuleConstants.FIRST_LAST_NAME],
            lead[LeadsModuleConstants.FIRST_MOBILE],
            lead[LeadsModuleConstants.FAX],
            lead[LeadsModuleConstants.EMAIL],
            lead[LeadsModuleConstants.SECONDARY_EMAIL],
            lead[LeadsModuleConstants.FIRST_LANGUAGE],
            lead[LeadsModuleConstants.PANDA_PARTNER],
            lead[LeadsModuleConstants.FIRST_REFERRAL],
            lead[LeadsModuleConstants.STREET],
            lead[LeadsModuleConstants.POSTAL_CODE],
            lead[LeadsModuleConstants.FIRST_COUNTRY],
            lead[LeadsModuleConstants.FIRST_DESCRIPTION],
            lead[LeadsModuleConstants.PHONE],
            lead[LeadsModuleConstants.FIRST_TITTLE],
            lead[LeadsModuleConstants.FIRST_LEAD_SOURCE],
            lead[LeadsModuleConstants.FIRST_LEAD_STATUS],
            lead[LeadsModuleConstants.FIRST_ASSIGNED_TO],
            lead[LeadsModuleConstants.FIRST_SOURCE_NAME],
            lead[LeadsModuleConstants.BRAND],
            lead[LeadsModuleConstants.PO_BOX],
            lead[LeadsModuleConstants.CITY],
            lead[LeadsModuleConstants.FIRST_STATE])
            return LeadPrecondition(self.driver, self.config)

    def create_three_leads(self):
        CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD))

        home_page = CRMHomePage()
        home_page.open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        home_page.refresh_page() \
            .open_client_module()

        CRMHomePage().open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECOND_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.SECOND_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        home_page.refresh_page() \
            .open_client_module()

        CRMHomePage().open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead(
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.THIRD_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FAX),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_REFERRAL),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.STREET),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_DESCRIPTION),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PHONE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_SOURCE),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_LEAD_STATUS),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_ASSIGNED_TO),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO,
                                           LeadsModuleConstants.FIRST_SOURCE_NAME),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.BRAND),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.PO_BOX),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.CITY),
            self.config.get_data_lead_info(LeadsModuleConstants.THIRD_LEAD_INFO, LeadsModuleConstants.FIRST_STATE))

        return LeadPrecondition(self.driver, self.config)

    def edit_lead_profile(self, new_lead_data):

        if global_var.current_brand_name == "safemarkets":
            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.FIRST_REFERRAL],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        else:
            LeadDetailViewInfo(self.driver).open_edit_lead_profile().perform_edit_lead(
                new_lead_data[LeadsModuleConstants.FIRST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_LAST_NAME],
                new_lead_data[LeadsModuleConstants.FIRST_MOBILE],
                new_lead_data[LeadsModuleConstants.FAX],
                new_lead_data[LeadsModuleConstants.EMAIL],
                new_lead_data[LeadsModuleConstants.SECONDARY_EMAIL],
                new_lead_data[LeadsModuleConstants.FIRST_LANGUAGE],
                new_lead_data[LeadsModuleConstants.PANDA_PARTNER],
                new_lead_data[LeadsModuleConstants.FIRST_REFERRAL],
                new_lead_data[LeadsModuleConstants.STREET],
                new_lead_data[LeadsModuleConstants.POSTAL_CODE],
                new_lead_data[LeadsModuleConstants.FIRST_COUNTRY],
                new_lead_data[LeadsModuleConstants.FIRST_DESCRIPTION],
                new_lead_data[LeadsModuleConstants.PHONE],
                new_lead_data[LeadsModuleConstants.FIRST_TITTLE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE],
                new_lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS],
                new_lead_data[LeadsModuleConstants.FIRST_ASSIGNED_TO],
                new_lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME],
                new_lead_data[LeadsModuleConstants.BRAND],
                new_lead_data[LeadsModuleConstants.PO_BOX],
                new_lead_data[LeadsModuleConstants.CITY],
                new_lead_data[LeadsModuleConstants.FIRST_STATE])

        return LeadPrecondition(self.driver, self.config)
