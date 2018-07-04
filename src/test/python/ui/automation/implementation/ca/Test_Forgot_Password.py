from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.utils.TestDataConstants import TestDataConstants


class ForgotPasswordTestCA(BaseTest):

    def test_perform_forgot_password(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .login() \
            .open_forgot_password_link() \
            .set_email(Config.data.get_data_client(TestDataConstants.E_MAIL)) \
            .restore_password()
