from src.main.python.ui.crm.model.pages.home_page.CRMHomePage import CRMHomePage
from src.main.python.ui.crm.model.pages.login.CRMLoginPage import CRMLoginPage
from src.main.python.ui.crm.model.constants.TestDataConstants import TestDataConstants
from src.main.python.ui.crm.model.constants.LeaderboardConstants import LeaderboardConstants


class LeaderboardPrecondition(object):

    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def check_leaderboard(self):
        CRMLoginPage(self.driver).open_first_tab_page(self.config.get_value('url')) \
            .crm_login(self.config.get_value(TestDataConstants.USER_NAME),
                       self.config.get_value(TestDataConstants.CRM_PASSWORD),
                       self.config.get_value(TestDataConstants.OTP_SECRET))

        leaderboard = CRMHomePage(self.driver)\
            .open_more_list_modules()\
            .select_leaderboard_module_more_list(LeaderboardConstants.LEADERBOARD_MODULE)
        leaderboard.choose_group()
        leaderboard.enter_name_group(LeaderboardConstants.NAME_GROUP)
        leaderboard.click_button_go()
