from scr.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from scr.test.python.ui.avtomation.BaseTest import *
from scr.test.python.utils.TestDataConstants import TestDataConstants


class TestForgotPassword(BaseTest):

    def test_perform_forgot_password(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex) \
            .login() \
            .open_forgot_password_link() \
            .set_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL)) \
            .restore_password()
