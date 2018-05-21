class DepositActualResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, amount, account):
        print('\n' + "Actual result: " + "I performed the deposit from CRM with " + amount + " for  " +
              account + " account" + '\n')
