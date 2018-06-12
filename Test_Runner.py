from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_Personal_Details_Update import PersonalDetailsUpdateTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa
from src.test.python.ui.automation.implementation.crm.Test_Make_Deposit import DepositTestCRM


class TestRunner(object):

    def run_sign_up(self):
        SignUpTest()

    def run_live_accounts(self):
        AddNewLiveAccountTestCA()

    def run_demo_accounts(self):
        AddDemoAccountsTestCA()

    def run_create_ticket(self):
        CreateSupportTicketTestCa()

    def run_client_update(self):
        PersonalDetailsUpdateTestCA()

    def run_deposit_crm(self):
        DepositTestCRM()
