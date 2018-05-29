from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.test.python.utils.TestDataConstants import TestDataConstants
from src.main.python.utils.config import Config


class CRMCreditOutPrecondition(object):

    def __init__(self) -> None:
        super().__init__()

    def add_live_account(self):
        BrandHomePage().open_first_tab_page(Config.url_new_forex).login() \
            .set_fields(Config.data.get_data_first_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_first_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.MANAGE_ACCOUNTS)

        CaManageAccounts().open_new_account_button() \
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_USD)) \
            .create_account_button()
        return CRMCreditInPrecondition()

    def make_credit_in(self):

        return CRMCreditInPrecondition()
