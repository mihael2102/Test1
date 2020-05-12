import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.login_ca.Deposit_CA_Preconditions import DepositCAPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import LoginCAPrecondition
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.CaUpdateClientPrecondition import \
    CaUpdateClientPrecondition
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.SignUpQ8Precondition import \
    SignUpQ8Precondition
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.CRMClientVerificationPreconditionUI import \
    CRMClientVerificationPreconditionUI
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.SignUpPrecondition import SignUpPrecondition


@pytest.mark.run(order=2)
class TestSignUpUI(BaseTest):

    def test_sign_up_ui(self):
        if global_var.current_brand_name == "q8":
            SignUpQ8Precondition(self.driver, self.config).sign_up_q8()
        else:
            SignUpPrecondition(self.driver, self.config).sign_up_ca_ui()

    def test_update_client_ui(self):
        CaUpdateClientPrecondition(self.driver, self.config).update_client_ca()

    def test_check_login(self):
        LoginCAPrecondition(self.driver, self.config).login_ca()

    def test_client_deposit_page_loading(self):
        DepositCAPrecondition(self.driver, self.config).client_deposit_page_loading()

    def test_registred_client_in_crm_ui(self):
        CRMClientVerificationPreconditionUI(self.driver, self.config).client_exist_in_crm_ui()

    def test_check_email_sign_up(self):
        LoginCAPrecondition(self.driver, self.config).check_email_sign_up()
