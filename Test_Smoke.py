
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Searching_Clients import \
    SearchingClientsTestCRM


class TestSmoke(object):

    def run_test_searching_client_module(self):
        SearchingClientsTestCRM()

    def run_create_ticket(self):
        CreateSupportTicketTestCa()

