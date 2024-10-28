import unittest
from HTMLTestRunner.runner import HTMLTestRunner

from test_login import TestLogin
from test_wallet import TestWallet
from test_plans import TestPlans

login_tests = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
wallet_tests = unittest.TestLoader().loadTestsFromTestCase(TestWallet)
plans_tests = unittest.TestLoader().loadTestsFromTestCase(TestPlans)
suite = unittest.TestSuite([login_tests, wallet_tests, plans_tests,])
runner = HTMLTestRunner(log=True, verbosity=2, output="reports", report_name="risevest_tests",
                        title="Risevest Test Cases", description="Risevest Test Cases",
                        open_in_browser=True, tested_by="Ikechukwu A.", add_traceback=True)
runner.run(suite)
