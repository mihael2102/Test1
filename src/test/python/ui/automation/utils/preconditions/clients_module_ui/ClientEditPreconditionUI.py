import pytest
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.ConvertLeadConstantsUI import ConvertLeadConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.leads_module_ui.LeadsModulePageUI import LeadsModulePageUI
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.clients_ui.ClientEditPageUI import ClientEditPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientEditConstantsUI import ClientEditConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.CreateLeadConstantsUI import CreateLeadConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.CreateLeadPageUI import CreateLeadPageUI
from src.main.python.ui.crm.model.constants_ui.leads_ui.LeadsModuleConstantsUI import LeadsModuleConstantsUI
from src.main.python.ui.crm.model.pages.leads_module_ui.ConvertLeadPageUI import ConvertLeadPageUI
import src.main.python.utils.data.globalVariableProvider.GlobalVariableProvider as var


@pytest.mark.run(order=13)
class ClientEditPreconditionUI(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def edit_client_ui(self):
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
        CreateLeadPageUI(self.driver) \
            .create_lead(
            field1=CreateLeadConstantsUI.FIELD_FNAME, fname=ClientEditConstantsUI.FNAME,
            field5=CreateLeadConstantsUI.FIELD_EMAIL, email=ClientEditConstantsUI.EMAIL,
            field2=CreateLeadConstantsUI.FIELD_LNAME, lname=ClientEditConstantsUI.LNAME,
            list3=CreateLeadConstantsUI.LIST_ASSIGNED_TO, assigned_to=CreateLeadConstantsUI.ASSIGNED_TO)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Search lead """
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_LEADS) \
            .set_data_column_field(column=LeadsModuleConstantsUI.COLUMN_EMAIL,
                                   data=ClientEditConstantsUI.EMAIL)
        LeadsModulePageUI(self.driver) \
            .open_lead('1')

        """ Convert Lead """
        ConvertLeadPageUI(self.driver) \
            .convert_lead_ui(
            field4=ConvertLeadConstantsUI.FIELD_PHONE, phone=ClientEditConstantsUI.PHONE,
            day=ConvertLeadConstantsUI.DAY, month=ConvertLeadConstantsUI.MONTH, year=ConvertLeadConstantsUI.YEAR,
            list1=ConvertLeadConstantsUI.LIST_CITIZENSHIP, citizenship=ConvertLeadConstantsUI.CITIZENSHIP,
            list2=ConvertLeadConstantsUI.LIST_UI_LANGUAGE, ui_language=ConvertLeadConstantsUI.UI_LANGUAGE,
            field5=ConvertLeadConstantsUI.FIELD_ADDRESS, address=ConvertLeadConstantsUI.ADDRESS,
            field6=ConvertLeadConstantsUI.FIELD_POSTAL_CODE, postal_code=ConvertLeadConstantsUI.POSTAL_CODE,
            field7=ConvertLeadConstantsUI.FIELD_CITY, city=ConvertLeadConstantsUI.CITY,
            list3=ConvertLeadConstantsUI.LIST_COUNTRY, country=ConvertLeadConstantsUI.COUNTRY,
            field9=ConvertLeadConstantsUI.FIELD_PASSWORD, password=ConvertLeadConstantsUI.PASSWORD,
            list5=ConvertLeadConstantsUI.LIST_BRAND, brand=ConvertLeadConstantsUI.BRAND)

        """ Edit Client """
        ClientEditPageUI(self.driver)\
            .edit_client(field1=ClientEditConstantsUI.FIELD_FNAME, fname=ClientEditConstantsUI.E_FNAME,
                         field4=ClientEditConstantsUI.FIELD_CITY, city=ClientEditConstantsUI.CITY,
                         list2=ClientEditConstantsUI.LIST_COUNTRY, country=ClientEditConstantsUI.COUNTRY,
                         button=ClientEditConstantsUI.BTN_SAVE)

        """ Verify successful message """
        GlobalModulePageUI(self.driver) \
            .verify_success_message() \
            .click_ok()

        """ Get client's data """
        details = ClientDetailsPageUI(self.driver)

        first_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_LNAME)
        email = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_EMAIL)
        phone = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_PHONE)
        birthday = details \
            .get_text_from_field(ClientDetailsConstantsUI.FIELD_BIRTHDAY)
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

        """ Verify client's data """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, ClientEditConstantsUI.E_FNAME) \
            .comparator_string(last_name, ClientEditConstantsUI.LNAME) \
            .comparator_string(birthday, ConvertLeadConstantsUI.BIRTHDAY) \
            .comparator_string(ui_language, ConvertLeadConstantsUI.UI_LANGUAGE) \
            .comparator_string(address, ConvertLeadConstantsUI.ADDRESS) \
            .comparator_string(postal_code, ConvertLeadConstantsUI.POSTAL_CODE) \
            .comparator_string(city, ClientEditConstantsUI.CITY) \
            .comparator_string(country, ClientEditConstantsUI.COUNTRY)

        if "*" not in email and "..." not in email:
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(email, ClientEditConstantsUI.EMAIL)
        elif "*" not in email:
            email = email.replace('...', '')
            assert email in ClientEditConstantsUI.EMAIL

        if phone and phone.isdecimal():
            CRMBaseMethodsPage(self.driver) \
                .comparator_string(phone, ClientEditConstantsUI.PHONE)
