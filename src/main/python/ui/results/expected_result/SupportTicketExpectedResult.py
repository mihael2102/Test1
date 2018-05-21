class SupportTicketExpectedResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, subject_crm, category_tittle_crm, ticket_status_crm):
        print(
            '\n' + "Expected result: " + "I checked  the ticket with parameters:  " + subject_crm + " subject , " + category_tittle_crm + " category tittle,  " + ticket_status_crm + " ticket status , " + "from CRM" + '\n')
