from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.tests_clients_module.Test_Make_Credit_Out import CreditOutTestCRM


class TestRegression(object):

    def run_transfer_between_ta_crm(self):
        CreditInTestCRM()

    def run_check_password_crm(self):
        CreditOutTestCRM()
