from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.deposit.CADeposit import CADeposit
from src.main.python.ui.brand.model.client_area_modules.deposit.CASuccessDeposit import CASuccessDeposit
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.test.python.ui.automation.BaseTest import BaseTest
from src.main.python.utils.config import Config
from src.test.python.utils.TestDataConstants import TestDataConstants


class DepositTestCa(BaseTest):

    def test_make_deposit_from_ca(self):
        BrandHomePage().open_first_tab_page(Config.url_client_area) \
            .login() \
            .set_fields(Config.data.get_data_client(TestDataConstants.E_MAIL),
                        Config.data.get_data_client(TestDataConstants.PASSWORD)) \
            .click_login_button() \
            .open_drop_down_menu() \
            .select_module(CaConstants.DEPOSIT)

        deposit_successful = CADeposit().select_payment_method(CaConstants.VISA) \
            .set_amount_deposit(CaConstants.AMOUNT_DEPOSIT) \
            .click_deposit_button() \
            .set_card_number(Config.data.get_data_client(TestDataConstants.CREDIT_CARD)) \
            .set_expiry_date(Config.data.get_data_client(TestDataConstants.EXPIRY_DATE)) \
            .set_expiry_year(Config.data.get_data_client(TestDataConstants.EXPIRY_YEAR)) \
            .set_cvc(Config.data.get_data_client(TestDataConstants.CVC)) \
            .perform_deposit() \
            .get_successful_deposit_message()

        amount_successful = CASuccessDeposit().get_amount_text()

        assert deposit_successful == CaConstants.SUCCESSFUL_DEPOSIT_MESSAGE
        assert amount_successful == CaConstants.SUCCESSFUL_AMOUNT_MESSAGE
