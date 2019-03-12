import pytest

from src.main.python.ui.crm.model.constants.CRMConstants import CRMConstants
from src.main.python.ui.crm.model.constants.TaskModule import TaskModuleConstants
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.side_bar.SidebarModules import SidebarModules
from src.test.python.ui.automation.BaseTest import *
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.ui.crm.model.side_bar.create_event.CreateEvent import CreateEvent
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from src.main.python.ui.crm.model.pages.client_profile.ClientProfilePage import ClientProfilePage
from src.main.python.ui.crm.model.pages.tasks.TasksPage import TasksPage
from src.test.python.ui.automation.utils.preconditions.dashboard.DashboardPrecondition import DashboardPrecondition
from src.test.python.ui.automation.utils.preconditions.leaderboard.LeaderboardPrecondition import LeaderboardPrecondition
from src.test.python.ui.automation.utils.preconditions.usermanagement.UserManagementPrecondition import UserManagementPrecondition

class CheckModules(BaseTest):

    def test_check_dashboard(self):
        DashboardPrecondition(self.driver, self.config).check_dashboard()

    def test_check_leaderboard(self):
        LeaderboardPrecondition(self.driver, self.config).check_leaderboard()

    def test_check_user_management(self):
        UserManagementPrecondition(self.driver, self.config).check_user_management()