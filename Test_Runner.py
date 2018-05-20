from unittest import TestLoader, TestSuite

import os
from src.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from src.test.python.ui.avtomation.implemetation.Test_Demo import TestDemo
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Add_Demo_Accounts import AddDemoAccounts
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Add_New_Live_Accounts import AddNewLiveAccount
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_Deposit import Deposit
from src.test.python.ui.avtomation.implemetation.ca_crm.Test_SignUp import SignUp

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(SignUp),
        loader.loadTestsFromTestCase(AddNewLiveAccount),
        loader.loadTestsFromTestCase(AddDemoAccounts),
        loader.loadTestsFromTestCase(Deposit),
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
