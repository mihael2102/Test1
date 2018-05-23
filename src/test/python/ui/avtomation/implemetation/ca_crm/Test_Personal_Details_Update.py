from src.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from src.main.python.ui.brand.model.client_area_modules.ca_constats.CAClientUpdate import CAClientUpdate
from src.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.avtomation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class Test_Personal_Details_Update(BaseTest):

    def test_perform_client_update_from_CA(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaStatusConstants.ACCOUNT_DETAILS)

        personal_information = CaAccountDetails().open_personal_information_tab() \
            .perform_change_personal_information(
            Config.data.get_data_client_information_update(CAClientUpdate.FIRST_NAME),
            Config.data.get_data_client_information_update(CAClientUpdate.LAST_NAME),
            Config.data.get_data_client_information_update(CAClientUpdate.DAY),
            Config.data.get_data_client_information_update(CAClientUpdate.MONTH),
            Config.data.get_data_client_information_update(CAClientUpdate.YEAR),
            Config.data.get_data_client_information_update(CAClientUpdate.COUNTRY),
            Config.data.get_data_client_information_update(CAClientUpdate.CITIZENSHIP),
            Config.data.get_data_client_information_update(CAClientUpdate.CITY),
            Config.data.get_data_client_information_update(CAClientUpdate.ZIPCODE),
            Config.data.get_data_client_information_update(CAClientUpdate.ADDRESS),
            Config.data.get_data_client_information_update(CAClientUpdate.PHONE)) \
            .perform_save_changed()

        date_birthday_ca = personal_information.get_date_birthday()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_client_information_update(CAClientUpdate.FIRST_NAME))

        first_name_crm = crm_client_profile.get_first_name()
        last_name_crm = crm_client_profile.get_last_name()
        date_birthday_crm = crm_client_profile.get_date_birthday()
        phone_crm = crm_client_profile.get_phone_text()
        citizenship_crm = crm_client_profile.get_citizenship_text()
        address_crm = crm_client_profile.get_address_text()
        city_crm = crm_client_profile.get_city_text()
        code_crm = crm_client_profile.get_code_text()
        country_crm = crm_client_profile.get_country_text()

        assert Config.data.get_data_client_information_update(CAClientUpdate.FIRST_NAME) == first_name_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.LAST_NAME) == last_name_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.PHONE) == phone_crm
        assert date_birthday_ca == date_birthday_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.CITIZENSHIP) == citizenship_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.ADDRESS) == address_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.CITY) == city_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.ZIPCODE) == code_crm
        assert Config.data.get_data_client_information_update(CAClientUpdate.COUNTRY) == country_crm


