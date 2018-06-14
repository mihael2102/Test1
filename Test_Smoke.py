import pytest
from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_Change_Password import ChangePasswordTestCA
from src.test.python.ui.automation.implementation.ca.Test_Download_Documents import DownloadDocumentsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Deposit import DepositTestCa
from src.test.python.ui.automation.implementation.ca.Test_Make_Transfer_Funds import TransferFundsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Withdraw import WithdrawTestCA
from src.test.python.ui.automation.implementation.ca.Test_Personal_Details_Update import PersonalDetailsUpdateTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa
from src.test.python.ui.automation.implementation.crm.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.Test_Change_Password import ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Check_Password import CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_Out import CreditOutTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Deposit import DepositTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Transfer_Between_Ta import TransferBetweenTa


class TestSmoke(object):

    @pytest.mark.run(order=1)
    def test_run_sign_up(self):
        SignUpTest()

    @pytest.mark.run(order=2)
    def test_run_live_accounts(self):
        AddNewLiveAccountTestCA()

    @pytest.mark.run(order=3)
    def test_run_demo_accounts(self):
        AddDemoAccountsTestCA()

    @pytest.mark.run(order=4)
    def test_run_create_ticket(self):
        CreateSupportTicketTestCa()

    @pytest.mark.run(order=5)
    def test_run_deposit_ca(self):
        DepositTestCa()

    @pytest.mark.run(order=6)
    def test_run_withdraw(self):
        WithdrawTestCA()

    @pytest.mark.run(order=7)
    def test_run_transfer_funds(self):
        TransferFundsTestCA()

    @pytest.mark.run(order=8)
    def test_run_upload_documents(self):
        DownloadDocumentsTestCA()

    @pytest.mark.run(order=9)
    def test_run_change_password(self):
        ChangePasswordTestCA()

    @pytest.mark.run(order=10)
    def test_run_client_update(self):
        PersonalDetailsUpdateTestCA()

    @pytest.mark.run(order=11)
    def test_run_deposit_crm(self):
        DepositTestCRM()

    @pytest.mark.run(order=12)
    def test_run_credit_in_crm(self):
        CreditInTestCRM()

    @pytest.mark.run(order=13)
    def test_run_credit_out_crm(self):
        CreditOutTestCRM()

    @pytest.mark.run(order=14)
    def test_run_transfer_between_ta_crm(self):
        TransferBetweenTa()

    @pytest.mark.run(order=15)
    def run_check_password_crm(self):
        CheckPasswordTestCRM()

    @pytest.mark.run(order=16)
    def run_change_password_crm(self):
        ChangePasswordTestCRM()

    @pytest.mark.run(order=17)
    def run_add_interaction_crm(self):
        AddInteraction()
