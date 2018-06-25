from src.test.python.ui.automation.implementation.ca.Test_Make_Deposit import DepositTestCa
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa


class TestSmoke(object):

    def run_create_ticket(self):
        CreateSupportTicketTestCa()

    def run_deposit_ca(self):
        DepositTestCa()
