import pytest
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.login_ca.Deposit_CA_Preconditions import DepositCAPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import LoginCAPrecondition


@pytest.mark.run(order=2)
class SignUpTest(BaseTest):

    def test_check_sign_up(self):
        LoginCAPrecondition(self.driver, self.config).sign_up_ca()

    def test_check_login(self):
        LoginCAPrecondition(self.driver, self.config).login_ca()

    def test_client_deposit_page_loading(self):
        DepositCAPrecondition(self.driver, self.config).client_deposit_page_loading()

    def test_registred_client_exist_in_crm(self):
        LoginCAPrecondition(self.driver, self.config).client_exist_in_crm()

    def test_registred_client_in_crm_new_ui(self):
        LoginCAPrecondition(self.driver, self.config).client_exist_in_crm_new_ui()

    def test_check_email_sign_up(self):
        LoginCAPrecondition(self.driver, self.config).check_email_sign_up()
