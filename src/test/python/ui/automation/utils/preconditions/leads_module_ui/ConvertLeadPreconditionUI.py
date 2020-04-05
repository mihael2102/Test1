import pytest
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsModulePageUI import LeadsModulePageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.CreateLeadPageUI import CreateLeadPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsDetailsPageUI import LeadsDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsDetailsConstantsUI import LeadsDetailsConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.ConvertLeadPageUI import ConvertLeadPageUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


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
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Leads module """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_LEADS)

        """ Create New Lead """
        CreateLeadPageUI(self.driver)\
            .create_lead(
                field1=CreateLeadConstantsUI.FIELD_FNAME, fname=CreateLeadConstantsUI.FNAME,
                field2=CreateLeadConstantsUI.FIELD_LNAME, lname=CreateLeadConstantsUI.LNAME,
                field3=CreateLeadConstantsUI.FIELD_MOBILE, mobile=CreateLeadConstantsUI.MOBILE,
                field4=CreateLeadConstantsUI.FIELD_PHONE, phone=CreateLeadConstantsUI.PHONE,
                field5=CreateLeadConstantsUI.FIELD_EMAIL, email=CreateLeadConstantsUI.EMAIL,
                field6=CreateLeadConstantsUI.FIELD_S_EMAIL, s_mail=CreateLeadConstantsUI.S_EMAIL,
                field7=CreateLeadConstantsUI.FIELD_TITLE, title=CreateLeadConstantsUI.TITLE,
                list1=CreateLeadConstantsUI.LIST_LEAD_SOURCE, l_source=CreateLeadConstantsUI.L_SOURCE,
                list2=CreateLeadConstantsUI.LIST_LEAD_STATUS, l_status=CreateLeadConstantsUI.L_STATUS,
                list3=CreateLeadConstantsUI.LIST_ASSIGNED_TO, assigned_to=CreateLeadConstantsUI.ASSIGNED_TO,
                field8=CreateLeadConstantsUI.FIELD_LANGUAGE, language=CreateLeadConstantsUI.LANGUAGE,
                field9=CreateLeadConstantsUI.FIELD_SOURCE_NAME, source_name=CreateLeadConstantsUI.SOURCE_NAME,
                field10=CreateLeadConstantsUI.FIELD_FAX, fax=CreateLeadConstantsUI.FAX,
                field11=CreateLeadConstantsUI.FIELD_REFERRAL, referral=CreateLeadConstantsUI.REFERRAL,
                field12=CreateLeadConstantsUI.FIELD_ADDRESS, address=CreateLeadConstantsUI.ADDRESS,
                field13=CreateLeadConstantsUI.FIELD_POSTAL_CODE, p_code=CreateLeadConstantsUI.POSTAL_CODE,
                field14=CreateLeadConstantsUI.FIELD_CITY, city=CreateLeadConstantsUI.CITY,
                list4=CreateLeadConstantsUI.LIST_COUNTRY, country=CreateLeadConstantsUI.COUNTRY,
                field15=CreateLeadConstantsUI.FIELD_STATE, state=CreateLeadConstantsUI.STATE,
                field16=CreateLeadConstantsUI.FIELD_PO_BOX, po_box=CreateLeadConstantsUI.PO_BOX,
                field17=CreateLeadConstantsUI.FIELD_DESCRIPTION, description=CreateLeadConstantsUI.DESCRIPTION)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Search lead """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS) \
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
            .comparator_string(title, CreateLeadConstantsUI.TITLE) \
            .comparator_string(l_source, CreateLeadConstantsUI.L_SOURCE) \
            .comparator_string(l_status, CreateLeadConstantsUI.L_STATUS) \
            .comparator_string(assigned_to, CreateLeadConstantsUI.ASSIGNED_TO) \
            .comparator_string(language, CreateLeadConstantsUI.LANGUAGE) \
            .comparator_string(source_name, CreateLeadConstantsUI.SOURCE_NAME) \
            .comparator_string(referral, CreateLeadConstantsUI.REFERRAL) \
            .comparator_string(address, CreateLeadConstantsUI.ADDRESS) \
            .comparator_string(postal_code, CreateLeadConstantsUI.POSTAL_CODE) \
            .comparator_string(city, CreateLeadConstantsUI.CITY) \
            .comparator_string(country, CreateLeadConstantsUI.COUNTRY) \
            .comparator_string(state, CreateLeadConstantsUI.STATE) \
            .comparator_string(po_box, CreateLeadConstantsUI.PO_BOX) \
            .comparator_string(description, CreateLeadConstantsUI.DESCRIPTION)

        if "*" not in email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(email, CreateLeadConstantsUI.EMAIL)

        if "*" not in s_email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(s_email, CreateLeadConstantsUI.S_EMAIL) \

        if "*" not in phone:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(phone, CreateLeadConstantsUI.PHONE)

        if "*" not in mobile:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(mobile, CreateLeadConstantsUI.MOBILE)

        if "*" not in fax:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(fax, CreateLeadConstantsUI.FAX)

        """ Convert Lead """
        ConvertLeadPageUI(self.driver) \
            .convert_lead_ui(
                field1=ConvertLeadConstantsUI.FIELD_FNAME, first_name=ConvertLeadConstantsUI.FNAME,
                field2=ConvertLeadConstantsUI.FIELD_LNAME, last_name=ConvertLeadConstantsUI.LNAME,
                field4=ConvertLeadConstantsUI.FIELD_PHONE, phone=ConvertLeadConstantsUI.PHONE,
                day=ConvertLeadConstantsUI.DAY, month=ConvertLeadConstantsUI.MONTH, year=ConvertLeadConstantsUI.YEAR,
                list1=ConvertLeadConstantsUI.LIST_CITIZENSHIP, citizenship=ConvertLeadConstantsUI.CITIZENSHIP,
                list2=ConvertLeadConstantsUI.LIST_UI_LANGUAGE, ui_language=ConvertLeadConstantsUI.UI_LANGUAGE,
                field5=ConvertLeadConstantsUI.FIELD_ADDRESS, address=ConvertLeadConstantsUI.ADDRESS,
                field6=ConvertLeadConstantsUI.FIELD_POSTAL_CODE, postal_code=ConvertLeadConstantsUI.POSTAL_CODE,
                field7=ConvertLeadConstantsUI.FIELD_CITY, city=ConvertLeadConstantsUI.CITY,
                list3=ConvertLeadConstantsUI.LIST_COUNTRY, country=ConvertLeadConstantsUI.COUNTRY,
                field9=ConvertLeadConstantsUI.FIELD_PASSWORD, password=ConvertLeadConstantsUI.PASSWORD,
                list4=ConvertLeadConstantsUI.LIST_CURRENCY, currency=var.get_var(self.__class__.__name__)
                                                                                ["convert_lead_currency"],
                field10=ConvertLeadConstantsUI.FIELD_REFERRAL, referral=ConvertLeadConstantsUI.REFERRAL,
                list5=ConvertLeadConstantsUI.LIST_BRAND, brand=ConvertLeadConstantsUI.BRAND,
                field11=ConvertLeadConstantsUI.FIELD_SOURCE_NAME, source_name=ConvertLeadConstantsUI.SOURCE_NAME)

        """ Get client's data """
        details = ClientDetailsPageUI(self.driver)

        first_name = details\
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = details\
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_LNAME)
        email = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_EMAIL)
        phone = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_PHONE)
        birthday = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BIRTHDAY)
        citizenship = details \
            .get_text_from_field(var.get_var(self.__class__.__name__)["field_citizenship"])
        ui_language = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_UI_LANGUAGE)
        address = details \
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_ADDRESS)
        postal_code = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CODE)
        city = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CITY)
        country = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_COUNTRY)
        currency = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BASE_CURRENCY)
        referral = details \
            .open_tab(ClientDetailsConstantsUI.TAB_CUSTOM_INFORMATION) \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_REFERRAL)
        source_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_CLIENT_SOURCE)

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, ConvertLeadConstantsUI.FNAME) \
            .comparator_string(last_name, ConvertLeadConstantsUI.LNAME) \
            .comparator_string(birthday, ConvertLeadConstantsUI.BIRTHDAY) \
            .comparator_string(citizenship, ConvertLeadConstantsUI.CITIZENSHIP) \
            .comparator_string(currency, var.get_var(self.__class__.__name__)["convert_lead_currency"]) \
            .comparator_string(ui_language, ConvertLeadConstantsUI.UI_LANGUAGE) \
            .comparator_string(source_name, ConvertLeadConstantsUI.SOURCE_NAME) \
            .comparator_string(referral, ConvertLeadConstantsUI.REFERRAL) \
            .comparator_string(address, ConvertLeadConstantsUI.ADDRESS) \
            .comparator_string(postal_code, ConvertLeadConstantsUI.POSTAL_CODE) \
            .comparator_string(city, ConvertLeadConstantsUI.CITY) \
            .comparator_string(country, ConvertLeadConstantsUI.COUNTRY)

        if "*" not in email and "..." not in email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(email, CreateLeadConstantsUI.EMAIL)
        elif "*" not in email:
            email = email.replace('...', '')
            assert email in CreateLeadConstantsUI.EMAIL

        if phone and phone.isdecimal():
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(phone, ConvertLeadConstantsUI.PHONE)
