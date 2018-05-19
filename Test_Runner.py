from unittest import TestLoader, TestSuite

import os

from scr.main.python.ui.core.reporter.HTMLTestRunner import HTMLTestRunner
from scr.test.python.ui.avtomation.implemetation.Test_Demo import TestDemo
from scr.test.python.ui.avtomation.implemetation.ca_crm.Test_SignUp import SignUp

direct = os.getcwd()

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestDemo),
        loader.loadTestsFromTestCase(SignUp)
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
