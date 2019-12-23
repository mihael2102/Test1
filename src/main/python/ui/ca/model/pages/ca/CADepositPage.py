from selenium.webdriver.common.by import By
from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage
from src.main.python.ui.crm.model.pages.main.ClientsPage import ClientsPage
from src.main.python.utils.logs.Loging import Logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import pyotp
from selenium.webdriver.support.select import Select
import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
from src.main.python.ui.ca.model.constants.CAconstants.CAConstants import CAConstants
import re
import autoit
from src.main.python.ui.ca.model.constants.CAconstants.TradingConstants import TradingConstants


class CADepositPage(CRMBasePage):

    def click_deposit_btn(self):
        sleep(0.1)
        deposit_btn = super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["deposit_btn"])
        self.driver.execute_script("arguments[0].click();", deposit_btn)
        Logging().reportDebugStep(self, "Click DEPOSIT button")
        return CADepositPage(self.driver)

    def check_deposit_page_loaded(self):
        sleep(0.1)
        if global_var.current_brand_name == "q8":
            self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//*[@id='cke_1_contents']/iframe"))
        super().wait_load_element(global_var.get_xpath_for_current_brand_element(
                                                    self.__class__.__name__)["deposit_page"])
        Logging().reportDebugStep(self, "DEPOSIT page was loaded successfully")
        return CADepositPage(self.driver)
