import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.mydashboard.MyDashboardPrecondition import MyDashboardPrecondition
from src.test.python.ui.automation.utils.preconditions.audit_logs.AuditLogsPrecondition import AuditLogsPrecondition
from src.test.python.ui.automation.utils.preconditions.dashboard.DashboardPrecondition import DashboardPrecondition
from src.test.python.ui.automation.utils.preconditions.leaderboard.LeaderboardPrecondition import LeaderboardPrecondition
from src.test.python.ui.automation.utils.preconditions.usermanagement.UserManagementPrecondition import UserManagementPrecondition

@pytest.mark.run(order=35)
class CheckModulesTest(BaseTest):

    def test_my_dashboard_loading(self):
        MyDashboardPrecondition(self.driver, self.config).check_mydashboard_loading()

    def test_audit_logs_loading(self):
        AuditLogsPrecondition(self.driver, self.config).check_audit_logs_loading()

    def test_check_dashboard(self):
        DashboardPrecondition(self.driver, self.config).check_dashboard()

    def test_check_leaderboard(self):
        LeaderboardPrecondition(self.driver, self.config).check_leaderboard()

    def test_check_user_management(self):
        UserManagementPrecondition(self.driver, self.config).check_user_management()