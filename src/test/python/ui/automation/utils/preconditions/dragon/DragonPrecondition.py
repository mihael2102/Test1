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
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
import glob
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.pages.dragon_page.DragonPage import DragonPage
from src.main.python.utils.logs.Loging import Logging
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.crm.model.pages.leads.EditLeadsProfilePage import EditLeadsProfilePage
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
from src.main.python.ui.crm.model.pages.client_profile.ClientProfileUpdate import ClientProfileUpdate
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants


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
        LeadViewInfo(self.driver)\
            .open_convert_lead_module()
        ConvertLeadModule(self.driver)\
            .perform_convert_lead_short(DragonConstants.FIRST_NAME_CONVERT,
                                        DragonConstants.BIRTHDAY_CONVERT,
                                        DragonConstants.ADDRESS_CONVERT,
                                        DragonConstants.POST_CODE_CONVERT,
                                        DragonConstants.CITY_CONVERT,
                                        DragonConstants.COUNTRY_CONVERT)
        try:
            confirmation_message = LeadViewInfo(self.driver)\
                .get_confirm_message_lead_view_profile()
            assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
            LeadViewInfo(self.driver)\
                .click_ok()
        except (TimeoutException, AssertionError, NoSuchElementException):
            Logging().reportDebugStep(self, "Lead convert message was not picked up")

        ' Check phone and email in Clients list view: '
        CRMHomePage(self.driver)\
            .open_client_module()\
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .enter_email(DragonConstants.LEAD_EMAIL)\
            .click_search_button()
        DragonPage(self.driver) \
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_LIST_VIEW)

        ' Check phone number and email in detail view: '
        ClientsPage(self.driver)\
            .open_client_id()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_DETAIL_VIEW)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

        ' Check phone number on edit page: '
        phone_edit_page = ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .get_phone_edit_page()
        assert phone_edit_page == DragonConstants.PHONE_NUMBER_INVALID

        ' Update phone to another invalid number and verify on details view page: '
        ClientProfileUpdate(self.driver)\
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID2)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID2)
        ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID3)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID3)

        ' Update phone to valid number and verify on details view page: '
        ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .set_phone(DragonConstants.PHONE_NUMBER_VALID)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)

        ' Check valid number and email in list view: '
        CRMHomePage(self.driver) \
            .open_client_module() \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .enter_email(DragonConstants.LEAD_EMAIL) \
            .click_search_button()
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

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

        ' Check phone number and email in list view: '
        CRMHomePage(self.driver)\
            .open_lead_module()\
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_LIST_VIEW)
        LeadsModule(self.driver)\
            .open_lead_personal_details()

        ' Check phone number and email in detail view: '
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_DETAIL_VIEW)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

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
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID2)
        LeadDetailViewInfo(self.driver)\
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID3) \
            .click_save()
        DragonPage(self.driver) \
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID3)

        ' Update phone to valid number and verify on details view page: '
        LeadDetailViewInfo(self.driver) \
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_VALID) \
            .click_save()
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)

        ' Check valid number and email in list view: '
        CRMHomePage(self.driver) \
            .open_lead_module() \
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME)) \
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

    def check_dragon_valid_phone(self):
        ' Sign up with valid phone: '
        CALoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url_ca')) \
            .click_sign_up()
        if (global_var.current_brand_name == "b-finance") or (global_var.current_brand_name == "eafx"):
            CALoginPage(self.driver) \
                .click_regulatory_confirmation()
        CALoginPage(self.driver) \
            .fill_first_name(DragonConstants.FIRST_NAME_CONVERT) \
            .fill_last_name(DragonConstants.LEAD_LAST_NAME) \
            .fill_email(DragonConstants.LEAD_EMAIL) \
            .fill_phone(DragonConstants.PHONE_NUMBER_VALID_CA) \
            .fill_password(CAConstants.PASSWORD)
        if global_var.current_brand_name != "q8":
            CALoginPage(self.driver)\
                .fill_confirm_password(CAConstants.PASSWORD) \
                .check_box_accept()
        CALoginPage(self.driver) \
            .click_submit()

        ' CRM login: '
        CRMLoginPage(self.driver)\
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))
        sleep(3)

        ' Assign the client to user, have not permission to see phone numbers: '
        ClientsPage(self.driver) \
            .find_client_by_email(DragonConstants.LEAD_EMAIL)\


        ' Go to User Management and make Login As DragonTest user: '
        CRMHomePage(self.driver)\
            .select_user_management() \
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
        LeadViewInfo(self.driver)\
            .open_convert_lead_module()
        ConvertLeadModule(self.driver)\
            .perform_convert_lead_short(DragonConstants.FIRST_NAME_CONVERT,
                                        DragonConstants.BIRTHDAY_CONVERT,
                                        DragonConstants.ADDRESS_CONVERT,
                                        DragonConstants.POST_CODE_CONVERT,
                                        DragonConstants.CITY_CONVERT,
                                        DragonConstants.COUNTRY_CONVERT)
        try:
            confirmation_message = LeadViewInfo(self.driver)\
                .get_confirm_message_lead_view_profile()
            assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
            LeadViewInfo(self.driver)\
                .click_ok()
        except (TimeoutException, AssertionError, NoSuchElementException):
            Logging().reportDebugStep(self, "Lead convert message was not picked up")

        ' Check phone and email in Clients list view: '
        CRMHomePage(self.driver)\
            .open_client_module()\
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .enter_email(DragonConstants.LEAD_EMAIL)\
            .click_search_button()
        DragonPage(self.driver) \
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_LIST_VIEW)

        ' Check phone number and email in detail view: '
        ClientsPage(self.driver)\
            .open_client_id()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_DETAIL_VIEW)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

        ' Check phone number on edit page: '
        phone_edit_page = ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .get_phone_edit_page()
        assert phone_edit_page == DragonConstants.PHONE_NUMBER_INVALID

        ' Update phone to another invalid number and verify on details view page: '
        ClientProfileUpdate(self.driver)\
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID2)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID2)
        ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID3)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID3)

        ' Update phone to valid number and verify on details view page: '
        ClientProfileUpdate(self.driver)\
            .click_edit_client_button()\
            .set_phone(DragonConstants.PHONE_NUMBER_VALID)\
            .click_save()\
            .refresh_page()
        DragonPage(self.driver)\
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)

        ' Check valid number and email in list view: '
        CRMHomePage(self.driver) \
            .open_client_module() \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .enter_email(DragonConstants.LEAD_EMAIL) \
            .click_search_button()
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

    def check_dragon_invalid_phone(self):
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

        ' Check phone number and email in list view: '
        CRMHomePage(self.driver)\
            .open_lead_module()\
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_LIST_VIEW)
        LeadsModule(self.driver)\
            .open_lead_personal_details()

        ' Check phone number and email in detail view: '
        DragonPage(self.driver)\
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID)\
            .check_email_address(DragonConstants.EMAIL_VALID_DETAIL_VIEW)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)

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
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID2)
        LeadDetailViewInfo(self.driver)\
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_INVALID3) \
            .click_save()
        DragonPage(self.driver) \
            .check_invalid_phone(DragonConstants.PHONE_NUMBER_INVALID3)

        ' Update phone to valid number and verify on details view page: '
        LeadDetailViewInfo(self.driver) \
            .open_edit_lead_profile() \
            .set_phone(DragonConstants.PHONE_NUMBER_VALID) \
            .click_save()
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)

        ' Check valid number and email in list view: '
        CRMHomePage(self.driver) \
            .open_lead_module() \
            .select_filter(
                self.config.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME)) \
            .perform_searching_lead_by_mail(DragonConstants.LEAD_EMAIL)
        DragonPage(self.driver) \
            .check_valid_phone(DragonConstants.PHONE_NUMBER_HIDDEN)\
            .check_email_in_send_mail_popup(DragonConstants.EMAIL_VALID_SEND_MAIL_POPUP)
