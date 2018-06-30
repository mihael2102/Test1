from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class TestDemo(BaseTest):

    def testing_tabs(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        "fdsfsdf") \
            .click_login_button().close_client_area_pop_up()

        # CRMLoginPage() \
        #     .open_second_tab_page(Config.url_crm) \
        #     .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
        #                Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD))


