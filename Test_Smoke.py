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

    def run_sign_up(self):
        SignUpTest()

    def run_live_accounts(self):
        AddNewLiveAccountTestCA()

    def run_demo_accounts(self):
        AddDemoAccountsTestCA()

    def run_create_ticket(self):
        CreateSupportTicketTestCa()

    def run_deposit_ca(self):
        DepositTestCa()

    def run_withdraw(self):
        WithdrawTestCA()

    def run_transfer_funds(self):
        TransferFundsTestCA()

    def run_upload_documents(self):
        DownloadDocumentsTestCA()

    def run_change_password(self):
        ChangePasswordTestCA()

    def run_client_update(self):
        PersonalDetailsUpdateTestCA()

    def run_deposit_crm(self):
        DepositTestCRM()

    def test_run_credit_in_crm(self):
        CreditInTestCRM()

    def run_credit_out_crm(self):
        CreditOutTestCRM()

    def run_transfer_between_ta_crm(self):
        TransferBetweenTa()

    def run_check_password_crm(self):
        CheckPasswordTestCRM()

    def run_change_password_crm(self):
        ChangePasswordTestCRM()

    def run_add_interaction_crm(self):
        AddInteraction()
