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
import src.main.python.utils.data.globals.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule

@pytest.mark.run(order=24)
class LeadModuleTest(BaseTest):

    def setUp(self):
        super(LeadModuleTest, self).setUp()
        self.lead1 = self.load_lead_from_config(LeadsModuleConstants.FIRST_LEAD_INFO)
        self.lead2 = self.load_lead_from_config(LeadsModuleConstants.SECOND_LEAD_INFO)
        self.client1 = self.load_lead_from_config(TestDataConstants.CLIENT_ONE)

    def test_create_lead(self):
        LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
        self.verify_lead(self.lead1)

    def test_edit_lead(self):
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
        LeadPrecondition(self.driver, self.config).create_lead(self.lead1)
        lead_view_profile_page = LeadViewInfo(self.driver)

        lead_view_profile_page.open_convert_lead_module() \

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


        convert_verified = False
        try:
            confirmation_message = lead_view_profile_page.get_confirm_message_lead_view_profile()
            assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
            lead_view_profile_page.click_ok()
            convert_verified = True
        except TimeoutException:
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
        language = lead_detail_view.get_language_text()
        # brand = lead_detail_view.get_brand_text()
        po_box = lead_detail_view.get_po_box_text()
        city = lead_detail_view.get_city_text()
        state = lead_detail_view.get_state_text()

        self.assertEqual(first_name, lead_data[LeadsModuleConstants.FIRST_NAME])
        self.assertEqual(last_name, lead_data[LeadsModuleConstants.FIRST_LAST_NAME])
        self.assertEqual(mobile, lead_data[LeadsModuleConstants.FIRST_MOBILE])
        self.assertEqual(fax, lead_data[LeadsModuleConstants.FAX])
        self.assertEqual(email, lead_data[LeadsModuleConstants.EMAIL])
        self.assertEqual(secondary_email, lead_data[LeadsModuleConstants.SECONDARY_EMAIL])
        self.assertEqual(source_name, lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME])
        if lead_data[LeadsModuleConstants.PANDA_PARTNER]:
            self.assertEqual(panda_partner_id, lead_data[LeadsModuleConstants.PANDA_PARTNER])
        if lead_data[LeadsModuleConstants.FIRST_REFERRAL]:
            self.assertEqual(referral, lead_data[LeadsModuleConstants.FIRST_REFERRAL])
        self.assertEqual(street, lead_data[LeadsModuleConstants.STREET])
        self.assertEqual(postal_code, lead_data[LeadsModuleConstants.POSTAL_CODE])
        self.assertEqual(country, lead_data[LeadsModuleConstants.FIRST_COUNTRY])
        self.assertEqual(description, lead_data[LeadsModuleConstants.FIRST_DESCRIPTION])
        self.assertEqual(phone, lead_data[LeadsModuleConstants.PHONE])
        self.assertEqual(tittle, lead_data[LeadsModuleConstants.FIRST_TITTLE])
        self.assertEqual(lead_source, lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE])
        self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS])
        self.assertEqual(language, lead_data[LeadsModuleConstants.FIRST_LANGUAGE])
        # if lead_data[LeadsModuleConstants.BRAND]:
        #     self.assertEqual(brand, lead_data[LeadsModuleConstants.BRAND])
        self.assertEqual(po_box, lead_data[LeadsModuleConstants.PO_BOX])
        self.assertEqual(city, lead_data[LeadsModuleConstants.CITY])
        self.assertEqual(state, lead_data[LeadsModuleConstants.FIRST_STATE])
        return True
