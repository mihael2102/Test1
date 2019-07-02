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
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.modules.leads_module.ConvertLeadModule import ConvertLeadModule
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage

from src.main.python.ui.crm.model.constants.AffiliateModuleConstants import AffiliateModuleConstants
from src.main.python.ui.crm.model.pages.affiliates.AffiliateListViewPage import AffiliateListViewPage
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.utils.config import Config
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.affiliates.AffiliatePage import AffiliatePage
from src.main.python.ui.crm.model.pages.api_page.ApiPage import ApiPage
from src.main.python.ui.crm.model.constants.APIConstants import APIConstants
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
import re
import time
from time import sleep


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

    def autorization_process(self):
        """ Login to CRM """
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        affiliate_list_view_page = CRMHomePage(self.driver).open_more_list_modules().select_affiliates_module_more_list(
            AffiliateModuleConstants.AFFILIATES_MODULE)


        AffiliatePage(self.driver).search_by_partner_id(APIConstants.PARTNER_ID)

        AffiliatePage(self.driver).open_edit_affiliate()
        selected_methods = AffiliatePage(self.driver).check_selected_methods()
        if "Selected" in selected_methods:
            AffiliatePage(self.driver).add_all_methods()
            selected_methods_new = AffiliatePage(self.driver).check_selected_methods()
            if "None selected" in selected_methods_new:
                AffiliatePage(self.driver).add_all_methods()
        else:
            AffiliatePage(self.driver).add_all_methods()

        selected_countries = AffiliatePage(self.driver).check_selected_countries()
        if "Selected" in selected_countries:
            AffiliatePage(self.driver).add_none_selected_countries()
            selected_countries_new = AffiliatePage(self.driver).check_selected_countries()
            if "None selected" in selected_countries_new:
                AffiliatePage(self.driver).click_submit()
            else:
                AffiliatePage(self.driver).add_none_selected_countries()
                AffiliatePage(self.driver).click_submit()
        else:
            AffiliatePage(self.driver).click_submit()

        secret_key = AffiliatePage(self.driver).copy_secret_key()

        api = affiliate_list_view_page.get_link_api()
        CRMLoginPage(self.driver).open_first_tab_page(api)
        ApiPage(self.driver).enter_secret_key(secret_key)
        ApiPage(self.driver).authorization_module()
        ApiPage(self.driver).input_partner_id(APIConstants.PARTNER_ID)

        ApiPage(self.driver).generate_time()
        ApiPage(self.driver).generate_accessKey()
        ApiPage(self.driver).send_authorization()
        check_token = ApiPage(self.driver).check_token()
        time.sleep(10)
        assert APIConstants.STATUS_OK in check_token

    def test_perform_convert_lead(self):
        if global_var.current_brand_name == "kayafx":
            self.autorization_process()
            ApiPage(self.driver).create_customer_module()
            ApiPage(self.driver).enter_email(self.client1[LeadsModuleConstants.EMAIL])
            ApiPage(self.driver).enter_password(self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD])
            ApiPage(self.driver).enter_country(APIConstants.COUNTRY)
            ApiPage(self.driver).enter_firstName(self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                                                     LeadsModuleConstants.FIRST_NAME])
            ApiPage(self.driver).enter_lastName(APIConstants.LASTNAME)
            ApiPage(self.driver).enter_phone(APIConstants.PHONE)
            ApiPage(self.driver).enter_refferal(APIConstants.REFFERAL)
            ApiPage(self.driver).send_create_customer()

            check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
            sleep(3)
            count = 0
            while APIConstants.STATUS_OK not in check_create_customer_token:
                sleep(2)
                check_create_customer_token = ApiPage(self.driver).check_create_customer_token()
                count += 1
                if count == 5:
                    break
            assert APIConstants.STATUS_OK in check_create_customer_token

            CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url'))
            ClientsPage(self.driver).select_filter(self.config.get_data_client(
                TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
                .find_client_by_email(self.client1[LeadsModuleConstants.EMAIL])
            client_email = ClientsPage(self.driver).get_first_client_email()
            client_country = ClientsPage(self.driver).get_client_country()
            client_first_name = ClientsPage(self.driver).get_client_first_name()
            client_last_name = ClientsPage(self.driver).get_client_last_name()
            client_phone = ClientsPage(self.driver).get_client_phone()
            ClientsPage(self.driver).click_custom_information()

            assert client_email == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                LeadsModuleConstants.EMAIL]
            assert client_country == APIConstants.COUNTRY_CRM
            assert client_first_name == self.load_lead_from_config(TestDataConstants.CLIENT_ONE)[
                LeadsModuleConstants.FIRST_NAME]
            assert client_last_name == APIConstants.LASTNAME
            assert client_phone == APIConstants.PHONE_CRM

        else:

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

            elif (global_var.current_brand_name == "oinvestsa") :
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
                    self.client1[LeadsModuleConstants.FIRST_COUNTRY_SA],
                    self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                    self.client1[LeadsModuleConstants.BRAND],
                    self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                    self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

            elif global_var.current_brand_name == "itrader_global":

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
                    self.client1[LeadsModuleConstants.FIRST_COUNTRY_ME],
                    self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_REFERRAL],
                    self.client1[LeadsModuleConstants.BRAND],
                    self.client1[LeadsModuleConstants.FIRST_SOURCE_NAME],
                    self.client1[LeadsModuleConstants.PHONE_AREA_CODE])

            elif (global_var.current_brand_name == "gmo") or (global_var.current_brand_name == "itrader") or \
                    (global_var.current_brand_name == "etfinance"):

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
                    self.client1[LeadsModuleConstants.FIRST_COUNTRY_GERMANY],
                    self.client1[LeadsModuleConstants.FIRST_PASSWORD_LEAD],
                    self.client1[LeadsModuleConstants.FIRST_CURRENCY_LEAD_EUR],
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
                assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE or CRMConstants().CONVERT_SUCCESSFUL_MESSAGE_EMPTY
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
        # source_name = lead_detail_view.get_source_name_text()
        panda_partner_id = lead_detail_view.get_panda_partner_id_text()

        if (global_var.current_brand_name != "rimarkets") and (global_var.current_brand_name != "ogtrade"):
            referral = lead_detail_view.get_referral_text()

        street = lead_detail_view.get_street_text()
        postal_code = lead_detail_view.get_postal_code_text()
        country = lead_detail_view.get_country_text()
        description = lead_detail_view.get_description_text()
        phone = lead_detail_view.get_phone_text()
        tittle = lead_detail_view.get_tittle_text()
        lead_source = lead_detail_view.get_lead_source_text()
        lead_status = lead_detail_view.get_lead_status_text()
        if global_var.current_brand_name != "ogtrade":
            language = lead_detail_view.get_language_text()
        else:
            po_box = lead_detail_view.get_po_box_text()

        # brand = lead_detail_view.get_brand_text()
        city = lead_detail_view.get_city_text()
        state = lead_detail_view.get_state_text()

        self.assertEqual(first_name, lead_data[LeadsModuleConstants.FIRST_NAME])
        self.assertEqual(last_name, lead_data[LeadsModuleConstants.FIRST_LAST_NAME])
        self.assertEqual(mobile, lead_data[LeadsModuleConstants.FIRST_MOBILE])
        self.assertEqual(fax, lead_data[LeadsModuleConstants.FAX])
        self.assertEqual(email, lead_data[LeadsModuleConstants.EMAIL])
        self.assertEqual(secondary_email, lead_data[LeadsModuleConstants.SECONDARY_EMAIL])
        # self.assertEqual(source_name, lead_data[LeadsModuleConstants.FIRST_SOURCE_NAME])

        self.assertEqual(street, lead_data[LeadsModuleConstants.STREET])
        self.assertEqual(postal_code, lead_data[LeadsModuleConstants.POSTAL_CODE])
        if (global_var.current_brand_name != "ogtrade") and (global_var.current_brand_name != "itrader") and \
                (global_var.current_brand_name != "itrader_global"):
            self.assertEqual(country, lead_data[LeadsModuleConstants.FIRST_COUNTRY])
            self.assertEqual(lead_source, lead_data[LeadsModuleConstants.FIRST_LEAD_SOURCE])
            if lead_data[LeadsModuleConstants.PANDA_PARTNER]:
                self.assertEqual(panda_partner_id, lead_data[LeadsModuleConstants.PANDA_PARTNER])
            if (global_var.current_brand_name != "gmo") and (global_var.current_brand_name != "gmo-dev") \
                    and (global_var.current_brand_name != "oinvestsa") and (global_var.current_brand_name != "itrader") \
                    and (global_var.current_brand_name != "otcapital") and (global_var.current_brand_name != "urf") \
                    and (global_var.current_brand_name != "rimarkets") and (global_var.current_brand_name != "itrader_global") \
                    and (global_var.current_brand_name != "ogtrade") and (global_var.current_brand_name != "fm-fx"):
                if lead_data[LeadsModuleConstants.FIRST_REFERRAL]:
                    self.assertEqual(referral, lead_data[LeadsModuleConstants.FIRST_REFERRAL])
        else:
            self.assertEqual(description, lead_data[LeadsModuleConstants.FIRST_DESCRIPTION])

        self.assertEqual(phone, lead_data[LeadsModuleConstants.PHONE])
        self.assertEqual(tittle, lead_data[LeadsModuleConstants.FIRST_TITTLE])

        if global_var.current_brand_name == "safemarkets":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW])
        elif global_var.current_brand_name == "forex_staging":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS1])
        elif global_var.current_brand_name == "ogtrade":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NEW_LEAD])
        elif (global_var.current_brand_name == "rimarkets") or (global_var.current_brand_name == "oinvestsa") or \
                (global_var.current_brand_name == "otcapital"):
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_TEST])
        elif global_var.current_brand_name == "fxpmarkets":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_C_NEW])
        elif global_var.current_brand_name == "itrader_global" or global_var.current_brand_name == "itrader":
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_NO_INTRS])
        elif global_var.current_brand_name == "gmo" or global_var.current_brand_name == "fm-fx":
            try:
                self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS_TEST_GMO])
            except:
                return self
        else:
            self.assertEqual(lead_status, lead_data[LeadsModuleConstants.FIRST_LEAD_STATUS])

        if global_var.current_brand_name != "ogtrade":
            self.assertEqual(language, lead_data[LeadsModuleConstants.FIRST_LANGUAGE])
        else:
            self.assertEqual(po_box, lead_data[LeadsModuleConstants.PO_BOX])
        # if lead_data[LeadsModuleConstants.BRAND]:
        #     self.assertEqual(brand, lead_data[LeadsModuleConstants.BRAND])
        self.assertEqual(city, lead_data[LeadsModuleConstants.CITY])
        self.assertEqual(state, lead_data[LeadsModuleConstants.FIRST_STATE])
        return True
