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


class CADepositPage(CRMBasePage):

    ''' In list of payment methods select PRAXIS '''
    def select_payment_method(self):
        sleep(0.1)
        try:
            praxis = super().wait_load_element("//div[@class='pay-method-pandats praxis ng-star-inserted']", 8)
            self.driver.execute_script("arguments[0].click();", praxis)
            Logging().reportDebugStep(self, "Praxis method was selected successfully")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "Selection of payment providers is not available")
        return CADepositPage(self.driver)

    def click_deposit_btn(self):
        sleep(0.1)
        try:
            deposit_btn = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                        self.__class__.__name__)["deposit_btn"])
            self.driver.execute_script("arguments[0].click();", deposit_btn)
            Logging().reportDebugStep(self, "Click DEPOSIT button")
        except(NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "DEPOSIT pop up is already opened")
        return CADepositPage(self.driver)

    ''' Check in deposit pop up loading Praxis iframe and in iframe available deposit button '''
    def check_deposit_page_loaded(self):
        sleep(0.1)
        ''' Check iframe is loaded '''
        try:
            self.driver.switch_to_frame(super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                            self.__class__.__name__)["deposit_iframe"]))
            Logging().reportDebugStep(self, "DEPOSIT iframe was loaded successfully")
        except(NoSuchFrameException, NoSuchElementException, TimeoutException):
            Logging().reportDebugStep(self, "DEPOSIT iframe is not exist in current brand")
        ''' Check any deposit button in iframe is available '''
        super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["deposit_page"])
        Logging().reportDebugStep(self, "DEPOSIT button in iframe is available")
        return CADepositPage(self.driver)
