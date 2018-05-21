class CAChangePasswordActualResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_check_invalid_message(self, old_password, message):
        print(
            '\n' + "Actual result: " + "Enter with old " + old_password + " password isn't possible  in CA:  " + ", the error  message is" +
            message + '\n')

    def print_change_password_actual_result(self, old, new_password):
        print(
            '\n' + "Actual result: " + "The password changed was performed successfully:  " + old + " password change to a  " +
            new_password + " new password " + '\n')

    def print_change_password_again_actual_result(self, old, new_password):
        print(
            '\n' + "Actual result: " + "The password was successfully changed again from " + new_password + " on the " +
            old + " old password " + '\n')
