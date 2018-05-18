import unittest
from unittest import TestLoader, TestSuite

import os
from scr.main.python.ui.brand.core.reporter.HTMLTestRunner import HTMLTestRunner
from scr.test.python.ui.avtomation.implemetation.Test_Demo import TestDemo

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestDemo)
    ))

    outfile = open(direct + "\Regression.html", "w")
    runner_report = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Regression Tests'
    )

    runner_report.run(suite)
    # #run test parallel using concurrent_suite
