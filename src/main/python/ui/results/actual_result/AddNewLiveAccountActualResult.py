class AddNewLiveAccountActualResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, account_id_ca, eur_currency_ca):
        print('\n' + "Actual result: " + "I got " + account_id_ca + " account and " +
              eur_currency_ca + " currency from client area" + '\n')
