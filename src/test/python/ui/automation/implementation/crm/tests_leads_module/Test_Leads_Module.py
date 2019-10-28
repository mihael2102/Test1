import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.leads.LeadDetailViewInfo import LeadDetailViewInfo
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition
from selenium.common.exceptions import TimeoutException
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
from src.main.python.ui.crm.model.pages.document.DocumentsPage import DocumentsPage
from selenium.common.exceptions import NoSuchElementException
from src.main.python.ui.crm.model.constants.DragonConstants import DragonConstants
from src.main.python.ui.crm.model.pages.leads.CreateLeadsProfilePage import CreateLeadsProfilePage
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.modules.leads_module.LeadsModule import LeadsModule


@pytest.mark.run(order=24)
class LeadModuleTest(BaseTest):

    def setUp(self):
        super(LeadModuleTest, self).setUp()
        self.lead1 = self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
        self.lead2 = self.load_lead_from_config(LeadsModuleConstants.SECOND_LEAD_INFO)
        self.client1 = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)

    def test_edit_lead_pencil_icon(self):
        LeadPrecondition(self.driver, self.config).test_edit_lead_pencil_icon()

    def test_check_email_popup(self):
        LeadPrecondition(self.driver, self.config).check_email_popup()

    def test_create_lead(self):
        LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
        self.verify_lead(self.lead1)

    def test_create_edit_lead(self):
        LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
        self.verify_lead(self.lead1)
        LeadPrecondition(self.driver, self.config).edit_lead_profile(self.lead2)
        self.verify_lead(self.lead2)

    def test_mass_edit_lead(self):
        LeadPrecondition(self.driver, self.config).create_three_leads()
        CRMHomePage().refresh_page() \
            .open_client_module()

        lead_module = CRMHomePage().open_lead_module()

        lead_module.select_filter(self.config.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                                                 LeadsModuleConstants.FILTER_NAME)) \
            .select_three_records_task_module() \
            .open_mass_edit_task() \
            .perform_mass_edit(self.config.get_data_lead_info(LeadsModuleConstants.FIRST_UPDATE_LEAD,
                                                              LeadsModuleConstants.SECOND_TITTLE),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LEAD_SOURCE),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LEAD_STATUS),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_ASSIGNED_TO),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LANGUAGE),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_SOURCE_NAME),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_REFERRAL),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_COUNTRY),
                               self.config.get_data_lead_info(
                                   LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_DESCRIPTION))

        assert lead_module.get_message_lead_module() == LeadsModuleConstants.MESSAGE_MASS_EDIT_SUCCESSFULY
        lead_module.click_ok().perform_screen_shot_lead_module()

    def test_mass_assign_lead_module(self):
        LeadPrecondition(self.driver, self.config).create_three_leads()
        CRMHomePage().refresh_page() \
            .open_client_module()

        lead_module = CRMHomePage().open_lead_module()

        lead_module.select_filter(self.config.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                                                 LeadsModuleConstants.FILTER_NAME)) \
            .select_three_records_task_module() \
            .open_mass_assign_lead_module() \
            .search_user(MassEditConstants.USER_ONE) \
            .enter_check_box() \
            .click_save()

        confirmation_message = lead_module.get_confirm_message_lead_module()
        assert confirmation_message == CRMConstants().MASS_ASSIGN_MESSAGE
        lead_module.click_ok().perform_screen_shot_lead_module()

    def test_perform_convert_lead(self):
        LeadPrecondition(self.driver, self.config)\
            .create_lead(self.lead1)
        lead_view_profile_page = LeadViewInfo(self.driver)

        if global_var.current_brand_name == "newcrmui":
            CreateLeadsProfilePage(self.driver)\
                .verify_success_message()
            CRMHomePage(self.driver)\
                .click_ok()
            LeadsModule(self.driver)\
                .select_filter(self.config.get_data_lead_info(
                                LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME))\
                .enter_email(self.config.get_data_lead_info(
                                LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL))\
                .open_personal_details_lead()

        lead_view_profile_page\
            .open_convert_lead_module() \

        if global_var.current_brand_name == "mpcrypto":
            ConvertLeadModule(self.driver).perform_convert_lead(
                self.client1[LeadsModuleConstants.FIRST_NAME],
                self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                self.client1[LeadsModuleConstants.EMAIL],
                self.client1[LeadsModuleConstants.PHONE],
                self.client1[LeadsModuleConstants.BIRTHDAY],
                self.client1[LeadsModuleConstants.CITIZENSHIP],
                self.client1[LeadsModuleConstants.STREET],
                self.client1[LeadsModuleConstants.POSTAL_CODE],
                self.client1[LeadsModuleConstants.CITY],
                self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD_BCH],
                self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                self.client1[LeadsModuleConstants.BRAND],
                self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

        elif global_var.current_brand_name == "trade99":
            ConvertLeadModule(self.driver).perform_convert_lead(
                self.client1[LeadsModuleConstants.FIRST_NAME],
                self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                self.client1[LeadsModuleConstants.EMAIL],
                self.client1[LeadsModuleConstants.PHONE],
                self.client1[LeadsModuleConstants.BIRTHDAY],
                self.client1[LeadsModuleConstants.CITIZENSHIP],
                self.client1[LeadsModuleConstants.STREET],
                self.client1[LeadsModuleConstants.POSTAL_CODE],
                self.client1[LeadsModuleConstants.CITY],
                self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD_BTC],
                self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                self.client1[LeadsModuleConstants.BRAND],
                self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

        elif global_var.current_brand_name == "newcrmui":
            ConvertLeadModule(self.driver).perform_convert_lead_new_ui(
                self.client1[LeadsModuleConstants.FIRST_NAME],
                self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                self.client1[LeadsModuleConstants.EMAIL],
                self.client1[LeadsModuleConstants.PHONE],
                self.client1[LeadsModuleConstants.DAY],
                self.client1[LeadsModuleConstants.MONTH],
                self.client1[LeadsModuleConstants.YEAR],
                self.client1[LeadsModuleConstants.CITIZENSHIP],
                self.client1[LeadsModuleConstants.STREET],
                self.client1[LeadsModuleConstants.POSTAL_CODE],
                self.client1[LeadsModuleConstants.CITY],
                self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                self.client1[LeadsModuleConstants.BRAND],
                self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME])

        else:
            ConvertLeadModule(self.driver).perform_convert_lead(
                self.client1[LeadsModuleConstants.FIRST_NAME],
                self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                self.client1[LeadsModuleConstants.EMAIL],
                self.client1[LeadsModuleConstants.PHONE],
                self.client1[LeadsModuleConstants.BIRTHDAY],
                self.client1[LeadsModuleConstants.CITIZENSHIP],
                self.client1[LeadsModuleConstants.STREET],
                self.client1[LeadsModuleConstants.POSTAL_CODE],
                self.client1[LeadsModuleConstants.CITY],
                self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                self.client1[LeadsModuleConstants.BRAND],
                self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

        if global_var.current_brand_name == "newcrmui":
            CreateLeadsProfilePage(self.driver)\
                .verify_success_message()
            CRMHomePage(self.driver)\
                .click_ok()

        if global_var.current_brand_name != "newcrmui":
            convert_verified = False
            try:
                confirmation_message = lead_view_profile_page.get_confirm_message_lead_view_profile()
                assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
                lead_view_profile_page.click_ok()
                convert_verified = True
            except (TimeoutException, AssertionError, NoSuchElementException):
                Logging().reportDebugStep(self, "Lead convert message was not picked up")
            if not convert_verified:
                lead_detail_view = LeadDetailViewInfo(self.driver)
                lead_detail_view.wait_element_to_be_clickable("//input[@name='Edit']")
                self.assertEqual(' yes ', lead_detail_view.get_exists_text(), "Lead is not at exists state")

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def verify_lead(self, lead_data, converted=None):
        """
        Verify the lead displayed in the detail view against a lead_data dictionary
        :param lead_data: a dictionary containing lead data
        :return: returns True if the lead displayed matches the given lead_data
        :raise: asserts on non matching fields
        """
        lead_detail_view = LeadDetailViewInfo(self.driver)
        lead_detail_view.wait_element_to_be_clickable("//input[@name='Edit']")
        Logging().reportDebugStep(self, "Verifying lead data")

        first_name = lead_detail_view.get_first_name_text()
        last_name = lead_detail_view.get_last_name_text()
        mobile = lead_detail_view.get_mobile_text()
        fax = lead_detail_view.get_fax_text()
        email = lead_detail_view.get_email_text()
        secondary_email = lead_detail_view.get_secondary_email_text()
        source_name = lead_detail_view.get_source_name_text()
        panda_partner_id = lead_detail_view.get_panda_partner_id_text()
        referral = lead_detail_view.get_referral_text()
        street = lead_detail_view.get_street_text()
        postal_code = lead_detail_view.get_postal_code_text()
        country = lead_detail_view.get_country_text()
        description = lead_detail_view.get_description_text()
        phone = lead_detail_view.get_phone_text()
        tittle = lead_detail_view.get_tittle_text()
        lead_source = lead_detail_view.get_lead_source_text()
        lead_status = lead_detail_view.get_lead_status_text()
        po_box = lead_detail_view.get_po_box_text()
        city = lead_detail_view.get_city_text()
        state = lead_detail_view.get_state_text()

        # Verify First Name:
        self.assertEqual(first_name, lead_data[LeadsModuleConstants.FIRST_NAME])
        # Verify Last Name:
        self.assertEqual(last_name, lead_data[LeadsModuleConstants.FIRST_LAST_NAME])
        # Verify Mobile:
        try:
            self.assertEqual(mobile, lead_data[LeadsModuleConstants.FIRST_MOBILE])
        except(NoSuchElementException, TimeoutException, AssertionError):
            assert mobile == DragonConstants.PHONE_NUMBER_HIDDEN4 or \
                   mobile == DragonConstants.PHONE_NUMBER_HIDDEN3
        # Verify Fax:
        try:
            self.assertEqual(fax, lead_data[LeadsModuleConstants.FAX])
        except(NoSuchElementException, TimeoutException, AssertionError):
            assert fax == DragonConstants.PHONE_NUMBER_HIDDEN4 or \
                   fax == DragonConstants.PHONE_NUMBER_HIDDEN3
        # Verify Phone:
        try:
            self.assertEqual(phone, lead_data[LeadsModuleConstants.PHONE])
        except(NoSuchElementException, TimeoutException, AssertionError):
            assert phone == DragonConstants.PHONE_NUMBER_HIDDEN4 or \
                   phone == DragonConstants.PHONE_NUMBER_HIDDEN3
        # Verify Email:
        try:
            self.assertEqual(email, lead_data[LeadsModuleConstants.EMAIL])
        except(NoSuchElementException, TimeoutException, AssertionError):
            assert email == DragonConstants.EMAIL_VALID_DETAIL_VIEW4 or \
                   email == DragonConstants.EMAIL_VALID_DETAIL_VIEW3
        # Verify Secondary Email:
        try:
            self.assertEqual(secondary_email, lead_data[LeadsModuleConstants.SECONDARY_EMAIL])
        except(NoSuchElementException, TimeoutException, AssertionError):
            assert secondary_email == DragonConstants.EMAIL_VALID_DETAIL_VIEW4 or \
                   secondary_email == DragonConstants.EMAIL_VALID_DETAIL_VIEW3
        # Verify First source name:
        if global_var.current_brand_name != "marketsplus":
            self.assertEqual(source_name, lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME])
        # Verify Panda Partner:
        if lead_data[LeadsModuleConstants.PANDA_PARTNER] and global_var.current_brand_name != "marketsplus":
            self.assertEqual(panda_partner_id, lead_data[LeadsModuleConstants.PANDA_PARTNER])
        # Verify First Referral:
        if lead_data[LeadsModuleConstants.FIRST_REFERRAL] and global_var.current_brand_name != "marketsplus":
            self.assertEqual(referral, lead_data[LeadsModuleConstants.FIRST_REFERRAL])
        # Verify Street:
        self.assertEqual(street, lead_data[LeadsModuleConstants.STREET])
        # Verify Postal Code:
        self.assertEqual(postal_code, lead_data[LeadsModuleConstants.POSTAL_CODE])
        # Verify Country:
        self.assertEqual(country, lead_data[LeadsModuleConstants.FIRST_COUNTRY])
        # Verify Description:
        self.assertEqual(description, lead_data[LeadsModuleConstants.FIRST_DESCRIPTION])
        # Verify Title:
        self.assertEqual(tittle, lead_data[LeadsModuleConstants.FIRST_TITTLE])
        # Verify Lead Source:
        if global_var.current_brand_name != "marketsplus":
            self.assertEqual(lead_source, lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE])
        # Verify Lead Status:
        if global_var.current_brand_name == "safemarkets":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW])

        elif global_var.current_brand_name == "uft" or global_var.current_brand_name == "trade99":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_UFT])

        elif global_var.current_brand_name == "gxfx":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_B_TEST])

        elif global_var.current_brand_name == "solocapitlas":
            self.assertEqual(po_box, lead_data[LeadsModuleConstants.PO_BOX])

        elif global_var.current_brand_name == "gigafx":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_GIGA])

        else:
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS])

        self.assertEqual(po_box, lead_data[LeadsModuleConstants.PO_BOX])
        self.assertEqual(city, lead_data[LeadsModuleConstants.CITY])
        self.assertEqual(state, lead_data[LeadsModuleConstants.FIRST_STATE])
        return True

    def test_convert_lead_new_ui(self):
        LeadPrecondition(self.driver, self.config) \
            .create_lead(self.lead1)
        lead_view_profile_page = LeadViewInfo(self.driver)

        CreateLeadsProfilePage(self.driver) \
            .verify_success_message()
        CRMHomePage(self.driver) \
            .click_ok()
        LeadsModule(self.driver) \
            .select_filter_new_ui(self.config.get_data_lead_info(
                    LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FILTER_NAME)) \
            .enter_email(self.config.get_data_lead_info(
                    LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL)) \
            .open_personal_details_lead()

        lead_view_profile_page \
            .open_convert_lead_module() \

        ConvertLeadModule(self.driver)\
            .perform_convert_lead_new_ui(
                self.client1[LeadsModuleConstants.FIRST_NAME],
                self.client1[LeadsModuleConstants.FIRST_LAST_NAME],
                self.client1[LeadsModuleConstants.EMAIL],
                self.client1[LeadsModuleConstants.PHONE],
                self.client1[LeadsModuleConstants.DAY],
                self.client1[LeadsModuleConstants.MONTH],
                self.client1[LeadsModuleConstants.YEAR],
                self.client1[LeadsModuleConstants.CITIZENSHIP],
                self.client1[LeadsModuleConstants.STREET],
                self.client1[LeadsModuleConstants.POSTAL_CODE],
                self.client1[LeadsModuleConstants.CITY],
                self.client1[LeadsModuleConstants.FIRST_COUNTRY],
                self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                self.client1[LeadsModuleConstants.BRAND],
                self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME])

        CreateLeadsProfilePage(self.driver) \
            .verify_success_message()
        CRMHomePage(self.driver) \
            .click_ok()
