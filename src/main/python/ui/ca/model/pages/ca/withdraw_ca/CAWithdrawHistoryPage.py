from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
import re
import autoit
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants


class CAWithdrawHistoryPage(CRMBasePage):

    def open_withdraw_history_tab(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Open Withdraw History tab")
        tab = super().wait_load_element("//a[text()='Withdraw History']")
        tab.click()
        return CAWithdrawHistoryPage(self.driver)

    def get_withdraw_status(self, row):
        sleep(0.1)
        Logging().reportDebugStep(self, "Get Status of withdraw from row: " + row)
        status = super().wait_load_element("//div[@class='history-pandats']//tbody/tr[%s]/td[2]" % row).text
        Logging().reportDebugStep(self, "Status of withdraw: " + status)
        return status
