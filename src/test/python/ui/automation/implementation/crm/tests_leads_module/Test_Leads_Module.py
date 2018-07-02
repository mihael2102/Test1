from src.main.python.ui.crm.model.constants.LeadsModuleConstants import LeadsModuleConstants
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.lead_modules.LeadPrecondition import LeadPrecondition


class LeadModule(BaseTest):

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
        assigned_to = lead_profile.get_assigned_to_text()
        language = lead_profile.get_language_text()
        brand = lead_profile.get_brand_text()
        po_box = lead_profile.get_po_box_text()
        city = lead_profile.get_city_text()
        state = lead_profile.get_state_text()

        assert first_name == Config.data.get_data_first_lead_info(LeadsModuleConstants.FIRST_NAME)
        assert last_name == Config.data.get_data_first_lead_info(LeadsModuleConstants.LAST_NAME)
        assert mobile == Config.data.get_data_first_lead_info(LeadsModuleConstants.MOBILE)
        assert fax == Config.data.get_data_first_lead_info(LeadsModuleConstants.FAX)
        assert email == Config.data.get_data_first_lead_info(LeadsModuleConstants.EMAIL)
        assert secondary_email == Config.data.get_data_first_lead_info(LeadsModuleConstants.SECONDARY_EMAIL)
        assert source_name == Config.data.get_data_first_lead_info(LeadsModuleConstants.SOURCE_NAME)
        assert panda_partner_id_ == Config.data.get_data_first_lead_info(LeadsModuleConstants.PANDA_PARTNER)
        assert referral == Config.data.get_data_first_lead_info(LeadsModuleConstants.REFERRAL)
        assert street == Config.data.get_data_first_lead_info(LeadsModuleConstants.STREET)
        assert postal_code == Config.data.get_data_first_lead_info(LeadsModuleConstants.POSTAL_CODE)
        assert country == Config.data.get_data_first_lead_info(LeadsModuleConstants.COUNTRY)
        assert description == Config.data.get_data_first_lead_info(LeadsModuleConstants.DESCRIPTION)
        assert phone == Config.data.get_data_first_lead_info(LeadsModuleConstants.PHONE)
        assert tittle == Config.data.get_data_first_lead_info(LeadsModuleConstants.TITTLE)
        assert lead_source == Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_SOURCE)
        assert lead_status == Config.data.get_data_first_lead_info(LeadsModuleConstants.LEAD_STATUS)
        assert assigned_to == Config.data.get_data_first_lead_info(LeadsModuleConstants.ASSIGNED_TO)
        assert language == Config.data.get_data_first_lead_info(LeadsModuleConstants.LANGUAGE)
        assert brand == Config.data.get_data_first_lead_info(LeadsModuleConstants.BRAND)
        assert po_box == Config.data.get_data_first_lead_info(LeadsModuleConstants.PO_BOX)
        assert city == Config.data.get_data_first_lead_info(LeadsModuleConstants.CITY)
        assert state == Config.data.get_data_first_lead_info(LeadsModuleConstants.STATE)
