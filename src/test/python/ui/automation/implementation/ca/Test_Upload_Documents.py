import pytest

from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.trading_account.TradingAccountPrecondition import TradingAccountPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Page_CA_Preconditions import Page_CA_Precondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Support_Ticket_Preconditions import Support_Ticket_Preconditions
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import LoginCAPrecondition
from src.test.python.ui.automation.utils.preconditions.login_ca.Page_CA_Preconditions import Page_CA_Precondition

@pytest.mark.run(order=5)
class UploadDocumentTestCa(BaseTest):

    def test_upload_document_ca(self):
        Page_CA_Precondition(self.driver, self.config).upload_document_ca()

    def test_check_and_update_document_in_crm(self):
        Page_CA_Precondition(self.driver, self.config).check_and_update_document_in_crm()

    def test_check_document_status_in_ca(self):
        Page_CA_Precondition(self.driver, self.config).check_document_status_in_ca()
