from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.mt4.deposit.MT4Deposit import MT4Deposit
from src.main.python.ui.crm.model.pages.client_profile.CRMClientProfilePage import CRMClientProfilePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.utils.TestDataConstants import TestDataConstants
from src.test.python.ui.avtomation.implemetation.crm.Test_Make_Deposit import Config


class CRMWithdrawPrecondition(object):

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
            .select_account_currency(Config.data.get_data_first_client(TestDataConstants.ACCOUNT_CURRENCY_CAD)) \
            .create_account_button()
        return CRMWithdrawPrecondition()

    def make_deposit(self):
        crm_client_profile = CRMLoginPage() \
            .open_second_tab_page(Config.url_crm) \
            .crm_login(Config.data.get_data_first_client(TestDataConstants.USER_NAME),
                       Config.data.get_data_first_client(TestDataConstants.CRM_PASSWORD)) \
            .select_filter(Config.data.get_data_first_client(TestDataConstants.FILTER)) \
            .find_client_by_email(Config.data.get_data_first_client(TestDataConstants.E_MAIL))

        account_number = crm_client_profile \
            .perform_scroll_down() \
            .open_trading_accounts_tab() \
            .get_client_account()

        CRMClientProfilePage() \
            .perform_scroll_up() \
            .open_mt4_actions(CRMConstants.DEPOSIT)

        MT4Deposit() \
            .make_deposit(account_number, CRMConstants.AMOUNT_WITHDRAW_SECOND, CRMConstants.PAYMENT_METHOD_DEPOSIT,
                          CRMConstants.STATUS_DEPOSIT, CRMConstants.DESCRIPTION_DEPOSIT) \
            .refresh_page()

        CRMClientProfilePage() \
            .click_trading_accounts_tab() \
            .get_amount_text(CRMConstants.AMOUNT_WITHDRAW_SECOND)
        return CRMWithdrawPrecondition()
