import unittest
from unittest import TestLoader, TestSuite
from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.automation.implementation.ca.Test_Change_Password import ChangePasswordTestCA
from src.test.python.ui.automation.implementation.ca.Test_Download_Documents import DownloadDocumentsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Deposit import DepositTestCa
from src.test.python.ui.automation.implementation.ca.Test_Make_Transfer_Funds import TransferFundsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Make_Withdraw import WithdrawTestCA
from src.test.python.ui.automation.implementation.ca.Test_Personal_Details_Update import PersonalDetailsUpdateTestCA
from src.test.python.ui.automation.implementation.ca.Test_SignUp import SignUpTest
from src.test.python.ui.automation.implementation.ca.Test_Support_Ticket import CreateSupportTicketTestCa
from src.test.python.ui.automation.implementation.crm.Test_Add_Interaction import AddInteraction
from src.test.python.ui.automation.implementation.crm.Test_Change_Password import ChangePasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Check_Password import CheckPasswordTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_In import CreditInTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Credit_Out import CreditOutTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Deposit import DepositTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Make_Withdraw import WithdrawTestCRM
from src.test.python.ui.automation.implementation.crm.Test_Transfer_Between_Ta import TransferBetweenTa

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUpTest),
        loader.loadTestsFromTestCase(AddNewLiveAccountTestCA),
        loader.loadTestsFromTestCase(AddDemoAccountsTestCA),
        loader.loadTestsFromTestCase(CreateSupportTicketTestCa),
        loader.loadTestsFromTestCase(DepositTestCa),
        loader.loadTestsFromTestCase(WithdrawTestCA),
        loader.loadTestsFromTestCase(TransferFundsTestCA),
        loader.loadTestsFromTestCase(DownloadDocumentsTestCA),
        loader.loadTestsFromTestCase(ChangePasswordTestCA),
        loader.loadTestsFromTestCase(PersonalDetailsUpdateTestCA),
        loader.loadTestsFromTestCase(DepositTestCRM),
        loader.loadTestsFromTestCase(WithdrawTestCRM),
        loader.loadTestsFromTestCase(CreditInTestCRM),
        loader.loadTestsFromTestCase(CreditOutTestCRM),
        loader.loadTestsFromTestCase(TransferBetweenTa),
        loader.loadTestsFromTestCase(CheckPasswordTestCRM),
        loader.loadTestsFromTestCase(ChangePasswordTestCRM),
        loader.loadTestsFromTestCase(AddInteraction)

    ))

    # run test sequentially using simple TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
