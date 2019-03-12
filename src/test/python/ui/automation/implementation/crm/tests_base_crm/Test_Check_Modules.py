import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.mydashboard.MyDashboardPrecondition import MyDashboardPrecondition
from src.test.python.ui.automation.utils.preconditions.audit_logs.AuditLogsPrecondition import AuditLogsPrecondition

@pytest.mark.run(order=35)
class CheckModulesTest(BaseTest):

    def test_my_dashboard_loading(self):
        MyDashboardPrecondition(self.driver, self.config).check_mydashboard_loading()

    def test_audit_logs_loading(self):
        AuditLogsPrecondition(self.driver, self.config).check_audit_logs_loading()