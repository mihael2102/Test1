from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.clients_ui.ClientDetailsPageUI import ClientDetailsPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientDetailsConstantsUI import ClientDetailsConstantsUI
from src.main.python.ui.crm.model.pages.global_module_ui.CRMLoginPageUI import CRMLoginPageUI
from src.main.python.ui.crm.model.pages.crm_base_page.BaseMethodsPage import CRMBaseMethodsPage
from src.main.python.ui.crm.model.pages.global_module_ui.GlobalModulePageUI import GlobalModulePageUI
from src.main.python.ui.crm.model.constants_ui.base_crm_ui.FiltersConstantsUI import FiltersConstantsUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientsModuleConstantsUI import ClientsModuleConstantsUI
from src.main.python.ui.crm.model.pages.clients_ui.ClientsModulePageUI import ClientsModulePageUI
from src.main.python.ui.ca.model.constants.sign_up.SignUpFirstStepConstants import SignUpFirstStepConstants
from src.main.python.ui.crm.model.pages.clients_ui.ClientEditPageUI import ClientEditPageUI
from src.main.python.ui.crm.model.constants_ui.clients_ui.ClientEditConstantsUI import ClientEditConstantsUI
from src.main.python.ui.ca.model.constants.sign_up.CaUpdateClientConstants import CaUpdateClientConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.PersonalDetailsPage import PersonalDetailsPage
from src.main.python.ui.ca.model.constants.main_page.MainPageConstants import MainPageConstants
from src.main.python.ui.ca.model.constants.main_page.PersonalDetailsConstants import PersonalDetailsConstants
from src.main.python.ui.ca.model.pages.ca_pages_ui.MainPage import MainPage
from src.main.python.ui.ca.model.pages.ca_pages_ui.LoginPage import LoginPage


class CaUpdateClientPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def update_client_ca(self):
        """ Login CRM """
        CRMLoginPageUI(self.driver) \
            .crm_login(
                url=self.config.get_value('url'),
                user_name=self.config.get_value(TestDataConstants.USER_NAME),
                password=self.config.get_value(TestDataConstants.CRM_PASSWORD),
                otp_secret=self.config.get_value(TestDataConstants.OTP_SECRET))

        """ Open Clients module and find created client by email """
        CRMBaseMethodsPage(self.driver) \
            .open_module_ui(TestDataConstants.MODULE_CLIENTS)
        GlobalModulePageUI(self.driver) \
            .select_filter_new_ui(FiltersConstantsUI.FILTER_TEST_CLIENTS) \
            .set_data_column_field(ClientsModuleConstantsUI.COLUMN_EMAIL,
                                   SignUpFirstStepConstants.EMAIL)
        ClientsModulePageUI(self.driver) \
            .click_crm_id_ui('1')

        """ Edit Client via 'Edit' button """
        ClientEditPageUI(self.driver) \
            .edit_client(
                field1=ClientEditConstantsUI.FIELD_FNAME, fname=CaUpdateClientConstants.FNAME,
                field4=ClientEditConstantsUI.FIELD_LNAME, city=CaUpdateClientConstants.LNAME,
                day=CaUpdateClientConstants.DAY, month=CaUpdateClientConstants.MONTH, year=CaUpdateClientConstants.YEAR,
                button=ClientEditConstantsUI.BTN_SAVE)

        """ Log in CA """
        LoginPage(self.driver)\
            .open_second_tab_page(url=self.config.get_value('url_ca')) \
            .login(email=SignUpFirstStepConstants.EMAIL,
                   password=SignUpFirstStepConstants.PASSWORD) \
            .click_hi_user() \
            .click_main_menu_item(item=MainPageConstants.ITEM_PER_DETAILS)

        """ Get data from CA """
        first_name = PersonalDetailsPage(self.driver)\
            .get_data_from_text_field(field=PersonalDetailsConstants.FIELD_FNAME)
        last_name = PersonalDetailsPage(self.driver) \
            .get_data_from_text_field(field=PersonalDetailsConstants.FIELD_LNAME)
        day = PersonalDetailsPage(self.driver) \
            .get_data_from_list(pick_list=PersonalDetailsConstants.LIST_DAY)
        month = PersonalDetailsPage(self.driver) \
            .get_data_from_list(pick_list=PersonalDetailsConstants.LIST_MONTH)
        year = PersonalDetailsPage(self.driver) \
            .get_data_from_list(pick_list=PersonalDetailsConstants.LIST_YEAR)

        """ Check data was updated in CA """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, CaUpdateClientConstants.FNAME) \
            .comparator_string(last_name, CaUpdateClientConstants.LNAME) \
            .comparator_string(day, CaUpdateClientConstants.DAY) \
            .comparator_string(month, CaUpdateClientConstants.MONTH_CA) \
            .comparator_string(year, CaUpdateClientConstants.YEAR)

        """ Edit client via pencil in CRM """
        ClientDetailsPageUI(self.driver)\
            .open_tab(ClientDetailsConstantsUI.TAB_ADDRESS_INFORMATION) \
            .edit_text_field_via_pencil_icon(field=ClientDetailsConstantsUI.FIELD_CITY,
                                             text=CaUpdateClientConstants.CITY) \
            .edit_text_field_via_pencil_icon(field=ClientDetailsConstantsUI.FIELD_CODE,
                                             text=CaUpdateClientConstants.CODE) \
            .edit_text_field_via_pencil_icon(field=ClientDetailsConstantsUI.FIELD_ADDRESS,
                                             text=CaUpdateClientConstants.ADDRESS)

        """ Get data from CA """
        MainPage(self.driver) \
            .switch_second_tab_page() \
            .refresh_page_ca() \
            .click_hi_user() \
            .click_main_menu_item(item=MainPageConstants.ITEM_PER_DETAILS)
        city = PersonalDetailsPage(self.driver) \
            .get_data_from_text_field(field=PersonalDetailsConstants.FIELD_CITY)
        code = PersonalDetailsPage(self.driver) \
            .get_data_from_text_field(field=PersonalDetailsConstants.FIELD_ZIP)
        address = PersonalDetailsPage(self.driver) \
            .get_data_from_text_field(field=PersonalDetailsConstants.FIELD_ADDRESS)

        """ Check data was updated in CA """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(city, CaUpdateClientConstants.CITY) \
            .comparator_string(code, CaUpdateClientConstants.CODE) \
            .comparator_string(address, CaUpdateClientConstants.ADDRESS)

        """ Edit client in CA """
        PersonalDetailsPage(self.driver)\
            .update_personal_information(
                field4=PersonalDetailsConstants.FIELD_FNAME, f_name=CaUpdateClientConstants.FNAME2,
                field5=PersonalDetailsConstants.FIELD_LNAME, l_name=CaUpdateClientConstants.LNAME2,
                field1=PersonalDetailsConstants.FIELD_CITY, city=CaUpdateClientConstants.CITY2,
                field2=PersonalDetailsConstants.FIELD_ZIP, zip_code=CaUpdateClientConstants.CODE2,
                field3=PersonalDetailsConstants.FIELD_ADDRESS, address=CaUpdateClientConstants.ADDRESS2)

        """ Verify client's data was updated in CRM """
        first_name = ClientDetailsPageUI(self.driver)\
            .refresh_client_page() \
            .get_text_from_field(field=ClientDetailsConstantsUI.FIELD_FNAME)
        last_name = ClientDetailsPageUI(self.driver) \
            .get_text_from_field(field=ClientDetailsConstantsUI.FIELD_LNAME)
        city = ClientDetailsPageUI(self.driver) \
            .get_text_from_field(field=ClientDetailsConstantsUI.FIELD_CITY)
        code = ClientDetailsPageUI(self.driver) \
            .get_text_from_field(field=ClientDetailsConstantsUI.FIELD_CODE)
        address = ClientDetailsPageUI(self.driver) \
            .get_text_from_field(field=ClientDetailsConstantsUI.FIELD_ADDRESS)

        """ Check data was updated in CRM """
        CRMBaseMethodsPage(self.driver) \
            .comparator_string(first_name, CaUpdateClientConstants.FNAME2) \
            .comparator_string(last_name, CaUpdateClientConstants.LNAME2) \
            .comparator_string(city, CaUpdateClientConstants.CITY2) \
            .comparator_string(code, CaUpdateClientConstants.CODE2) \
            .comparator_string(address, CaUpdateClientConstants.ADDRESS2)
