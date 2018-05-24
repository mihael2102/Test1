from unittest import TestLoader, TestSuite

import os
from src.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from src.test.python.ui.avtomation.implemetation.ca_crm.TestChangePasswordFromCA import ChangePasswordFromCA
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Add_Demo_Accounts import AddDemoAccounts
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Add_New_Live_Accounts import AddNewLiveAccount
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Download_Documents import DownloadDocuments
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Make_Transfer_Funds import TransferFunds
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Make_Withdraw_CA import CAWithdraw
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_SignUp import SignUp
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Support_Ticket import CreateSupportTicket

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUp),
        loader.loadTestsFromTestCase(AddNewLiveAccount),
        loader.loadTestsFromTestCase(AddDemoAccounts),
        loader.loadTestsFromTestCase(TransferFunds),
        loader.loadTestsFromTestCase(DownloadDocuments),
        loader.loadTestsFromTestCase(CreateSupportTicket),
        loader.loadTestsFromTestCase(CAWithdraw),
        loader.loadTestsFromTestCase(ChangePasswordFromCA),
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
