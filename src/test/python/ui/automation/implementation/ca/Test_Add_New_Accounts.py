import pytest

from src.main.python.ui.brand.model.client_area_modules.constats.CaConstants import CaConstants
from src.main.python.ui.brand.model.client_area_modules.personal_details.CaManageAccounts import CaManageAccounts
from src.main.python.ui.brand.model.pages.home.BrandHomePage import BrandHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.pages.trading_account.TradingAccountsInformationPage import \
    TradingAccountsInformationPage
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import TradingAccountPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Page_CA_Preconditions import Page_CA_Precondition


@pytest.mark.run(order=5)
class AddNewAccountTestCA(BaseTest):

    def test_add_live_account_ca(self):
        TradingAccountPrecondition(self.driver, self.config).add_live_account()

    def test_add_demo_account_ca(self):
        TradingAccountPrecondition(self.driver, self.config).add_demo_account()

    def test_verify_accounts_in_crm(self):
        TradingAccountPrecondition(self.driver, self.config).verify_account_in_crm()

    def test_verify_accounts_in_crm_ui(self):
        TradingAccountPrecondition(self.driver, self.config).verify_account_in_crm_ui()

    def test_switch_between_accounts_ca(self):
        Page_CA_Precondition(self.driver, self.config).switch_between_accounts()
