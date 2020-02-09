import pytest

from src.main.python.ui.crm.model.constants.EmailConstants import EmailConstants
from src.main.python.ui.crm.model.constants.FourthClientConstants import FourthClientConstants
from src.main.python.ui.crm.model.constants.MyDashboardConstants import MyDashboardConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.email.model.pages.EmailSignInPage import EmailSignInPage
from src.test.python.ui.automation.BaseTest import *
from src.test.python.ui.automation.utils.preconditions.task_module.ActionsTasksPrecondition import \
    ActionsTasksPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.MassEmailPrecondition import MassEmailPrecondition
from src.test.python.ui.automation.utils.preconditions.task_module.MassSmsPrecondition import MassSmSPrecondition
from src.test.python.ui.automation.utils.preconditions.mydashboard.MyDashboardPrecondition import MyDashboardPrecondition
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDEditEventPreconditionUI import \
    MDEditEventPreconditionUI
from src.test.python.ui.automation.utils.preconditions.my_dashboard_ui.MDEmailPreconditionUI import \
    MDEmailPreconditionUI


@pytest.mark.run(order=28)
class TestMyDashboardUI(BaseTest):

    def test_my_dashboard_edit_event_ui(self):
        MDEditEventPreconditionUI(self.driver, self.config).my_dashboard_edit_event_ui()

    def test_my_dashboard_email_ui(self):
        MDEmailPreconditionUI(self.driver, self.config).my_dashboard_email_ui()

    def test_sms_icon(self):
        MyDashboardPrecondition(self.driver, self.config).sms_icon()

    def test_searching_by_columns(self):
        MyDashboardPrecondition(self.driver, self.config).test_searching_by_columns()

    def test_sorting_columns(self):
        MyDashboardPrecondition(self.driver, self.config).test_sorting_columns()