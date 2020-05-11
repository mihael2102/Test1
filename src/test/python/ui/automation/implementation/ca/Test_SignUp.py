import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.login_ca.Deposit_CA_Preconditions import DepositCAPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import LoginCAPrecondition
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.SignUpStrattonPrecondition import \
    SignUpStrattonPrecondition
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.QuesDualixPrecondition import \
    QuesDualixPrecondition
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.SignUpQ8Precondition import \
    SignUpQ8Precondition
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.CRMClientVerificationPreconditionUI import \
    CRMClientVerificationPreconditionUI
from src.test.python.ui.automation.utils.preconditions.CA.sign_up.SignUpPrecondition import SignUpPrecondition


@pytest.mark.run(order=2)
class SignUpTest(BaseTest):

    def test_check_sign_up(self):
        if global_var.current_brand_name == "strattonmarkets-eu":
            SignUpStrattonPrecondition(self.driver, self.config).sign_up_stratton()
        elif global_var.current_brand_name == "dualix":
            QuesDualixPrecondition(self.driver, self.config).questionnaire_dualix()
        elif global_var.current_brand_name == "q8":
            SignUpQ8Precondition(self.driver, self.config).sign_up_q8()
        else:
            SignUpPrecondition(self.driver, self.config).sign_up_ca()

    def test_check_login(self):
        LoginCAPrecondition(self.driver, self.config).login_ca()

    def test_client_deposit_page_loading(self):
        DepositCAPrecondition(self.driver, self.config).client_deposit_page_loading()

    def test_registred_client_exist_in_crm(self):
        LoginCAPrecondition(self.driver, self.config).client_exist_in_crm()

    def test_registred_client_in_crm_new_ui(self):
        CRMClientVerificationPreconditionUI(self.driver, self.config).client_exist_in_crm_new_ui()

    def test_check_email_sign_up(self):
        LoginCAPrecondition(self.driver, self.config).check_email_sign_up()
