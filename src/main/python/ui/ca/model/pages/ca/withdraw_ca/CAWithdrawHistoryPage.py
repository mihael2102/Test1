from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.utils.logs.Loging import Logging
from time import sleep


class CAWithdrawHistoryPage(CRMBasePage):

    def switch_first_tab_page(self):
        super().switch_first_tab_page()
        return CAWithdrawHistoryPage(self.driver)

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

    def click_cancel_btn(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Cancel' button")
        cancel_button = super().wait_load_element("//button[contains(text(),'Cancel')]")
        cancel_button.click()
        submit_cancel_button = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                            self.__class__.__name__)["submit_cancel_button"])
        submit_cancel_button.click()
        sleep(1)
        Logging().reportDebugStep(self, "Withdraw request was canceled")
        return CAWithdrawHistoryPage(self.driver)
