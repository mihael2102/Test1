from unittest import TestLoader, TestSuite

import os
from src.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Deposit import Deposit
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Download_Documents import DownloadDocuments
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Make_Transfer_Funds import TransferFunds

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(DownloadDocuments),
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
