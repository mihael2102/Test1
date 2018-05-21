class SupportTicketActualResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, subject_ca, category_tittle_ca, ticket_status_ca, ca_id):
        print(
            '\n' + "Actual result: " + "I create  the ticket with parameters:  " + subject_ca + " subject , " + category_tittle_ca + " category tittle,  " + ticket_status_ca + " ticket status , " + ca_id + " id " + "from CA" + '\n')
