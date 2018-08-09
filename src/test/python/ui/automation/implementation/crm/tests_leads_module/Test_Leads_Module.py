import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.main.python.ui.crm.model.constants.MassEditConstants import MassEditConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.modules.leads_module.LeadViewInfo import LeadViewInfo
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition


@pytest.mark.run(order=24)
class LeadModuleTest(BaseTest):

    def test_create_lead(self):
        LeadPrecondition().create_lead()

    def test_edit_lead(self):
        LeadPrecondition().create_lead()
        lead_profile = LeadPrecondition().edit_lead_profile()

        first_name = lead_profile.get_first_name_text()
        last_name = lead_profile.get_last_name_text()
        mobile = lead_profile.get_mobile_text()
        fax = lead_profile.get_fax_text()
        email = lead_profile.get_email_text()
        secondary_email = lead_profile.get_secondary_email_text()
        source_name = lead_profile.get_source_name_text()
        panda_partner_id_ = lead_profile.get_panda_partner_id_text()
        referral = lead_profile.get_referral_text()
        street = lead_profile.get_street_text()
        postal_code = lead_profile.get_postal_code_text()
        country = lead_profile.get_country_text()
        description = lead_profile.get_description_text()
        phone = lead_profile.get_phone_text()
        tittle = lead_profile.get_tittle_text()
        lead_source = lead_profile.get_lead_source_text()
        lead_status = lead_profile.get_lead_status_text()
        language = lead_profile.get_language_text()
        brand = lead_profile.get_brand_text()
        po_box = lead_profile.get_po_box_text()
        city = lead_profile.get_city_text()
        state = lead_profile.get_state_text()

        assert first_name == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_NAME)
        assert last_name == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LAST_NAME)
        assert mobile == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_MOBILE)
        assert fax == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FAX)
        assert email == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.EMAIL)
        assert secondary_email == Config.data.get_data_lead_info \
            (LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.SECONDARY_EMAIL)
        assert source_name == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_SOURCE_NAME)
        assert panda_partner_id_ == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PANDA_PARTNER)
        assert referral == Config.data.get_data_lead_info(LeadsModuleConstants.FIRST_LEAD_INFO,
                                                          LeadsModuleConstants.FIRST_REFERRAL)
        assert street == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.STREET)
        assert postal_code == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.POSTAL_CODE)
        assert country == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_COUNTRY)
        assert description == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_DESCRIPTION)
        assert phone == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PHONE)
        assert tittle == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_TITTLE)
        assert lead_source == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_SOURCE)
        assert lead_status == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LEAD_STATUS)
        assert language == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_LANGUAGE)
        assert brand == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.BRAND)
        assert po_box == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.PO_BOX)
        assert city == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.CITY)
        assert state == Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_LEAD_INFO, LeadsModuleConstants.FIRST_STATE)

    def test_mass_edit_lead(self):
        LeadPrecondition().create_three_leads()
        CRMHomePage().refresh_page() \
            .open_client_module()

        lead_module = CRMHomePage().open_lead_module()

        lead_module.select_filter(Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
                                                                 LeadsModuleConstants.FILTER_NAME)) \
            .select_three_records_task_module() \
            .open_mass_edit_task() \
            .perform_mass_edit(Config.data.get_data_lead_info(
            LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_TITTLE),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LEAD_SOURCE),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LEAD_STATUS),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_ASSIGNED_TO),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_LANGUAGE),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_SOURCE_NAME),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_REFERRAL),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_COUNTRY),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_UPDATE_LEAD, LeadsModuleConstants.SECOND_DESCRIPTION))

        assert lead_module.get_message_lead_module() == LeadsModuleConstants.MESSAGE_MASS_EDIT_SUCCESSFULY
        lead_module.click_ok().perform_screen_shot_lead_module()

    def test_mass_assign_lead_module(self):
        LeadPrecondition().create_three_leads()
        CRMHomePage().refresh_page() \
            .open_client_module()

        lead_module = CRMHomePage().open_lead_module()

        lead_module.select_filter(Config.data.get_data_lead_info(LeadsModuleConstants.LEADS_MODULE_COLUMNS,
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
        LeadPrecondition().create_lead()
        lead_view_profile_page = LeadViewInfo()

        lead_view_profile_page.open_convert_lead_module() \
            .perform_convert_lead(
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_NAME_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_LAST_NAME_LEAD),
            LeadsModuleConstants.FIRST_EMAIL_LEAD,
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_PHONE_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_BIRTHDAY_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_CITIZENSHIP),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_ADDRESS_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_POSTAL_CODE_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_CITY_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_COUNTRY_NAME),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_PASSWORD_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_CURRENCY_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_REFERRAL_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_BRAND_LEAD),
            Config.data.get_data_lead_info(
                LeadsModuleConstants.FIRST_CONVERT_LEAD, LeadsModuleConstants.FIRST_SOURCE_NAME))

        confirmation_message = lead_view_profile_page.get_confirm_message_lead_view_profile()
        assert confirmation_message == CRMConstants().CONVERT_SUCCESSFUL_MESSAGE
        lead_view_profile_page.click_ok()
