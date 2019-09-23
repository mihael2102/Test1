import pytest
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import Login_CA_Precondition


@pytest.mark.run(order=2)
class SignUpTest(BaseTest):

    def test_check_sign_up(self):
        Login_CA_Precondition(self.driver, self.config).sign_up_ca()

    def test_registred_client_exist_in_crm(self):
        Login_CA_Precondition(self.driver, self.config).client_exist_in_crm()

    def test_check_email_sign_up(self):
        Login_CA_Precondition(self.driver, self.config).check_email_sign_up()
