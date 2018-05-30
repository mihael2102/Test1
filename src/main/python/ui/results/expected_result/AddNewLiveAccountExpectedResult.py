class AddNewLiveAccountExpectedResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, account_id_crm, eur_currency_crm):
        print('\n' + "Expected result: " + "I got " + account_id_crm + " account and "
              + eur_currency_crm + " currency from CRM" + '\n')
