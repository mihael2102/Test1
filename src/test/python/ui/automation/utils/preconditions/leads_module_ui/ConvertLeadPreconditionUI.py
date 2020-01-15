import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalTablePageUI import GlobalTablePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsModulePageUI import LeadsModulePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.CreateLeadPageUI import CreateLeadPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsDetailsPageUI import LeadsDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsDetailsConstantsUI import LeadsDetailsConstantsUI


@pytest.mark.run(order=31)
class ConvertLeadPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def load_lead_from_config(self, lead_key):
        lead = self.config.get_value(lead_key)
        return lead

    def convert_lead_ui(self):
        """ Login CRM """
        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET)) \
            .select_filter(self.config.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER))

        CRMLoginPage(self.driver) \
            .open_first_tab_page(self.config.get_value('url'))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Create New Lead """
        CreateLeadPageUI(self.driver)\
            .create_lead(CreateLeadConstantsUI.FIELD_FNAME, CreateLeadConstantsUI.FNAME,
                         CreateLeadConstantsUI.FIELD_LNAME, CreateLeadConstantsUI.LNAME,
                         CreateLeadConstantsUI.FIELD_MOBILE, CreateLeadConstantsUI.MOBILE,
                         CreateLeadConstantsUI.FIELD_PHONE, CreateLeadConstantsUI.PHONE,
                         CreateLeadConstantsUI.FIELD_EMAIL, CreateLeadConstantsUI.EMAIL,
                         CreateLeadConstantsUI.FIELD_S_EMAIL, CreateLeadConstantsUI.S_EMAIL,
                         CreateLeadConstantsUI.FIELD_TITLE, CreateLeadConstantsUI.TITLE,
                         CreateLeadConstantsUI.LIST_LEAD_SOURCE, CreateLeadConstantsUI.L_SOURCE,
                         CreateLeadConstantsUI.LIST_LEAD_STATUS, CreateLeadConstantsUI.L_STATUS,
                         CreateLeadConstantsUI.LIST_ASSIGNED_TO, CreateLeadConstantsUI.ASSIGNED_TO,
                         CreateLeadConstantsUI.FIELD_LANGUAGE, CreateLeadConstantsUI.LANGUAGE,
                         CreateLeadConstantsUI.FIELD_SOURCE_NAME, CreateLeadConstantsUI.SOURCE_NAME,
                         CreateLeadConstantsUI.FIELD_FAX, CreateLeadConstantsUI.FAX,
                         CreateLeadConstantsUI.FIELD_REFERRAL, CreateLeadConstantsUI.REFERRAL,
                         CreateLeadConstantsUI.FIELD_ADDRESS, CreateLeadConstantsUI.ADDRESS,
                         CreateLeadConstantsUI.FIELD_POSTAL_CODE, CreateLeadConstantsUI.POSTAL_CODE,
                         CreateLeadConstantsUI.FIELD_CITY, CreateLeadConstantsUI.CITY,
                         CreateLeadConstantsUI.LIST_COUNTRY, CreateLeadConstantsUI.COUNTRY,
                         CreateLeadConstantsUI.FIELD_STATE, CreateLeadConstantsUI.STATE,
                         CreateLeadConstantsUI.FIELD_PO_BOX, CreateLeadConstantsUI.PO_BOX,
                         CreateLeadConstantsUI.FIELD_DESCRIPTION, CreateLeadConstantsUI.DESCRIPTION)

        """ Verify successful message """
        GlobalTablePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Search lead """
        CRMBaseMethodsPage(self.driver) \
            .open_tab_list_view_ui(LeadsModuleConstantsUI.TAB_ALL)
        GlobalTablePageUI(self.driver)\
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=CreateLeadConstantsUI.EMAIL)

        """ Open lead and get data """
        LeadsModulePageUI(self.driver) \
            .open_lead()

        details = LeadsDetailsPageUI(self.driver)

        first_name = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_FNAME)

        last_name = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_LNAME)

        mobile = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_MOBILE)

        phone = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_PHONE)

        email = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_EMAIL)

        s_email = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_S_EMAIL)

        title = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_TITLE)

        l_source = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_LEAD_SOURCE)

        l_status = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_LEAD_STATUS)

        assigned_to = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_ASSIGNED_TO)

        language = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_LANGUAGE)

        source_name = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_SOURCE_NAME)

        fax = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_FAX)

        referral = details \
            .open_tab(LeadsDetailsConstantsUI.TAB_CUSTOM_INFORMATION) \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_REFERRAL)

        address = details \
            .open_tab(LeadsDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_STREET)

        postal_code = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_POSTAL_CODE)

        city = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_CITY)

        country = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_COUNTRY)

        state = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_STATE)

        po_box = details \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_PO_BOX)

        description = details \
            .open_tab(LeadsDetailsConstantsUI.TAB_DESCRIPTION_INFORMATION) \
            .get_text_from_field(LeadsDetailsConstantsUI.FIELD_DESCRIPTION)

        """ Verify lead's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, CreateLeadConstantsUI.FNAME) \
            .comparator_string(last_name, CreateLeadConstantsUI.LNAME) \
            .comparator_string(mobile, CreateLeadConstantsUI.MOBILE) \
            .comparator_string(phone, CreateLeadConstantsUI.PHONE) \
            .comparator_string(email, CreateLeadConstantsUI.EMAIL) \
            .comparator_string(s_email, CreateLeadConstantsUI.S_EMAIL) \
            .comparator_string(title, CreateLeadConstantsUI.TITLE) \
            .comparator_string(l_source, CreateLeadConstantsUI.L_SOURCE) \
            .comparator_string(l_status, CreateLeadConstantsUI.L_STATUS) \
            .comparator_string(assigned_to, CreateLeadConstantsUI.ASSIGNED_TO) \
            .comparator_string(language, CreateLeadConstantsUI.LANGUAGE) \
            .comparator_string(source_name, CreateLeadConstantsUI.SOURCE_NAME) \
            .comparator_string(fax, CreateLeadConstantsUI.FAX) \
            .comparator_string(referral, CreateLeadConstantsUI.REFERRAL) \
            .comparator_string(address, CreateLeadConstantsUI.ADDRESS) \
            .comparator_string(postal_code, CreateLeadConstantsUI.POSTAL_CODE) \
            .comparator_string(city, CreateLeadConstantsUI.CITY) \
            .comparator_string(country, CreateLeadConstantsUI.COUNTRY) \
            .comparator_string(state, CreateLeadConstantsUI.STATE) \
            .comparator_string(po_box, CreateLeadConstantsUI.PO_BOX) \
            .comparator_string(description, CreateLeadConstantsUI.DESCRIPTION)

        """ Convert Lead """

