import pytest
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDEditEventPreconditionUI import \
    MDEditEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDEmailPreconditionUI import \
    MDEmailPreconditionUI
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDSmsPreconditionUI import \
    MDSmsPreconditionUI
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDSearchingPreconditionUI import \
    MDSearchingPreconditionUI
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDSortingPreconditionUI import \
    MDSortingPreconditionUI


@pytest.mark.run(order=28)
class TestMyDashboardUI(BaseTest):

    def test_my_dashboard_edit_event_ui(self):
        MDEditEventPreconditionUI(self.driver, self.config).my_dashboard_edit_event_ui()

    def test_my_dashboard_email_ui(self):
        MDEmailPreconditionUI(self.driver, self.config).my_dashboard_email_ui()

    def test_sms_ui(self):
        MDSmsPreconditionUI(self.driver, self.config).my_dashboard_sms_ui()

    def test_searching_columns_ui(self):
        MDSearchingPreconditionUI(self.driver, self.config).searching_columns_ui()

    def test_sorting_columns_ui(self):
        MDSortingPreconditionUI(self.driver, self.config).sorting_columns_ui()
