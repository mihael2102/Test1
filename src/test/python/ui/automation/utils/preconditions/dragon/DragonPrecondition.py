from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.pages.usermanagement.UserManagementPage import UserManagementPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.UserInformation import UserInformation
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from time import sleep
import glob
from src.main.python.ui.crm.model.pages.dragon_page.DragonPage import DragonPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.crm.model.pages.leads.EditLeadsProfilePage import EditLeadsProfilePage


class DragonPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_dragon_clients(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)

        ' Go to User Management and make Login As DragonTest user: '
        CRMHomePage(self.driver).select_user_management()
        UserManagementPage(self.driver) \
            .open_crm_users_tab() \
            .click_remove_filter_btn() \
            .search_by_username(UserInformation.DRAGON_USER_NAME) \
            .check_user_found(UserInformation.DRAGON_USER_NAME) \
            .click_more_icon() \
            .click_login_as_icon()

        ' Create Lead with wrong phone number: '
        CRMHomePage(self.driver) \
            .open_lead_module() \
            .open_create_lead_module() \
            .perform_create_lead_short(DragonConstants.LEAD_LAST_NAME,
                                       DragonConstants.LEAD_EMAIL,
                                       DragonConstants.LEAD_ASSIGNED_TO,
                                       DragonConstants.PHONE_NUMBER_INVALID)
        sleep(1)
        ' Convert lead: '


    def check_dragon_leads(self):
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)

        ' Go to User Management and make Login As DragonTest user: '
        CRMHomePage(self.driver).select_user_management()
        UserManagementPage(self.driver) \
            .open_crm_users_tab() \
            .click_remove_filter_btn() \
            .search_by_username(UserInformation.DRAGON_USER_NAME) \
            .check_user_found(UserInformation.DRAGON_USER_NAME)\
            .click_more_icon()\
            .click_login_as_icon()

        ' Create Lead with wrong phone number: '
        CRMHomePage(self.driver)\
            .open_lead_module()\
            .open_create_lead_module()\
            .perform_create_lead_short(DragonConstants.LEAD_LAST_NAME,
                                       DragonConstants.LEAD_EMAIL,
                                       DragonConstants.LEAD_ASSIGNED_TO,
                                       DragonConstants.PHONE_NUMBER_INVALID)
        sleep(1)

        ' Check phone number in list view: '
        CRMHomePage(self.driver)\
            .open_lead_module()\
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver)\
            .check_invalid_phone_leads(DragonConstants.PHONE_NUMBER_INVALID)\
            .open_lead_personal_details()

        ' Check phone number in detail view: '
        DragonPage(self.driver)\
            .check_invalid_phone_leads(DragonConstants.PHONE_NUMBER_INVALID)

        ' Check phone number on edit page: '
        phone_edit_page = LeadDetailViewInfo(self.driver)\
            .open_edit_lead_profile()\
            .get_phone_edit_page()
        assert phone_edit_page == DragonConstants.PHONE_NUMBER_INVALID

        ' Update phone to another invalid number and verify on details view page: '
        EditLeadsProfilePage(self.driver)\
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID2)\
            .click_save()
        DragonPage(self.driver) \
            .check_invalid_phone_leads(DragonConstants.PHONE_NUMBER_INVALID2)
        LeadDetailViewInfo(self.driver)\
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID3) \
            .click_save()
        DragonPage(self.driver) \
            .check_invalid_phone_leads(DragonConstants.PHONE_NUMBER_INVALID3)

        ' Update phone to valid number and verify on details view page: '
        LeadDetailViewInfo(self.driver) \
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_VALID) \
            .click_save()
        DragonPage(self.driver) \
            .check_valid_phone_leads(DragonConstants.PHONE_NUMBER_HIDDEN)

        ' Check valid number in list view: '
        CRMHomePage(self.driver) \
            .open_lead_module() \
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME)) \
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver) \
            .check_valid_phone_leads(DragonConstants.PHONE_NUMBER_HIDDEN)