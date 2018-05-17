from scr.main.python.ui.brand.model.client_area_modules.account_details.CaAccountDetails import CaAccountDetails
from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CAClientUpdate import CAClientUpdate
from scr.main.python.ui.brand.model.client_area_modules.ca_constats.CaStatusConstants import CaStatusConstants
from scr.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from scr.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.utils.TestDataConstants import TestDataConstants


class Test_Personal_Details_Update(BaseTest):

    def test_perform_client_update(self):
        # BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
        #     .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
        #                 Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
        #     .click_login_button() \
        #     .open_drop_down_menu() \
        #     .select_module(CaStatusConstants.ACCOUNT_DETAILS)
        #
        # personal_information = CaAccountDetails().open_personal_information_tab() \
        #     .perform_change_personal_information(
        #     Config.data.get_data_client_information_update(CAClientUpdate.FIRST_NAME),
        #     Config.data.get_data_client_information_update(CAClientUpdate.LAST_NAME),
        #     Config.data.get_data_client_information_update(CAClientUpdate.DAY),
        #     Config.data.get_data_client_information_update(CAClientUpdate.MONTH),
        #     Config.data.get_data_client_information_update(CAClientUpdate.YEAR),
        #     Config.data.get_data_client_information_update(CAClientUpdate.COUNTRY),
        #     Config.data.get_data_client_information_update(CAClientUpdate.CITIZENSHIP),
        #     Config.data.get_data_client_information_update(CAClientUpdate.CITY),
        #     Config.data.get_data_client_information_update(CAClientUpdate.ZIPCODE),
        #     Config.data.get_data_client_information_update(CAClientUpdate.ADDRESS),
        #     Config.data.get_data_client_information_update(CAClientUpdate.PHONE)) \
        #     .perform_save_changed()
        #
        # date_birthday_ca = personal_information.get_date_birthday()

        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                         Config.data.get_data_client_information_update(CAClientUpdate.FIRST_NAME))

        date_birthday_crm = crm_client_profile.get_date_birthday()
        get_city_text=crm_client_profile.get_city_text()


        # assert date_birthday_ca == date_birthday_crm
