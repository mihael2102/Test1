import pytest
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.sign_up.BrandSignUpPrecondition import BrandSignUpPrecondition
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.ca.model.pages.login.CALoginPage import CALoginPage
from src.test.python.ui.automation.utils.preconditions.login_ca.Login_CA_Preconditions import LoginCAPrecondition
from src.test.python.ui.automation.utils.preconditions.base_pages_ca.Base_Pages_CA_Preconditions import \
    BasePagesCAPrecondition
from src.test.python.ui.automation.utils.preconditions.trading_process_ca.GraphPreconditionCA import GraphPreconditionCA


@pytest.mark.run(order=2)
class TestPagesCA(BaseTest):

    def test_main_menu_pages_loading(self):
        BasePagesCAPrecondition(self.driver, self.config).main_menu_pages_loading()

    def test_graphs_loading(self):
        BasePagesCAPrecondition(self.driver, self.config).graphs_loading()

    def test_graph_ca(self):
        GraphPreconditionCA(self.driver, self.config).verify_graph_ca()
