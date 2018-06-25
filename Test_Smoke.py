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
