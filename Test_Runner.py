import unittest
from unittest import TestLoader, TestSuite
from src.test.python.ui.automation.implementation.Test_Demo import TestDemo

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestDemo)
    ))

    # run test sequentially using simple TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
