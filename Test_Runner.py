from unittest import TestLoader, TestSuite

import os
from src.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from src.test.python.ui.avtomation.implemetation.ca.Test_Change_Password import ChangePasswordTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_Download_Documents import DownloadDocumentsTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_Make_Transfer_Funds import TransferFundsTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_Make_Withdraw import WithdrawTestCA
from src.test.python.ui.avtomation.implemetation.ca.Test_SignUp import SignUpTest
from src.test.python.ui.avtomation.implemetation.ca.Test_Support_Ticket import CreateSupportTicketTestCa

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUpTest),
        loader.loadTestsFromTestCase(AddNewLiveAccountTestCA),
        loader.loadTestsFromTestCase(AddDemoAccountsTestCA),
        loader.loadTestsFromTestCase(TransferFundsTestCA),
        loader.loadTestsFromTestCase(DownloadDocumentsTestCA),
        loader.loadTestsFromTestCase(CreateSupportTicketTestCa),
        loader.loadTestsFromTestCase(WithdrawTestCA)
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
