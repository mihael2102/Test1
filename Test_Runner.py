import pytest

from src.test.python.ui.automation.BaseTest import BaseTest
from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest


class Test_Runner(BaseTest):

    @pytest.mark.run(order=1)
    def test_sign_up(self):
        SignUpTest().test_check_sign_up()

    @pytest.mark.run(order=2)
    def test_check_live_accounts(self):
        live_accounts = AddNewLiveAccountTestCA()
        live_accounts.test_check_add_live_account_eur_currency()
        live_accounts.test_check_add_live_account_cad_currency()
        live_accounts.test_check_add_live_account_gbr_currency()
        live_accounts.test_check_add_live_account_jpy_currency()

    @pytest.mark.run(order=3)
    def test_check_demo_accounts(self):
        demo_accounts = AddDemoAccountsTestCA()
        demo_accounts.test_check_add_demo_account_usd_currency()
        demo_accounts.test_check_add_demo_account_eur_currency()
        demo_accounts.test_check_add_demo_account_gbr_currency()
        demo_accounts.test_check_add_demo_account_cad_currency()
