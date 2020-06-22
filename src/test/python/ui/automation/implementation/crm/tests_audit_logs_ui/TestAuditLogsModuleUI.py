import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.audit_logs_ui.AuditLogsSearchingColumnsPreconditionUI import \
    AuditLogsSearchingColumnsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.audit_logs_ui.AuditLogsEventsShownPreconditionUI import \
    AuditLogsEventsShownPreconditionUI


@pytest.mark.run(order=3)
class TestAuditLogsModuleUI(BaseTest):

    def test_audit_logs_searching_columns_ui(self):
        AuditLogsSearchingColumnsPreconditionUI(self.driver, self.config).audit_logs_searching_columns_ui()

    def test_new_events_shown_in_audit_logs_ui(self):
        AuditLogsEventsShownPreconditionUI(self.driver, self.config).new_events_shown_ui()
