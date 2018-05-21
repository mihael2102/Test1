class AddDemoAccountsExpectedResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, account_id_crm, cad_currency_crm, balance_crm):
        print(
            '\n' + "Expected result: " + "I opened the " + account_id_crm + " account with   "
            + cad_currency_crm + " currency and " + balance_crm + " balance" + " from CRM" + '\n')
