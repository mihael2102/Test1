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


class CAWithdrawPage(CRMBasePage):

    def click_withdraw_funds(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Withdraw Funds' button")
        withdraw_btn = super().wait_load_element("//button[text()='Withdraw Funds ']")
        self.driver.execute_script("arguments[0].click();", withdraw_btn)
        return CAWithdrawPage(self.driver)

    def select_payment_method(self, method):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select '" + method + "' payment method")
        list_methods = super().wait_load_element("//custom-select[@name='paymentTypesList']")
        list_methods.click()
        item = super().wait_load_element(
            "//div[@class='frx-dropdown-content-pandats dropdown-show-pandats']//span[contains(text(),'%s')]" % method)
        self.driver.execute_script("arguments[0].click();", item)
        return CAWithdrawPage(self.driver)

    def set_expiry_month(self, month):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set '" + month + "' expiry month")
        field = super().wait_load_element("//input[@placeholder='MM']")
        field.clear()
        field.send_keys(month)
        return CAWithdrawPage(self.driver)

    def set_expiry_year(self, year):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set '" + year + "' expiry year")
        field = super().wait_load_element("//input[@placeholder='YYYY']")
        field.clear()
        field.send_keys(year)
        return CAWithdrawPage(self.driver)

    def set_cc_last_digits(self, digits):
        sleep(0.1)
        Logging().reportDebugStep(self, "Set CC last 4 digits: " + digits)
        field = super().wait_load_element("//input[@name='number']")
        field.clear()
        field.send_keys(digits)
        return CAWithdrawPage(self.driver)

    def select_withdrawal_reason(self, reason):
        sleep(0.1)
        Logging().reportDebugStep(self, "Select withdrawal reason: " + reason)
        item = super().wait_load_element(
            "//span[contains(text(),'%s')]" % reason)
        self.driver.execute_script("arguments[0].click();", item)
        return CAWithdrawPage(self.driver)

    def click_submit(self):
        sleep(0.1)
        Logging().reportDebugStep(self, "Click 'Submit' button")
        submit_btn = super().wait_load_element("//button[text()=' Submit ']")
        self.driver.execute_script("arguments[0].click();", submit_btn)
        sleep(0.5)
        return CAWithdrawPage(self.driver)
