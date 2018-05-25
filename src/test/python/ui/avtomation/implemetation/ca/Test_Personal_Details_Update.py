from src.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.brand.model.client_area_modules.constats.CaStatusConstants import CaStatusConstants
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.client_profile.CRMClientUpdate import CRMClientUpdate
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class PersonalDetailsUpdateTestCA(BaseTest):

    def test_perform_client_update_from_CA(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex) \
            .login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.ACCOUNT_DETAILS)

        personal_information = CaAccountDetails().open_personal_information_tab() \
            .perform_change_personal_information(
            Config.data.get_data_client_information_update_ca(CAClientUpdate.FIRST_NAME),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.LAST_NAME),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.DAY),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.MONTH),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.YEAR),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.COUNTRY),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.CITIZEN_SHIP),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.CITY),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.ZIP_CODE),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.ADDRESS),
            Config.data.get_data_client_information_update_ca(CAClientUpdate.PHONE)) \
            .perform_save_changed()

        date_birthday_ca = personal_information.get_date_birthday()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        date_birthday_crm = crm_client_profile.get_date_birthday()
        phone_crm = crm_client_profile.get_phone_text()
        citizenship_crm = crm_client_profile.get_citizenship_text()
        address_crm = crm_client_profile.get_address_text()
        city_crm = crm_client_profile.get_city_text()
        code_crm = crm_client_profile.get_code_text()
        country_crm = crm_client_profile.get_country_text()

        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.FIRST_NAME) == first_name_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.LAST_NAME) == last_name_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.PHONE) == phone_crm
        assert date_birthday_ca == date_birthday_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.CITIZEN_SHIP) == citizenship_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.ADDRESS) == address_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.CITY) == city_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.ZIP_CODE) == code_crm
        assert Config.data.get_data_client_information_update_ca(CAClientUpdate.COUNTRY) == country_crm

    def test_perform_client_update_from_CRM(self):
        crm_client_profile = CRMLoginPage().open_first_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        date_birthday_crm = crm_client_profile.get_date_birthday()

        crm_client_profile.edit_client_profile_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.FIRST_NAME),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.FIRST_NAME_ELEMENT),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.EDIT_FIRST_NAME_FIELD),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.SAVE_FIRST_NAME_BUTTON)) \
            .edit_client_profile_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.LAST_NAME),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.LAST_NAME_ELEMENT),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.EDIT_LAST_NAME_FIELD),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.SAVE_LAST_NAME_BUTTON)) \
            .edit_client_profile_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.PHONE),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.PHONE_ELEMENT),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.EDIT_PHONE_FIELD),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.SAVE_PHONE_BUTTON)) \
            .edit_citizen_ship_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.CITIZEN_SHIP)) \
            .perform_scroll(300) \
            .edit_address_by_pencil(Config.data.get_data_first_client(TestDataConstants.ADDRESS)) \
            .edit_client_profile_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.POST_CODE),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.POST_CODE_ELEMENT),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.EDIT_POST_CODE_FIELD),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.SAVE_POST_CODE_BUTTON)) \
            .edit_client_profile_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.CITY),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.CITY_ELEMENT),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.EDIT_CITY_FIELD),
            Config.data.get_data_client_information_update_crm(CRMClientUpdate.SAVE_CITY_BUTTON)) \
            .edit_country_by_pencil(
            Config.data.get_data_first_client(TestDataConstants.FIRST_COUNTRY))

        BrandHomePage().open_second_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.ACCOUNT_DETAILS)

        account_info_ca = CaAccountDetails().open_personal_information_tab()

        day_of_birthday_ca = account_info_ca.get_date_of_birthday()
        citizen = account_info_ca.get_citizen_ship_text()
        country = account_info_ca.get_country_text()

        assert date_birthday_crm == day_of_birthday_ca
        assert Config.data.get_data_first_client(TestDataConstants.CITIZEN_SHIP) == citizen
        assert Config.data.get_data_first_client(TestDataConstants.FIRST_COUNTRY) == country
