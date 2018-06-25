from src.test.python.ui.automation.implementation.ca.Test_Add_Demo_Accounts import AddDemoAccountsTestCA
from src.test.python.ui.automation.implementation.ca.Test_Add_New_Live_Accounts import AddNewLiveAccountTestCA


class TestSmoke(object):

    def run_live_accounts(self):
        AddNewLiveAccountTestCA()

    def run_demo_accounts(self):
        AddDemoAccountsTestCA()
