import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.audit_logs_ui.AuditLogsSearchingColumnsPreconditionUI import \
    AuditLogsSearchingColumnsPreconditionUI


@pytest.mark.run(order=3)
class TestAuditLogsModuleUI(BaseTest):

    def test_audit_logs_searching_columns_ui(self):
        AuditLogsSearchingColumnsPreconditionUI(self.driver, self.config).audit_logs_searching_columns_ui()
