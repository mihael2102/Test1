from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class TestDemo(BaseTest):

    def testing_tabs(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button()

        # CRMLoginPage() \
        #     .open_second_tab_page(Config.url_crm) \
        #     .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
        #                Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))

        # BrandHomePageBrand() \
        #     .switch_first_tab_page() \
        #     .open_drop_down_menu() \
        #     .select_module(TestDataConstants.MANAGE_ACCOUNTS)
        #
        # CRMHomePage() \
        #     .switch_second_tab_page() \
        #     .refresh() \
        #     .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
        #     .find_client(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
        #                  Config.data.get_data_first_client(TestDataConstants.FIRST_NAME))
