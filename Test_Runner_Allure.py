import unittest

from src.test.python.ui.automation.implementation.Test_Demo import TestDemo
from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA


class TestRunnerAllure(unittest.TestCase):

    def run_tests(self):
        AddDemoAccountsTestCA()
        TestDemo()
