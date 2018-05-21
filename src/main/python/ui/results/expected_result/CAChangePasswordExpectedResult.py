class CAChangePasswordExpectedResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, amount, account):
        print('\n' + "Expected result: " + "Transaction was performed successfully:  " + amount + " for  " +
              account + " account" + '\n')
