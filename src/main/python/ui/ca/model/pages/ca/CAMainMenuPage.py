from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var


class CAMainMenuPage(CRMBasePage):

    def check_transaction_history_loaded(self):
        Logging().reportDebugStep(self, "Transaction History table is loaded")
        super().wait_load_element("//div[@class='history-pandats']")
        return CAMainMenuPage(self.driver)

    def open_account_details_tab(self):
        Logging().reportDebugStep(self, "Open Account Details tab")
        btn = super().wait_element_to_be_clickable("//i[@class='cmicon-person']")
        btn.click()
        return CAMainMenuPage(self.driver)

    def check_account_details_loaded(self):
        Logging().reportDebugStep(self, "Account Details table is loaded")
        super().wait_load_element("//label[contains(text(),'First Name')]")
        return CAMainMenuPage(self.driver)

    def open_verification_center_tab(self):
        Logging().reportDebugStep(self, "Open Verification Center tab")
        try:
            btn = super().wait_element_to_be_clickable("//i[@class='cmicon-check_box']", timeout=10)
            btn.click()
        except(NoSuchElementException, TimeoutException):
            pass
            Logging().reportDebugStep(self, "There is no Verification Center tab")
        return CAMainMenuPage(self.driver)

    def check_verification_center_loaded(self):
        try:
            super().wait_load_element("//span[contains(text(),'Proof of Identity')]", timeout=10)
            Logging().reportDebugStep(self, "Verification Center table is loaded")
        except(NoSuchElementException, TimeoutException):
            pass
            Logging().reportDebugStep(self, "There is no Verification Center tab")
        return CAMainMenuPage(self.driver)

    def open_service_desk_tab(self):
        try:
            Logging().reportDebugStep(self, "Open Service Desk tab")
            btn = super().wait_element_to_be_clickable("(//i[@class='cmicon-comment'])[1]", timeout=10)
            btn.click()
        except(NoSuchElementException, TimeoutException):
            pass
            Logging().reportDebugStep(self, "There is no Service Desk tab")
        return CAMainMenuPage(self.driver)

    def check_service_desk_loaded(self):
        try:
            super().wait_load_element("//button[text()='Create New Ticket']", timeout=10)
            Logging().reportDebugStep(self, "Service Desk table is loaded")
        except(NoSuchElementException, TimeoutException):
            pass
            Logging().reportDebugStep(self, "There is no Service Desk tab")
        return CAMainMenuPage(self.driver)

    def open_withdraw_tab(self):
        Logging().reportDebugStep(self, "Open Withdraw tab")
        btn = super().wait_element_to_be_clickable("//i[@class='cmicon-arrow']")
        btn.click()
        return CAMainMenuPage(self.driver)

    def check_withdraw_loaded(self):
        Logging().reportDebugStep(self, "Withdraw table is loaded")
        super().wait_load_element("//div[contains(text(),'Amount in')]")
        return CAMainMenuPage(self.driver)

    def open_manage_accounts_tab(self):
        Logging().reportDebugStep(self, "Open Manage Accounts tab")
        btn = super().wait_element_to_be_clickable("(//i[@class='cmicon-comment'])[2]")
        btn.click()
        return CAMainMenuPage(self.driver)

    def check_manage_accounts_loaded(self):
        Logging().reportDebugStep(self, "Manage Accounts table is loaded")
        super().wait_load_element("(//tr[@class='ng-star-inserted'])[1]")
        return CAMainMenuPage(self.driver)
