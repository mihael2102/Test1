class WithdrawActualResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_first_actual_result(self, withdraw_status, account):
        print(
            '\n' + "Actual result: " + "Withdraw was performed successfully from   " + account + " the withdraw status is " +
            withdraw_status + " status" + '\n')

    def print_second_actual_result(self, withdraw_cancel_request, account):
        print(
            '\n' + "Actual result: " + "Withdraw  cancel was perform successfully for   " + account + " the withdraw status is " +
            withdraw_cancel_request + " status" + '\n')
