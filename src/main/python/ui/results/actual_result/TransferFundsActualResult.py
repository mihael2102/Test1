class TransferFundsActualResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, first_transfer_account, amount, second_transfer_account):
        print('\n' + "Actual result: " + "I transferred from " + first_transfer_account + " to " +
              second_transfer_account + "  account " + "with the " + amount + " amount" + '\n')
