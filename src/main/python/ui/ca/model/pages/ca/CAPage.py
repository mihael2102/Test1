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
        sleep(2)
        button = super().wait_load_element("//*[@value='OPEN NEW ACCOUNT']")
        # button.click()
        self.driver.execute_script("arguments[0].click();", button)
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
        confirm = super().wait_load_element("//*[@value='NEW PRACTICE ACCOUNT']")
        self.driver.execute_script("arguments[0].click();", confirm)
        # confirm.click()
        sleep(2)
        Logging().reportDebugStep(self, "Click add new demo account")
        return CAPage(self.driver)

    def select_currency(self):
        sleep(3)
        select = super().wait_load_element("//*[@name='dnn$ctr472$View$NewDemoAccountCurrency']")
        # select.click()
        self.driver.execute_script("arguments[0].click();", select)
        usd_currency = super().wait_load_element("//*[@class='popup_mod_select']/option[1]")
        self.driver.execute_script("arguments[0].click();", usd_currency)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_leverage(self):
        sleep(3)
        select = super().wait_load_element("//*[@id='SelLeverageP']")
        select.click()
        select_leverage = super().wait_load_element("//select[@id='SelLeverageP']/option[1]")
        self.driver.execute_script("arguments[0].click();", select_leverage)
        Logging().reportDebugStep(self, "Select USD currency")
        return CAPage(self.driver)

    def select_deposit(self):
        sleep(3)
        input = super().wait_load_element("//*[@id='TextInitialDepositP']")
        input.send_keys("1000")
        Logging().reportDebugStep(self, "Select Deposit")
        return CAPage(self.driver)

    def click_submit(self):
        sleep(3)
        click_submit = super().wait_load_element("//button[@class= 'blue_btn popup_mod_btn']")
        click_submit.click()
        Logging().reportDebugStep(self, "Click Submit")
        return CAPage(self.driver)

    def finish_button(self):
        sleep(3)
        click_submit = super().wait_load_element("//input[@class= 'green_btn popup_mod_btn centered']")
        click_submit.click()
        Logging().reportDebugStep(self, "Click Finish")
        return CAPage(self.driver)