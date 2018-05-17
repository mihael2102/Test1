class TransferFundsExpectedResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, first_transfer_account, amount, second_transfer_account):
        print(
            '\n' + "Expected result: " + "I transferred from " + first_transfer_account + "  account to the " + second_transfer_account + "  account " + " successfully" + '\n'
            + " second transfer account : " + second_transfer_account + " = " + amount + '\n')
