from unittest import TestLoader, TestSuite

import os
from src.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from src.test.python.ui.avtomation.implemetation.ca.Test_Change_Password import CAChangePasswordFrom
from src.test.python.ui.avtomation.implemetation.ca.Test_Add_Demo_Accounts import CAAddDemoAccounts
from src.test.python.ui.avtomation.implemetation.ca.Test_Add_New_Live_Accounts import CAAddNewLiveAccount
from src.test.python.ui.avtomation.implemetation.ca.Test_Download_Documents import CADownloadDocuments
from src.test.python.ui.avtomation.implemetation.ca.Test_Make_Transfer_Funds import CATransferFunds
from src.test.python.ui.avtomation.implemetation.ca.Test_Make_Withdraw import CAWithdraw
from src.test.python.ui.avtomation.implemetation.ca.Test_SignUp import SignUp
from src.test.python.ui.avtomation.implemetation.ca.Test_Support_Ticket import CACreateSupportTicket

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUp),
        loader.loadTestsFromTestCase(CAAddNewLiveAccount),
        loader.loadTestsFromTestCase(CAAddDemoAccounts),
        loader.loadTestsFromTestCase(CATransferFunds),
        loader.loadTestsFromTestCase(CADownloadDocuments),
        loader.loadTestsFromTestCase(CACreateSupportTicket),
        loader.loadTestsFromTestCase(CAWithdraw),
        loader.loadTestsFromTestCase(CAChangePasswordFrom),
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
