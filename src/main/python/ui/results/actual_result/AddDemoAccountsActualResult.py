class AddDemoAccountsActualResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, account_id_ca, usd_currency_ca, balance_ca):
        print(
            '\n' + "Actual result: " + "I opened the " + account_id_ca + " account with   "
            + usd_currency_ca + " currency and " + balance_ca + " balance" + " from CA" + '\n')
