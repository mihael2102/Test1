import pytest
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import Login_CA_Precondition
from src.test.python.ui.automation.utils.preconditions.stratton_questionnaire.Stratton_Questionnaire_Precondition \
    import StrattonQuestionnairePrecondition


@pytest.mark.run(order=2)
class StrattonQuestionnaire(BaseTest):

    def test_customer_classification_empty(self):
        StrattonQuestionnairePrecondition(self.driver, self.config).customer_classification_empty()

    def test_customer_classification_blocked(self):
        StrattonQuestionnairePrecondition(self.driver, self.config).customer_classification_blocked()

    def test_customer_classification_negative(self):
        StrattonQuestionnairePrecondition(self.driver, self.config).customer_classification_negative()

    def test_customer_classification_retail(self):
        StrattonQuestionnairePrecondition(self.driver, self.config).customer_classification_retail()
