class DepositExpectedResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, amount, account):
        print('\n' + "Expected result: " + "Transaction was performed successfully:  " + amount + " for  " +
              account + " account" + '\n')
