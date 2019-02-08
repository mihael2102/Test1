from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var

class CAPage(CRMBasePage):

    def open_live_account(self):
        button = super().wait_load_element("//*[@id='dnn_ctl02_lblText']")
        button.click()
        Logging().reportDebugStep(self, "Click Open Live Account")
        return CAPage(self.driver)

    def click_check_box_confirm(self):
        check_box = super().wait_load_element("//*[@id='cbRiskAck']")
        check_box.click()
        Logging().reportDebugStep(self, "Click I am over 18 years of age and I have read and accepted these")
        return CAPage(self.driver)

    def click_confirm(self):
        confirm = super().wait_load_element("//*[@id='btnCloseRiskPopup']")
        confirm.click()
        Logging().reportDebugStep(self, "Click confirm")
        return CAPage(self.driver)

    def verify_relevant_currency(self):
        my_account_button = super().wait_load_element("//*[@id='mainmenu']/li[1]/a")
        my_account_button.click()
        sleep(8)
        currency = super().wait_load_element("//*[@id='RealAccountListBody']/tr/td[3]").text
        Logging().reportDebugStep(self, "Click My Account and check currency")
        return currency

    def verify_correct_data(self):
        leverage = super().wait_load_element("//*[@id='RealAccountListBody']/tr/td[2]").text
        Logging().reportDebugStep(self, "Check leverage")
        return leverage

    def open_demo_account(self):
        confirm = super().wait_load_element("//*[@id='btnNewPracticeAccount']")
        confirm.click()
        sleep(7)
        Logging().reportDebugStep(self, "Click add new demo account")
        return CAPage(self.driver)

    def select_currency(self):
        sleep(4)
        select = self.driver.find_element(By.XPATH, "//select[@name = 'dnn$ctr472$View$NewDemoAccountCurrency']")
        self.driver.execute_script("arguments[0].click();", select)
        usd_currency = self.driver.find_element(By.XPATH, "//select[@name = 'dnn$ctr472$View$NewDemoAccountCurrency']/option[1]")
        self.driver.execute_script("arguments[0].click();", usd_currency)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_leverage(self):
        sleep(4)
        select = self.driver.find_element(By.XPATH, "//select[@name = 'dnn$ctr472$View$SelLeverageP']")
        self.driver.execute_script("arguments[0].click();", select)
        select_leverage = self.driver.find_element(By.XPATH, "//select[@name = 'dnn$ctr472$View$SelLeverageP']/option[1]")
        self.driver.execute_script("arguments[0].click();", select_leverage)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_deposit(self):
        sleep(3)
        input = self.driver.find_element(By.XPATH, "//input[@name = 'InitialDepositP']")
        input.send_keys("1000")
        Logging().reportDebugStep(self, "Select Deposit")
        return CAPage(self.driver)

    def click_submit(self):
        click_submit = self.driver.find_element(By.XPATH, "//button[@class= 'blue_btn popup_mod_btn']")
        click_submit.click()
        Logging().reportDebugStep(self, "Click Submit")
        return CAPage(self.driver)

    def finish_button(self):
        click_submit = self.driver.find_element(By.XPATH, "//input[@class= 'green_btn popup_mod_btn centered']")
        click_submit.click()
        Logging().reportDebugStep(self, "Click Finish")
        return CAPage(self.driver)