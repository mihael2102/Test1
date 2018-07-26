import pytest

from src.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from src.main.python.ui.brand.model.client_area_modules.constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.client_profile.ClientProfileUpdate import ClientProfileUpdate
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants


@pytest.mark.run(order=11)
class PersonalDetailsUpdateTestCA(BaseTest):

    def test_perform_client_update_from_CA(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.ACCOUNT_DETAILS)

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
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

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
            .crm_login(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.USER_NAME),
                       Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL))

        date_birthday_crm = crm_client_profile.get_date_birthday()

        client_profile_edit = ClientProfileUpdate()

        client_profile_edit.edit_first_name_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.SECOND_FIRST_NAME)) \
            .edit_last_name_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.LAST_NAME)) \
            .edit_phone_by_pencil(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PHONE)) \
            .edit_citizen_ship_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITIZEN_SHIP)) \
            .perform_scroll(300) \
            .edit_address_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.ADDRESS)) \
            .edit_post_code_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.POST_CODE)) \
            .edit_city_by_pencil(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.CITY)) \
            .edit_country_by_pencil(
            Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.FIRST_COUNTRY))

        BrandHomePage().open_second_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.CLIENT_ONE, TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.ACCOUNT_DETAILS)

        account_info_ca = CaAccountDetails().open_personal_information_tab()

        day_of_birthday_ca = account_info_ca.get_date_of_birthday()
        citizen = account_info_ca.get_citizen_ship_text()
        country = account_info_ca.get_country_text()

        assert date_birthday_crm == day_of_birthday_ca
        assert Config.data.get_data_client(TestDataConstants.CLIENT_ONE,TestDataConstants.CITIZEN_SHIP) == citizen
        assert Config.data.get_data_client(TestDataConstants.CLIENT_ONE,TestDataConstants.FIRST_COUNTRY) == country
