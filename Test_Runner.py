import pytest

from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest


@pytest.mark.run(order=1)
def test_foo():
    sign = SignUpTest()
    sign.test_check_sign_up()


@pytest.mark.run(order=2)
def test_bar():
    ad = AddNewLiveAccountTestCA()
    ad.test_check_add_live_account_eur_currency()
